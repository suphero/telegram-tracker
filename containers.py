from dependency_injector import containers, providers

from handler.config_handler import ConfigHandler
from handler.data_handler import DataHandler
from handler.telegram_handler import TelegramHandler
from client.telegram_client import MyTelegramClient
from handler.tracking_handler import TrackingHandler


class Container(containers.DeclarativeContainer):
    config_handler = providers.Factory(
        ConfigHandler
    )

    telegram_client = providers.Singleton(
        MyTelegramClient,
        config_handler=config_handler
    )

    data_handler = providers.Factory(
        DataHandler,
        config_handler=config_handler
    )

    telegram_handler = providers.Factory(
        TelegramHandler,
        telegram_client=telegram_client
    )

    tracking_handler = providers.Factory(
        TrackingHandler,
        telegram_handler=telegram_handler,
        config_handler=config_handler,
        data_handler=data_handler
    )
