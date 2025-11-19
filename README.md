# Way of the Datastar

## Author notes

-   This is a distilled version of my personal notes from reading various thinkpiece about a novel way of making websites / web apps using Datastar.
-   Essentially, it's like making a game: the app listens for user actions interacting with the page, the underlying data gets mutated, then the page gets re-rendered to reflect said changes.
-   Credit me (Huangphoux) if you decide to use all, or some part of this.

# Datastar

-

# Hypermedia + Fat Morphing + SSE + Brotli

1.  **Generalize hypermedia controls**: `data-on:click="@get('/endpoint')"`
    -   Any element can make HTTP requests: `data-on`
    -   Any event can trigger HTTP requests: `click`
    -   HTML can interact with the server: `@get('/endpoint')`
2.  **Fat Morphing**: responses can replace elements within the current document
    -   Respond with `<main>`
    -   Morph elements that have matching IDs in both the new and the old `<main>`
3.  **SSE**: open an long-lived connection to stream reponses to the client, compressing that stream using **Brotli**

# data-on: the only Attribute that you would need

-   There are also other `data-on` attributes for non-standard events:
    -   `data-init`: used to be `data-on-load`
    -   `data-on-intersect`
    -   `data-on-interval`
    -   `data-on-signal-patch`
    -   `data-on-signal-patch-filter`

# Fat Morphing

-   Suitable for collaborative app: all users see the same updated page

## Fat: Sending Complete `<main>`

-   Send the entire modified `<main>` instead of small, specific fragments.
-   Reduce the need for numerous endpoints to handle fragment updates.
-   Event Bubbling: `data-on` on `<main>` is enough
-   Use `data-on:pointerdown/mousedown` rather than `data-on:click` → No need to wait for `pointerup/mouseup`

## Morphing

-   Also called "Patching": `Create`, `Update` and `Delete`
-   Leave it to the algorithm to modify the current page

## View = Function(State)

-   A function turning state into view
-   Present data using HTML, then render it as a page
-   All data stored and processed on the server ⇒ No need for separating the Front-End and the Back-End
-   On every data change, the page gets re-rendered
-   Each page only needs one single render function

### CQRS

-   Command Query Responsibility Segregation
-   Commands
    -   `Create`, `Update` and `Delete`
    -   User actions on the page that change the application's states
-   Query
    -   `Read`
    -   The render function retrieves data to compute the view
-   Separate Commands from Query: any user actions that interact with the page should affect the data underneath, so that the re-rendered view can reflect those changes

# SSE + Brotli

## SSE

-   Suitable for real time app: updates can be sent in a stream that get compressed for its whole duration
-   Use HTTP/2 for more connections than HTTP/1
-   Can be inspected in the browser's DevTools

## Brotli

-   Specifically created to compress HTTP stream
-   Compressing a stream of data is better because of duplications in the stream, compression can reduce those duplications
-   Tunable context window: how much the compressor can remember about the past and current data
    -   Increase from the default 32 kB can reduce network for sending data, and CPU usage on the client

---

# From this point onward, it's mostly minor details regarding using Datastar.

# Misc.

-   Use query parameters or request body to store states in the URL
-   Avoid path parameters as they enforce a hierarchical structure

# Multiplayer

-   Multiplayer: real time + collaborative
-   The function rendering the view don't distinguish users, so that it renders the same view for everyone
-   To show user-specific views, create them in that same function, and send them to that user's stream only

# Signals

-   Add client-side reactivity to a page
-   Use as few signals as possible to avoid the need for signal management, alongside with state management
-   Datastar stores all signals in one object in every request, so the server still has full access to the client's state
-   Declare all signals with `__ifmissing` to prevent mutating existing signals: `data-signals:foo__ifmissing="1"`
    -   `__ifmissing`: Only patches signals if their keys do not already exist.
-   Add an underscore to not include that signal in requests to the backend: `data-signals:_foo="1"`
-   Signals are not stored persistently, and are not shared between tabs.

# Limitations

-   No progressive enhancement
    -   JavaScript is needed.
-   No History API support
    -   Add new history entry: redirect to a new page
    -   How to deal with state
        -   Make state a part of the URL
        -   Put state in cookie
-   PWA is impossible
