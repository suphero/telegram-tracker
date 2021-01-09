import asyncio
import sys

from dependency_injector.wiring import inject, Provide

from containers import Container

from performance_handler import PerformanceHandler
from telegram_client import MyTelegramClient
from tracking_handler import TrackingHandler


@inject
async def main(
    telegram_client: MyTelegramClient = Provide[Container.telegram_client],
    tracking_handler: TrackingHandler = Provide[Container.tracking_handler]
) -> None:
    performance_handler = PerformanceHandler("{:.2f} seconds passed")
    with performance_handler:
        async with telegram_client:
            await tracking_handler.track()


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(*sys.argv[1:]))
    loop.close()
