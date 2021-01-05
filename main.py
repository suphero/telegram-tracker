import asyncio

from config import ConfigHandler
from data import DataHandler
from performance import PerformanceHandler
from telegram import TelegramHandler, MyTelegramClient
from tracking import TrackingHandler

config_handler = ConfigHandler()
data_handler = DataHandler(config_handler)
performance_handler = PerformanceHandler("{:.2f} seconds passed")
telegram_client = MyTelegramClient(config_handler)
telegram_handler = TelegramHandler(telegram_client)
tracking_handler = TrackingHandler(telegram_handler, config_handler, data_handler)


async def main():
    with performance_handler:
        async with telegram_handler:
            await tracking_handler.track()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
