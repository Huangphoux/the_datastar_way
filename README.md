# Way of the [Datastar](https://data-star.dev/)

## [Author](https://github.com/Huangphoux/) Notes

-   This is a distilled version of my personal notes from reading various thinkpiece about a novel way of making websites / web apps using [Datastar](https://data-star.dev/).
-   Essentially, it's like making a game: the app listens for user actions interacting with the page, the underlying data gets mutated, then the page gets re-rendered to reflect said changes.
-   Credit me ([Huangphoux](https://github.com/Huangphoux/)) if you use any part of this.

# [Datastar](https://data-star.dev/)

-   Consider using [Datastar](https://data-star.dev/) if you want to build [real-time](https://example.andersmurphy.com/), [collaborative](https://checkboxes.andersmurphy.com/) web apps.
-   You can also utilize this technology to build simple websites as well, since it's a [simpler mental model](https://yagni.club/3m475dwkjvc2o/l-quote/39_0-39_329#39_0).

# [Hypermedia System](https://hypermedia.systems/) + [Fat Morphing](https://data-star.dev/how_tos/prevent_sse_connections_closing) + [SSE](https://yagni.club/3m475dwkjvc2o) + [Brotli](https://andersmurphy.com/2025/04/15/why-you-should-use-brotli-sse.html)

-   [Hypermedia System](https://hypermedia.systems/): send HTML over the wire instead of [JSON](https://htmx.org/essays/hateoas/)
    -   Use `data-on` to generalize [hypermedia](https://hypermedia.systems/) controls: `data-on:click="@get('/endpoint')"`
        -   Any element can make HTTP requests: `data-on`
        -   Any event can trigger HTTP requests: `click`
        -   HTML can interact with the server: `@get('/endpoint')`

1.  [**Fat Morphing**](https://data-star.dev/how_tos/prevent_sse_connections_closing): responses can replace elements within the current document
    -   Respond with `<main>`
    -   Morph elements that have matching IDs in both the new and the old `<main>`
2.  **[SSE](https://yagni.club/3m475dwkjvc2o)**: open an long-lived connection to stream reponses to the client, compressing that stream using **[Brotli](https://andersmurphy.com/2025/04/15/why-you-should-use-brotli-sse.html)**

# [data-on](https://data-star.dev/reference/attributes#data-on): the only [attribute](https://data-star.dev/reference/attributes) that you would need

-   There are also other [`data-on`](https://data-star.dev/reference/attributes#data-on) [attributes](https://data-star.dev/reference/attributes) for non-standard events:
    -   [`data-init`](https://data-star.dev/reference/attributes#data-init): used to be [`data-on-load`](https://github.com/starfederation/datastar/releases/tag/v1.0.0-RC.6)
    -   [`data-on-intersect`](https://data-star.dev/reference/attributes#data-on-intersect)
    -   [`data-on-interval`](https://data-star.dev/reference/attributes#data-on-interval)
    -   [`data-on-signal-patch`](https://data-star.dev/reference/attributes#data-on-signal-patch)

# [Fat Morphing](https://data-star.dev/how_tos/prevent_sse_connections_closing)

-   Suitable for [collaborative](https://checkboxes.andersmurphy.com/) app: all users see the same updated page

## Fat

-   Send the entire modified `<main>` instead of small, specific fragments.
-   Reduce the need for numerous endpoints to handle fragment updates.
-   [Event Bubbling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/Event_bubbling): `data-on` on `<main>` is enough
-   Use `data-on:pointerdown/mousedown` rather than `data-on:click` → No need to wait for `pointerup/mouseup`

## Morphing

-   Also called "[Patching](https://data-star.dev/guide/getting_started#patching-elements)": `Create`, `Update` and `Delete`
-   Leave it to the [algorithm](https://github.com/bigskysoftware/idiomorph) to modify the current page

## [View = Function(State)](https://yagni.club/3m3anpetejc23)

-   A function turning state into view
-   Present data using HTML, then render it as a page
-   All data stored and processed on the server ⇒ No need for separating the Front-End and the Back-End
-   On every data change, the page gets re-rendered
-   Each page only needs one single render function

### CQRS

-   Command Query Responsibility Segregation
-   Commands
    -   `Create`, `Update` and `Delete` actions
    -   User actions on the page that change the application's states
-   Query
    -   `Read` action
    -   The render function retrieves data to compute the view
-   Separate Commands from Query: any user actions that interact with the page should affect the data underneath, so that the re-rendered view can reflect those changes

# [SSE](https://yagni.club/3m475dwkjvc2o) + [Brotli](https://andersmurphy.com/2025/04/15/why-you-should-use-brotli-sse.html)

## [SSE](https://yagni.club/3m475dwkjvc2o)

-   Suitable for [real-time](https://example.andersmurphy.com/) apps: updates can be sent in a stream that get compressed for its whole duration
-   Use [HTTP/2](https://github.com/alvarolm/datastar-resources/blob/main/docs/considerations.md#6-connection-sse-limit-on-http11) to allow more connections
-   Can be inspected in the browser's DevTools
-   `text/html` for initial page loads and [`text/event-stream`](https://data-star.dev/essays/event_streams_all_the_way_down) for everything else
-   [How do Server-Sent Events actually work?](https://stackoverflow.com/questions/7636165/how-do-server-sent-events-actually-work/11998868#11998868)

## [Brotli](https://andersmurphy.com/2025/04/15/why-you-should-use-brotli-sse.html)

-   Specifically created to compress HTTP stream
-   Compressing a stream of data is better because of duplications in the stream, compression can reduce those duplications
-   Tunable context window: how much the compressor can remember about the past and current data
    -   Increase from the default 32 kB can reduce network for sending data, and CPU usage on the client

---

# From this point onward, it's mostly minor details regarding using [Datastar](https://data-star.dev/).

# Misc.

-   Use query parameters or request body to store states in the URL
-   Avoid path parameters as they enforce a hierarchical structure

# Multiplayer

-   Multiplayer: real time + collaborative
-   The function rendering the view don't distinguish users, so that it renders the same view for everyone
-   To show user-specific views, create them in that same function, and send them to that user's stream only

# [Signals](https://data-star.dev/guide/reactive_signals)

-   Add client-side reactivity to a page
-   Use as few signals as possible to avoid the need for signal management, alongside with state management
-   Datastar stores all signals in one object in every request, so the server still has full access to the client's state
-   Declare all signals with `__ifmissing` to prevent existing signals getting patched: `data-signals:foo__ifmissing="1"`
-   Add an underscore to not include that signal in requests to the backend: `data-signals:_foo="1"`
-   Signals are not stored persistently, and are not shared between tabs.

# Limitations

-   No [progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement)
    -   JavaScript is needed.
    -   Consider alternatives: [htmx](https://htmx.org/)'s [`hx-boost`](https://htmx.org/attributes/hx-boost/), [Alpine](https://alpinejs.dev/)'s [Alpine-Ajax](https://alpine-ajax.js.org/)
-   Modern browsers only (no IE11 support)
-   No History API support
    -   Add new history entry: [redirect](https://data-star.dev/how_tos/redirect_the_page_from_the_backend) to a new page
    -   How to deal with state
        -   Make state a part of the URL
        -   Put state in cookie
-   [PWA](https://en.wikipedia.org/wiki/Progressive_web_app) capability is yet to be tested
