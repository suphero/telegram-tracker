from dependency_injector import containers, providers

from config_handler import ConfigHandler
from data_handler import DataHandler
from telegram_handler import TelegramHandler
from telegram_client import MyTelegramClient
from tracking_handler import TrackingHandler


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
