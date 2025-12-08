import asyncio
from fasthtml.common import *
from datastar_py.fasthtml import (
    datastar_response,
    ServerSentEventGenerator as SSE,
)
from datastar_py import attribute_generator as data

count = 0

counter = APIRouter(prefix="/counter")


@counter("/")
def index():
    return Body(data.init(f"@get('{updates}')"))(
        A("Home", href="/"),
        H1(count),
        P("Waiting for the button…"),
    )


def render():
    return Body(
        A("Home", href="/"),
        H1(count),
        Button(
            "+1",
            data.on("click", f"@get('{increment}')"),
        ),
    )


@counter("/increment")
async def increment():
    global count
    count += 1


@counter("/updates")
@datastar_response
async def updates():
    while True:
        yield SSE.patch_elements(render())

        fps = 24  # 60 fps = 1 frame every ~16.67ms,
        await asyncio.sleep(1 / fps)  # 1/60 ≈ 0.01667 seconds
