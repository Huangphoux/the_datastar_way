# Quotes to be intergrated

> The server has a global store for global count, and a session store, based on your session cookie, is used for user count. If you use F12 tools network tab in the browser you can see that when the user button is clicked the user button html is patched via a regular http PATCH request and response. When the global button is clicked, a PATCH request is sent to the server but there's just an OK response because the global button is updated by an long-running SSE connection on the page which sends an event from the server to your browser whenever anyone clicks the the global button.


> I find that if you want partial multiplayer you still have to do some considerations, like what if some parts need it but you want other parts of the page to only have your state. Sure its great for apps where everybody is seeing the same thing

> yes, you have to think about what user X can see... that doesn't go away


> htmx pattern: Client enters data —> send update to server, Server does some work —> send state update to client, Client morphs update, decides where to go from there, Client requests new view —> to server, Server updates state —> sends new view morph and signals to client, Even a simple (?) thing like a login / registration / forgot password form can end up quite chatty, and involve 30x redirects

> There is an example app in the zig SDK that has a single long lived SSE endpoint to broadcast state updates to all clients. Whenever it does the global broadcast, it customises the output for each client to match their current preferences (in this case sort order for a list of cats for sale). Client preferences are associated with a session cookie, sessions being unique to each client. So if client A places a new bid on a cat, client B gets updated via SSE with a list sorted by their preferences . When a client updates preferences, the server only updates that 1 session. It’s not much code, but it’s a bit subtle

> It’s a bit tricky to communicate that D* difference, as it’s a paradigm that is simply not possible using react or even htmx. When, for example, the client submits a login form, the client side can’t know in advance if it will succeed or not, so you always need a redirect on success., and therefore more chatty over the wire. Even htmx, the client can’t know in advance which element will get patched by the response. In D* you can just morph them straight to the main menu or whatever on a login success without any extra round trips. Might sound trivial, but it’s a massive difference for mobile clients. You can even ignore the whole window.location thing if you track all state at the backend. It takes a bit of getting used to thinking it out differently

> Will add to that - have encountered resistance in Enterprise(tm), where the “experts” argue that even htmx is too heavy on the server compared to react .. because SPA architecture somehow magically offloads performance to the mass of client machines … somehow. Even though it’s objectively easy to prove that generating html through a template is basically a no-op compared to generating equivalent json responses. The idea of managing all client state on the server must be enough to make these same “experts” wet their beds. Compare a few MB of fast access memory out of L3 cache vs the overhead of so many extra round trips doesn’t even compute in their minds. In their little world, accepting another socket connection, possibly spawning another thread, decoding and validating another encrypted cookie .. these are all “free” operations in the fantasy world of the enterprise architect.


> https://github.com/zangster300/northstar/tree/main/features

> With regards to "no progressive enhancement" in the limitations section... I'm not sure what you mean by it, but I would disagree and say a blanket statement like that is not necessarily true. You _can_ build progressively enhanced websites/applications using Datastar (I have tried it out, see https://github.com/Regaez/unac) but Datastar becomes more the "icing on top of the cake", so to speak. You can still follow progressive enhancement idealogy by ensuring your application can function (or at least, the core behaviour) without Datastar or JS, but you have to make compromises. It's not really that different from other js libraries Alpine Ajax or HTMX, in that regard. In many ways, Datastar promotes progressive enhancement (in my opinion) by encouraging you to use existing web standards wherever possible. But on the other hand, it also promotes architectural patterns that may not work so well when you take Datastar out of the equation. It's more a question of: does your core experience/minimum viable functionality lend itself to being operational without any JS? Is it worth it to do the extra work to make your application work with _and_ without Datastar? And if so, are you still benefiting from using Datastar?

> https://delaneyj.github.io/minification_measurements/ ⇒ Use the bundler

> https://www.youtube.com/watch?v=Cum5uN2634o

> [Datastar first impressions, coming from React](https://threadgold.nz/writing/datastar-coming-from-react) > [Datastar: Web Framework for the Future? - Chris Malek - Tech Writings](https://chrismalek.me/posts/data-star-first-impressions/) > [Why I switched from HTMX to Datastar](https://everydaysuperpowers.dev/articles/why-i-switched-from-htmx-to-datastar/) > [Using Datastar | Ian Smith](https://medium.com/@ianster/using-datastar-da1984a6cc77) > https://www.youtube.com/watch?v=kxl71T5XoQ0 > https://medium.com/@ianster/the-microlith-and-a-simple-plan-e8b168dafd9e
> What's up with NATS?

> Progressive enhancement
> You also dont need to specify the data: selector #foo if the fragment contains an ID (as it should) - idiomorph will just find it and deal with it. This all makes D\* is particularly compatible with brownfield apps, as you dont need to modify the html templates as you would with something liek htmx (eg adding hx-swap, hx-target etc...). Just send the fragment with the ID and/or data: selector and it will work. Should probably elaborate on this compared to hx-boost

> https://data-star.dev/videos

> https://github.com/WICG/declarative-partial-updates

> In the project's defense: datastar only makes sense when you think in a certain way: event streams, server controls the state, the ui becomes a projection of the stream. The maintainers frequently see people who stubbornly refuse to give this style of thinking a chance, and instead attempt to bend what they've made to traditional styles of thinking which lead to things being worse for the person asking for help. They've seen this pattern so many times, they are quick to jump

> https://stario.dev/ > https://github.com/banditburai/starhtml > https://github.com/go-via/via > https://github.com/banditburai/ft-datastar

> https://www.fastht.ml/docs/

-   Convert FastHTML's examples to use Datastar
-   Event bus

- https://github.com/derekr/get-to-getting?tab=readme-ov-file
- https://gist.github.com/gazpachoking/3a695467b4f25ad66bb8404e4209ae8b
- https://discord.com/channels/1296224603642925098/1362094432370819406

- https://data-star.dev/examples/form_data

> I do a mix of everythingz whatever best does the job. Some things are just straight MPA, post to an endpoint and return a page/redirect, some are that with `@post`, some are `@post` and return X events, some are CQRS with a long lived `/updates`

- [SSE vs WebSockets vs Long Polling](https://www.youtube.com/watch?v=n9mRjkQg3VE)