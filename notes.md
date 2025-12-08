
# [URL Design](https://gist.github.com/lobre/7432c39d7f0c1c4d9c8afe1bd173f0d4#results)

-   Use query parameters or request body to store states in the URL.
-   Avoid path parameters as they enforce a hierarchical structure.

# Multiplayer

-   Multiplayer: real-time + collaborative.
-   Multiplayer is the default behavior, since the views are shared to all users.
-   The function rendering the view doesn't distinguish users, so that it renders the same view for everyone.
-   To show user-specific views, create them in that same function, and send them to that user's stream only.

# [Signals](https://data-star.dev/guide/reactive_signals)

-   Add client-side reactivity to a page.
-   Start with 0 signals.
-   Datastar stores all signals in one object in every request, so the server still has full access to the client's state
-   Declare all signals with `__ifmissing` to prevent existing signals getting patched: `data-signals:foo__ifmissing="1"`
-   Add an underscore to not include that signal in requests to the backend: `data-signals:_foo="1"`
-   Signals are not stored persistently, and are not shared between tabs.

# Limitations

-   No [progressive enhancement](https://en.wikipedia.org/wiki/Progressive_enhancement).
    -   JavaScript is needed.
    -   Consider alternatives: htmx's [`hx-boost`](https://htmx.org/attributes/hx-boost/), [Alpine](https://alpinejs.dev/)'s [Alpine-Ajax](https://alpine-ajax.js.org/)
-   Modern browsers only (no IE11 support)
-   No History API support
    -   Add new history entry: [redirect](https://data-star.dev/how_tos/redirect_the_page_from_the_backend) to a new page
    -   How to deal with state
        -   Make state a part of the URL
        -   Put state in cookie
-   Offline functionality: uncharted territory, consider using [Service Workers](https://github.com/mvolkmann/htmx-offline).

# HTML generator
- A better alternative to templating engines
- Use your favorite language's features to write HTML directly in your code
- Maintain [Locality of Behaviour (LoB)](https://htmx.org/essays/locality-of-behaviour/) better: no separate file to maintain
- [Anders Muprhy](https://andersmurphy.com/) do this in their [Game of Life](https://github.com/andersmurphy/hyperlith/blob/master/examples/game_of_life/src/app/main.clj) code so I know I'm right 😎.

# FastHTML
- All-in-one package 