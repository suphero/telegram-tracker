import asyncio
import sys

from dependency_injector.wiring import inject, Provide

from containers import Container

from handler.performance_handler import PerformanceHandler
from handler.tracking_handler import TrackingHandler


@inject
async def main(
    tracking_handler: TrackingHandler = Provide[Container.tracking_handler]
) -> None:
    """
    Code entry point
    """
    performance_handler = PerformanceHandler("{:.2f} seconds passed")
    with performance_handler:
        await tracking_handler.track()


if __name__ == "__main__":
    container = Container()
    container.init_resources()
    container.wire(modules=[sys.modules[__name__]])

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(*sys.argv[1:]))
    loop.close()
