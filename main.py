import asyncio

from config import ConfigHandler
from data import DataHandler
from performance import PerformanceHandler
from telegram import TelegramHandler
from tracking import TrackingHandler

config_handler = ConfigHandler()
data_handler = DataHandler(config_handler)
telegram_handler = TelegramHandler(config_handler)
tracking_handler = TrackingHandler(telegram_handler, config_handler, data_handler)
performance_handler = PerformanceHandler("{:.2f} seconds passed")


async def main():
    with performance_handler:
        async with telegram_handler:
            await tracking_handler.track()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
