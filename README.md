# The [Datastar](https://data-star.dev/) Way

## [Author](https://github.com/Huangphoux/) Notes

-   This is a distilled version of my personal notes from reading various thinkpiece about a novel way of making websites / web apps using Datastar.
-   Essentially, it's like making a game: the app listens for user actions interacting with the page, the underlying data gets mutated, then the page gets re-rendered to reflect said changes.
-   Credit me (Huangphoux) if you use any part of this.
-   I added some additional sources that seems relevant, mostly of my own picking.

# Datastar

-   Consider using Datastar if you want to build [real-time](https://example.andersmurphy.com/), [collaborative](https://checkboxes.andersmurphy.com/) web apps without sacrificing any [performance](https://andersmurphy.com/2025/04/07/clojure-realtime-collaborative-web-apps-without-clojurescript.html).
-   You can also utilize this technology to build simple websites as well, since it's a [simpler mental model](https://yagni.club/3m475dwkjvc2o/l-quote/39_0-39_329#39_0).

# [Hypermedia System](https://hypermedia.systems/) + [Fat Morphing](https://data-star.dev/how_tos/prevent_sse_connections_closing#cqrs-pattern) + [SSE](https://yagni.club/3m475dwkjvc2o) + [Brotli](https://andersmurphy.com/2025/04/15/why-you-should-use-brotli-sse.html)

1.  **Hypermedia System**: send HTML over the wire instead of [JSON](https://htmx.org/essays/hateoas/)

    -   Use [`data-on`](https://data-star.dev/reference/attributes#data-on) to generalize hypermedia controls: `data-on:click="@get('/endpoint')"`
        -   Any [element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements) can make HTTP requests: `data-on`
        -   Any [event](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events) can trigger HTTP requests: `click`
        -   HTML can use all of the HTTP request methods using [Backend Actions](https://data-star.dev/guide/backend_requests#backend-actions): `@get('/endpoint')`

2.  **Fat Morphing**: respond with the whole modified `<body>`, then morph elements that have matching IDs in both the new and the old `<body>`
3.  **SSE**: open an long-lived connection to stream reponses to the client, compressing that stream using **Brotli**

# data-on: the only [attribute](https://data-star.dev/reference/attributes) that you would need

-   Check out Datastar [examples](https://data-star.dev/examples)!

-   There are also other `data-on` attributes for non-standard events:
    -   [`data-init`](https://data-star.dev/reference/attributes#data-init): used to be [`data-on-load`](https://github.com/starfederation/datastar/releases/tag/v1.0.0-RC.6)
    -   [`data-on-intersect`](https://data-star.dev/reference/attributes#data-on-intersect)
    -   [`data-on-interval`](https://data-star.dev/reference/attributes#data-on-interval)
    -   [`data-on-signal-patch`](https://data-star.dev/reference/attributes#data-on-signal-patch)
-   The string evaluated by `data-on` attributes are Datastar [expressions](https://data-star.dev/guide/datastar_expressions), you can do more than using only Backend Actions
    -   `data-on:click="confirm('Are you sure?') && @delete('/examples/delete_row/0')"`
-   Be sure to use request indicators, as they are an important UX aspect of any distributed apps: `data-indicator:_fetching`, `data-attr:disabled="$_fetching"`
    - `$_fetching` is a [signal](#signals) 
# Fat Morphing

-   Suitable for collaborative app: all users see the same updated page

## Fat

-   Send the entire modified `<body>` instead of small, specific fragments.
-   Reduce the need for numerous endpoints to handle fragment updates.
-   [Event Bubbling](https://javascript.info/bubbling-and-capturing): `data-on` on `<body>` is enough
-   Use `data-on:pointerdown/mousedown` rather than `data-on:click` → No need to wait for `pointerup/mouseup`

## Morphing

-   Also called "[Patching](https://data-star.dev/guide/getting_started#patching-elements)": `Create`, `Update` and `Delete`
-   Leave it to the [algorithm](https://github.com/bigskysoftware/idiomorph) to modify the current page

## [View = Function(State)](https://yagni.club/3m3anpetejc23)

-   A function turning state into view
-   Present data using HTML, then render it as a page
-   All data stored and processed on the server
-   On every data change, the page gets re-rendered
-   Each page only needs one single render function

## CQRS

-   Command Query Responsibility Segregation: separate Commands and Queries
-   Commands = `Create`, `Update` and `Delete`
    -   `POST`, `PATCH`, `DELETE`: change the data
    -   These actions should not directly update the view
        -   Queries already take care of that responsibility
        -   Instead of patching elements, patching signals is permitted
-   Queries: `Read`
    -   `GET`: retrieve data / watch for data changes → compute the view
    -   Work Sharing / Caching: cache data so the query runs only once, no matter how many users connect

## Event Sourcing

-   Queries watch for data changes by keeping a log of Commands
-   Whenever there's a new Command, the Queries retrieve the modified data

# SSE + Brotli

## SSE

-   Suitable for real-time apps: updates can be sent in a stream that get compressed for its whole duration
-   Use HTTP/2 or HTTP/3 to allow for more [connections](https://github.com/alvarolm/datastar-resources/blob/main/docs/considerations.md#6-connection-sse-limit-on-http11)
-   Can be inspected in the browser's DevTools
-   `text/html` for initial page loads and [`text/event-stream`](https://data-star.dev/essays/event_streams_all_the_way_down#the-solution) for everything else
-   [How do Server-Sent Events actually work?](https://stackoverflow.com/questions/7636165/how-do-server-sent-events-actually-work/11998868#11998868)

## Brotli

-   Specifically created to compress HTTP stream
-   Compressing a stream of data is better because of duplications in the stream, compression can reduce those duplications
-   Tunable context window: how much the compressor can remember about the past and current data
    -   Increase from the default 32 kB can reduce network for sending data, and CPU usage on the client

---

# From this point onward, it's mostly minor details regarding using Datastar.

# [URL Design](https://gist.github.com/lobre/7432c39d7f0c1c4d9c8afe1bd173f0d4#results)

-   Use query parameters or request body to store states in the URL
-   Avoid path parameters as they enforce a hierarchical structure

# Multiplayer

-   Multiplayer: real-time + collaborative
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
-   Offline functionality: uncharted territory, consider using a [service worker](https://github.com/mvolkmann/htmx-offline).
---
# Quotes to be intergrated

> multi-player is the default, you actually need to do a small amount of work to scope down the multi-player, which is a revelation if you've tried to do multi-player with other approaches. Maybe "multiplayer should be the default" ?  I was ideating a project at work and realized that adding "oh you don't know, just let them send a link to their peer who maybe does and they can pick up from there" was just a thing that could happen now that the backend is managing state

>  Start with full multiplayer and then tone it down where you need to.

> The server has a global store for global count, and a session store, based on your session cookie, is used for user count. If you use F12 tools network tab in the browser you can see that when the user button is clicked the user button html is patched via a regular http PATCH request and response. When the global button is clicked, a PATCH request is sent to the server but there's just an OK response because the global button is updated by an long-running SSE connection on the page which sends an event from the server to your browser whenever anyone clicks the the global button.

> I wouldn’t call it the “default” mode (though it probably is for you given the way you build apps). But “multi-player” is definitely the answer to most “what does Datastar give me that framework X doesn’t?” questions.

> I find that if you want partial multiplayer you still have to do some considerations, like what if some parts need it but you want other parts of the page to only have your state.  Sure its great for apps where everybody is seeing the same thing

>  yes, you have to think about what user X can see... that doesn't go away

> Client enters data —> send to server. Server does all the things —> completely transition the client to the new state in 1 hit. So much less going over the wire. Don’t ever need 30x redirects

> htmx pattern: Client enters data —> send update to server, Server does some work —> send state update to client, Client morphs update, decides where to go from there, Client requests new view —> to server, Server updates state —> sends new view morph and signals to client, Even a simple (?) thing like a login / registration / forgot password form can end up quite chatty, and involve 30x redirects 

> There is an example app in the zig SDK that has a single long lived SSE endpoint to broadcast state updates to all clients. Whenever it does the global broadcast, it customises the output for each client to match their current preferences (in this case sort order for a list of cats for sale). Client preferences are associated with a session cookie, sessions being unique to each client. So if client A places a new bid on a cat, client B gets updated via SSE with a list sorted by their preferences . When a client updates preferences, the server only updates that 1 session. It’s not much code, but it’s a bit subtle

> It’s a bit tricky to communicate that D* difference, as it’s a paradigm that is simply not possible using react or even htmx. When, for example, the client submits a login form, the client side can’t know in advance if it will succeed or not, so you always need a redirect on success., and therefore more chatty over the wire. Even htmx, the client can’t know in advance which element will get patched by the response. In D* you can just morph them straight to the main menu or whatever on a login success without any extra round trips. Might sound trivial, but it’s a massive difference for mobile clients. You can even ignore the whole window.location thing if you track all state at the backend. It takes a bit of getting used to thinking it out differently

> Will add to that - have encountered resistance in Enterprise(tm), where the “experts” argue that even htmx is too heavy on the server compared to react .. because SPA architecture somehow magically offloads performance to the mass of client machines … somehow. Even though it’s objectively easy to prove that generating html through a template is basically a no-op compared to generating equivalent json responses. The idea of managing all client state on the server must be enough to make these same “experts” wet their beds.  Compare a few MB of fast access memory out of L3 cache vs the overhead of so many extra round trips doesn’t even compute in their minds. In their little world, accepting another socket connection, possibly spawning another thread, decoding and validating another encrypted cookie .. these are all “free” operations in the fantasy world of the enterprise architect.

> https://github.com/starfederation/datastar-python/tree/develop/examples/fasthtml, All examples (except Django) include Inline Script Metadata (PEP 723), allowing them to be run with uv without first installing dependencies.

> https://github.com/zangster300/northstar/tree/main/features

> With regards to "no progressive enhancement" in the limitations section... I'm not sure what you mean by it, but I would disagree and say a blanket statement like that is not necessarily true. You *can* build progressively enhanced websites/applications using Datastar (I have tried it out, see https://github.com/Regaez/unac) but Datastar becomes more the "icing on top of the cake", so to speak. You can still follow progressive enhancement idealogy by ensuring your application can function (or at least, the core behaviour) without Datastar or JS, but you have to make compromises. It's not really that different from other js libraries Alpine Ajax or HTMX, in that regard. In many ways, Datastar promotes progressive enhancement (in my opinion) by encouraging you to use existing web standards wherever possible. But on the other hand, it also promotes architectural patterns that may not work so well when you take Datastar out of the equation. It's more a question of: does your core experience/minimum viable functionality lend itself to being operational without any JS? Is it worth it to do the extra work to make your application work with *and* without Datastar? And if so, are you still benefiting from using Datastar?

> https://delaneyj.github.io/minification_measurements/ ⇒ Use the bundler

> https://www.youtube.com/watch?v=Cum5uN2634o

> [Datastar first impressions, coming from React](https://threadgold.nz/writing/datastar-coming-from-react)
> [Datastar: Web Framework for the Future? - Chris Malek - Tech Writings](https://chrismalek.me/posts/data-star-first-impressions/)
> [Why I switched from HTMX to Datastar](https://everydaysuperpowers.dev/articles/why-i-switched-from-htmx-to-datastar/)
> [Using Datastar | Ian Smith](https://medium.com/@ianster/using-datastar-da1984a6cc77)
> https://www.youtube.com/watch?v=kxl71T5XoQ0
> https://medium.com/@ianster/the-microlith-and-a-simple-plan-e8b168dafd9e
> What's up with NATS?

> Progressive enhancement
> You also dont need to specify the data: selector #foo if the fragment contains an ID (as it should) - idiomorph will just find it and deal with it. This all makes D* is particularly compatible with brownfield apps, as you dont need to modify the html templates as you would with something liek htmx (eg adding hx-swap, hx-target etc...). Just send the fragment with the ID and/or data: selector and it will work. Should probably elaborate on this compared to hx-boost


> https://data-star.dev/videos

> https://github.com/WICG/declarative-partial-updates

> In the project's defense: datastar only makes sense when you think in a certain way: event streams, server controls the state, the ui becomes a projection of the stream. The maintainers frequently see people who stubbornly refuse to give this style of thinking a chance, and instead attempt to bend what they've made to traditional styles of thinking which lead to things being worse for the person asking for help. They've seen this pattern so many times, they are quick to jump
> 