from fasthtml.common import *
from brotli_asgi import BrotliMiddleware

from counter import counter
from temperature import temperature


app, rt = fast_app(
    htmx=False,
    surreal=False,
    hdrs=(
        Script(
            type="module",
            src="https://cdn.jsdelivr.net/gh/starfederation/datastar@v1.0.0-RC.6/bundles/datastar.js",
        ),
    ),
    middleware=(
        Middleware(
            BrotliMiddleware,
            quality=6,
            mode="text",
            lgwin=22,  # 2^22 bytes = 4194.304 kB
            lgblock=0,
            minimum_size=400,
            gzip_fallback=False,
        ),
    ),
)

counter.to_app(app)
temperature.to_app(app)


@rt
def index():
    return Titled(
        "7GUIs",
        Body(
            Ul(
                Li(A("Counter", href="/counter")),
                Li(A("Temperature Converter", href="/temperature")),
            )
        ),
    )


serve()
