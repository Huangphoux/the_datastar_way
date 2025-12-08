import asyncio
from fasthtml.common import *
from datastar_py.fasthtml import (
    datastar_response,
    ServerSentEventGenerator as SSE,
)
from datastar_py import attribute_generator as data


temperature = APIRouter("/temperature")

celcius: float = 0
fahrenheit: float = 0


@temperature("/")
def index():
    return Body(data.init(f"@get('{updates}')"))(
        A("Home", href="/"),
        P("Waiting for the Celcius textbox…"),
        P("Waiting for the Fahrenheit textbox…"),
        H1(celcius),
        H1(fahrenheit),
    )


def render():
    return Body(
        A("Home", href="/"),
        Label(
            "Celcius",
            Input(
                data.on("change__debounce.500ms", f"@get('{convert}')"),
                type="number",
                value=str(celcius),
            ),
        ),
        Label(
            "Fahrenheit",
            Input(
                data.on("change__debounce.500ms", f"@get('{convert}')"),
                type="number",
                value=str(fahrenheit),
            ),
        ),
    )


@temperature("/convert")
async def convert():
    global celcius, fahrenheit
    celcius = (fahrenheit - 32) * (5 / 9)
    fahrenheit = celcius * (9 / 5) + 32


@temperature("/updates")
@datastar_response
async def updates():
    while True:
        yield SSE.patch_elements(render())

        fps = 24  # 60 fps = 1 frame every ~16.67ms,
        await asyncio.sleep(1 / fps)  # 1/60 ≈ 0.01667 seconds
