# Way of the Datastar

## Author notes

-   This is a distilled version of my personal notes from reading various thinkpiece about a novel way of making websites / web apps using Datastar.
-   Essentially, it's like making a game: listen for user actions interacting with the page, the underlying data get mutated, then the page get re-rendered to reflect said changes.
-   Credit me (Huangphoux) if you decide to use all, or some part of this.

# Hypermedia + SEE + Brotli + Fat Morphing

1.  **Generalize hypermedia controls**: `data-on:click="@get('/endpoint')"`
    -   Any element can make HTTP requests: `data-on`
    -   Any event can trigger HTTP requests: `click`
    -   HTML can interact with the server: `@get()`
2.  **SSE**: open an long-lived connection to stream reponses to the client, compressing that stream using **Brotli**
3.  **Fat Morphing**: responses can replace elements within the current document
    -   Respond with `<main>`
    -   Morph elements that have matching IDs in both the new and the old `<main>`

# data-on: the only Attribute that you would need

-   `data-on-intersect`
-   `data-on-interval`
-   `data-on-signal-patch`
-   `data-on-signal-patch-filter`
-   `data-init`: used to be `data-on-load`

# Fat Morphing

-   Suitable for collaborative app: all users see the same updated page

## Fat

-   Send the whole modified `<main>`: avoid the abundance of endpoints for sending fragments
-   `data-on` on `<main>` is enough
-   Use `data-on:pointerdown/mousedown` rather than `data-on:click` → No need to wait for `pointerup/mouseup`

## Morphing

-   Leave it to the algorithm to modify the current page
-   ❌ Merging, ✅ Patching

## View = Function(State)

-   A function turning state into view
-   Present data using HTML, then render it as a page
-   All data stored and processed on the server ⇒ No CORS
-   On every data change, the page gets re-rendered
-   Each page only needs one single render function

# SSE + Brotli

## SSE

-   Suitable for real time app: updates can be sent in a stream that get compressed for its whole duration
-   Use HTTP/2 for more connections than HTTP/1
-   Can be inspected in the browser's DevTools

## Brotli

-   Specifically created to compress HTTP stream
-   Compressing a stream of data is better because of duplications in the stream, compression can reduce those duplications
-   Tunable context window: how much the compressor can remember about the past and current data
    -   The right amount can reduce network for sending data, and CPU usage on the client

---

From this point onward, it's mostly minor details regarding using Datastar.

# Misc.

-   Path parameter > Query parameter / Body: path parameters introduce hierarchy
-   CQRS: Separating `Create`, `Update` and `Delete` operations from `Read`

# Multiplayer

-   Multiplayer: real time + collaborative
-   How to show user-specific view?

# Signals

-   Add client-side reactivity to a page
-   Use as few signals as possible to avoid the need for signal management, alongside with state management
-   Server has full access to the client's state by sending all signals as an object in every request

# Cons

-   No progressive enhancement
-   No History API support
    -   Add new history entry: redirect to a new page
    -   How to deal with state
        -   Make state a part of the URL
        -   Put state in cookie
-   PWA is impossible
