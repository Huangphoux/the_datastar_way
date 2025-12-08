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

> [Why I switched from HTMX to Datastar](https://everydaysuperpowers.dev/articles/why-i-switched-from-htmx-to-datastar/) > [Using Datastar | Ian Smith](https://medium.com/@ianster/using-datastar-da1984a6cc77) > https://www.youtube.com/watch?v=kxl71T5XoQ0 > https://medium.com/@ianster/the-microlith-and-a-simple-plan-e8b168dafd9e

> Progressive enhancement
> You also dont need to specify the data: selector #foo if the fragment contains an ID (as it should) - idiomorph will just find it and deal with it. This all makes D\* is particularly compatible with brownfield apps, as you dont need to modify the html templates as you would with something liek htmx (eg adding hx-swap, hx-target etc...). Just send the fragment with the ID and/or data: selector and it will work. Should probably elaborate on this compared to hx-boost

> https://data-star.dev/videos

> https://github.com/WICG/declarative-partial-updates

> In the project's defense: datastar only makes sense when you think in a certain way: event streams, server controls the state, the ui becomes a projection of the stream. The maintainers frequently see people who stubbornly refuse to give this style of thinking a chance, and instead attempt to bend what they've made to traditional styles of thinking which lead to things being worse for the person asking for help. They've seen this pattern so many times, they are quick to jump

> https://stario.dev/ > https://github.com/banditburai/starhtml > https://github.com/go-via/via > https://github.com/banditburai/ft-datastar

> https://www.fastht.ml/docs/

-   Convert FastHTML's examples to use Datastar
-   Event bus

-   https://github.com/derekr/get-to-getting?tab=readme-ov-file
-   https://gist.github.com/gazpachoking/3a695467b4f25ad66bb8404e4209ae8b
-   https://discord.com/channels/1296224603642925098/1362094432370819406

-   https://data-star.dev/examples/form_data

> I do a mix of everythingz whatever best does the job. Some things are just straight MPA, post to an endpoint and return a page/redirect, some are that with `@post`, some are `@post` and return X events, some are CQRS with a long lived `/updates`

-   [SSE vs WebSockets vs Long Polling](https://www.youtube.com/watch?v=n9mRjkQg3VE)

> I suppose you'd use GET when you are using the form to just submit some sort of reference info that dictates what will be returned, rather than changing state. Eg. a search form would be GET and a contact form would be POST. Anyway, what I was referring to was that I think the example is much clearer now how it works - its really just a normal form, but you submit it as fetch/ajax. And the submission can happen from outside the form by using the selector. I dont know why it wasn't obvious to me previously, but i get it now

-   https://data-star.dev/guide/the_tao_of_datastar

```
Here's some feedback on the Tao.

> Since the frontend is exposed to the user, the backend should be the source of truth for your application state.

I agree, but it isn't really substantiated why.

Should some mention of Hypermedia, HATEOAS, etc be made - perhaps in reference to State in the Right place, and Use Signals Sparingly (state stored in backend, and effectively embedded in the hypermedia that is delivered to the browser)

> A good rule of thumb is to only use signals for user interactions (e.g. toggling element visibility) and for sending new state to the backend (e.g. form input fields).

Its still unclear to me whether signals or normal form elements + `contentType: 'form'` are recommended. I just got rid of signals and am using normal form stuff, and I find it to be working much better.

Should any mention of how to use ids properly be made? How about semantic html elements, vanilla js, browser apis, and browser standards?

Should there be any mention, perhaps in Page Navigation and/or Browser History, about how each page is a resource, but any variations on the current resource are either ephemeral, or can be stored in query string, etc?
```

```
> I agree, but it isn't really substantiated why.
It’s not intended to be. If each heading went into the why, this would turn into a massive guide.

> Should some mention of Hypermedia, HATEOAS, etc be made
Maybe.

> Its still unclear to me whether signals or normal form elements + contentType: 'form' are recommended.
The defaults (in this case `contentType: json`) are the recommended approach.

> Should any mention of how to use ids properly be made?
No, this is not a guide.

> Should there be any mention, perhaps in Page Navigation and/or Browser History, about how each page is a resource, but any variations on the current resource are either ephemeral, or can be stored in query string, etc?
No, this is not a guide.

The Tao is a recommended learning journey.
Here’s a map, go visit each point on it, explore, and then put the pieces together.
```

```
I also have some Tao feedback:

> loading indicators

The guidance on loading indicators subtly conflicts with the guidance on CQRS; loading indicators as implemented in the example don't work very well w/ a CQRS model as shown in the CQRS example because while the write's request has gone through when the indicator is reset to false, the read of the updated state has not yet necessarily been pushed down. So the indicator means "your write is in flight" but what users understand it to mean is more "waiting on updated state".

> optimistic updates

Delaney had a really good demo of some sort of graph or tree editor (can't remember the details or find the example) that had what might be called "honest optimistic UI" where the expected results of changes were immediately apparent without any deception. Maybe it would be good to link to that here so people can better understand? I think people might misunderstand this section as saying that your webpage will need to show loading indicators all over the place for all operations.
```

```
loading indicators: if using cqrs, you'd probably set a loading class before posting the command and remove it later via morph
optimistic updates: this one? https://data-star.dev/examples/rocket_flow
```

```
yep, that's the demo.

Manually setting and removing the loading indicator is the approach I've settled on as well for a cqrs/fat morph app, but that's not what this doc says to do, which is why I thought it was worth mentioning the discrepancy.
```

```
`openWhenHidden` should be true by default for POST/PUT/PATCH/DELETE

This may be controversial, but hear me out...

I find auto interrupting requests on visibility change to potentially be a footgun. For long lived GET requests I understand why and I can see no downsides, but for the other methods, I am not so sure.

Scenario:
- A user clicks a button and immediately changes tab,
- then the @post/@patch/@put/@delete is interrupted and restarted when the user comes back to the tab.
- The user thinks the thing is done, but in such a case there are many questions...

- Did the backend receive the request fully before it was interrupted?
- Did the backend react to the cancellation by interrupting the work?
- Will the backend recognise the repeat request as being the same and skip the work if it is already done?
- What if the user closes the tab without coming back to it?

I would argue that automatic interruption on visibility change is the right choice for GET's but that the default should be to not automatically interrupt POST/PUT/PATCH/DELETE. The docs should insist on the distinction, and mention that if you really need to use a POST where a GET would be more semantically correct, then we can always set openWhenHidden: false. Lest we forget the http spec already distinguishes GET requests from the others: they are cachable by default.

Granted
- The user should wait to verify the action has been processed correctly
- The backend should be idempotent for things that matter
- The backend can simply ignore the request cancellation but that only works if the cancellation happens once the request is fully received, and if the frontend is sending a file the window is large...
- I can just add openWhenHidden: true  where appropriate.
```

```
My main thought on this is: why are you holding a put/patch/post open at all? Unless, perhaps, you're streaming data to the backend somehow (which might be a better use case for web sockets?) shouldn't those almost always just be a single one and done request? And how would that differ from put/patch/post then change tab when not using  datastar?

The only concern I can think of is if you are submitting data with something like data-init, such that returning to the tab re-submits the data. But, if that's not actually desirable (eg presence indicators), then it shouldnt be done (eg use GET instead with data-init)

Also, which http method you use seems like it has little to do with d* and its docs
```

```
I am not holding them open longer than necessary, but if the @post is uploading a file, or if the database is unusually slow, or if the user does ctrl-tab unusually fast, then the automatic interruption of the request may cause a strange bug that will take forever to diagnose.
```

```
Uploading a file is a good example. But, otherwise, what is the "necessary" in "longer than necessary"? If the backend has received the request in its entirety, why does it matter if the user changes tabs/http connection closes before the db and application are done what they're doing? Can't they keep doing that?

Perhaps it would be more useful to discuss how this is handled when datastar is not in the picture. What happens if you submit a post, or whatever, and change tabs immediately?
```

```
Do some languages/frameworks kill the entire process if the http connection is closed? If so, again this doesn't seem to be a datastar problem. If not, well it's just not a problem at all.
```

```
When datastar is not in the picture a form submission via get or post is not interrupted when you change tabs, at least not quickly. My test route waits for 30s before replying and it isn't interrupted.
```

-   https://data-star.dev/essays/im_a_teapot

```
use data-on:submit="@post('/login', {contentType: 'form'}) and get the data the good old way as a regular form

use data-bind on each inputs, and on the button click, post to your endpoint, and retrieve the values as signals (or do inline validation on change on each input).

just do the button click handler, and do a @post('/foo/${retrieve user name here}/${retrieve password here}')
```

```
i think the distinction is you don't need <form>. you end up doing more work to use <form> then just binding to inputs and sending a post e.g. preventing default event of form submission. deserializing form data on the backend etc
```

```
d* does all the heavy lifting of gathering all bound signals/inputs and including them in the request and you don't need to deserialize on the backend

so instead of dealing with weird form data to build an array to work with you just get the array

plus you don't need the encapsulation/grouping of fields when using signals since they're all sent on every request

cuts through incidental complexity even if that complexity happens to be part of the paltform
```

```
So it means signals are the perfect replacement for `<form>` then 😁 . At least one scenario where we can recommend signals without thinking too much then 🤷 . I understand the idea of not advocating them too much here on the discord, but I feel that people now think that they should resist using them at all, which might not be acurate either.

User submission data (that originally lives inside of forms) exist and are pretty common in web applications, and so cannot be dismissed entierely. People should just learn how to handle them when using D*. But if forms are considered old school and less practical that signals (which makes sense to me as per the above criticisms), well, it means that they are useful and they should be used somehow.

At least I struggle to understand the 0-signals philosophy that we hear about here sometimes. From what I understand, 0-signals work for the kind of applications that can encode this user data inside the URL. But we cannot say that it generally applies to most apps. Most applications have a concept of password or secret somewhere, and passwords should not be passed in URLs for instance.
```

```
i think it's safer to recommend 0 signals or push that narrative. you'll know when you need them if you do. i said signals for input binding is a good default because this is a safe space [this thread] ;p.

vs people reaching for signals right away tend to use them for old/bad habits like tracking form dirty state, client side validation etc

isntead of strickly just binding the input value for sole use to hitch a ride to the backend

then the flip side is when you're driving true client state, but if you're doing CRUD it's not likely you'll need it

if you're rendering a 3d globe w/ markers and interactivity then yeah. signals are great here because you get a multiplayer 3d globe experience out of the box

like if most of the UX on the page is interacting with form inputs/sending updates you likely won't need to extensively use signals

other than binding the input values
```

```
My view generally (and this is just my opinion, I'm not being authoritative here) is if you are doing req/resp and forms you probably don't need datastar just do full MPA with view transitions.

I don't do that because I don't use forms (outside of file upload);and I like building everything in a CQRS style with a single streaming connection of updates. I find it's a super nice way of building things once it's set up. Mean I don't have two ways of doing things, realtime/multiplayer is the same as CRUD.
```

```
Also to give additional context as we're now in a thread: There is a trade-off to be made here how to do the initial load on your site:

[A] Send a stub, send the first "real content" down the fat morph long-lived SSE pipe down.
This will warm up the SSE context and subsequent updates will be much better compressed.

[B] Send the full page (you're doing a MPA right?), allowing dumber clients access to your content in full while paying the warm-up cost for the SSE/brotli stream on first interaction instead of first load.

I do B but I think quite a few people o this Discord do A
```

```
I mean B is fine. Just will double your time to first interactiviity with large content and a bad network when things get big

technically B speeds up your first meaningful content paint.
```

```
I do C: send the full page AND send the latest full page content again immediately when the SSE connection is opened on page init.

For my web app, it is highly likely that both will be exactly the same, so you probably won't see any flashes of content changing between the page load and the first SSE event, but it will warm up the Brotli stream before the first user interaction.

It also means you don't have a dependency on the SSE stream to serve a contentful experience, since the first page load contains everything.
```

```
Yeah B doesn't actually work, although unlikely you can miss events between the request and SSE getting set up, so you have to do C.
```

```
That seems to unfortunately be true. I hadn't considered that timing aspect, well not a big change but nipping stale state in the bud conceptually is good
```

```
So after reading some things on here, do i understand correctly that Fat Morphin is the best way to go abouts for updating anything UI related on the Page.  There isn't really a need to breaking things into fragments causing to manage multiple templates. Just target the body or html or main.  This saves the headache of managing Partial Blocks or templates...is that right?

Also, Full Page load via Anchors always when wanting to preserve browser navigation history
```

```
Honestly it's whatever is convenient for you, I've found both useful (targetted vs. full page)

but the nice think about datastar is that it make both options equally viable rather than forcing one or the other

It also depends on how your backend is setup, if you're doing regular request/response then targetted might be easier in some cases because you might not want to reload all the data for the whole page if your handler is responding directly with a patch to a specific request.

If you're following more of the CQRS style with 1 streaming endpoint for the page then fat morph is more convenient
```

```
1. Here is an example use case I have in mind... Professionally I work on a CRM/ERP type web application, so pretty CRUDdy for the most part.

Suppose the page /contacts/234 shows the details of a contact in a CRM, their contact info, recent meetings, qualifications they are looking for, notes, etc. So we have an SSE request open for updates to the resource.
Suppose the user has opened a modal to plan a new meeting, or to modify some part of the details of the contact. This might involve several fields with complex validation logic, so when we @post the form we want the backend to be able to reply with validation error annotations, or by closing the modal. This seems like a typical reasonable UI for this sort of app.

Now the modal represents a draft state of part of the main resource, so I don't really want to handle the validation error response, nor the modal closing response via the main SSE request for updates to the resource. It seems reasonable for the @post request to be the one that sends these two types of responses, this means that the request must be open for the duration of the processing, which with our crappy sql architecture can sometimes take a second or two.

Sales people are often pretty speedy people, most of them won't know about Ctrl-Tab, but those who do will be fast. In this case the request is cancelled mid-flight and restarted later on. If the data is invalid this is not too problematic, the server validates twice. If the data is valid, this might be more problematic.

I am sure I could find a way to make sure the processing is idempotent, but that seems to be an overcomplication in this case where openWhenHidden:true solves the problem.

You call this an edge case, but from the point of view of someone who works on CRUDdy apps, it seems to be pretty common.

2. Having different defaults per verb doesn't seem to be too much of a stretch. According to the specs, GETs are different to the other verbs and extending this logic to datastar doesn't seem unreasonable. I would also argue that having openWhenHidden:false for POST requests is already a departure from the normal behaviour of the web platform. If you load a web page over a post request the browser won't reload the page without asking you whether you want to resubmit the data.

3. And for my last point: nobody today has said they were doing long lived POST/PUT/PATCH/DELETE requests, so changing the default shouldn't be a breaking change for too many people. But that is just hopeful guesswork at this point.
```

```
This does feel like a justified argument for CRUDdy apps. It means adding caveats to the docs, but is not a breaking change since it doesn’t “break” behaviour. Will discuss with the team.
```

```
I am personally trying to go down that route of applying d* in larger applications, not necessarily the game/single page (with /update endpoint) style. I guess is it important to realize that d* will be used in different contexts, and that some patterns apply for some contexts better than others.

Currently, I am trying to wrap my head around CQRS style + SSE while still in a MPA. Like should I open a long-lived query-side SSE on each page of my MPA, or should I just use that pattern for highly interactive pages while just returning fat html from direct requests for simpler pages, and so on...
```

```
you'll end up simplifying all routes if you go with this approach, like if you have any kind of updating on the page
```

```
I generally do a different page per logical page,  embrace MPA, As it's mostly going to reset your SSE brotli context anyway
```

```
like if you can assume every route has a single SSE connection it's a simpler mental model imo.

I think where i'm at:
- per-request morphing is a good place to start
- maybe res from request is good for initial morphing (loading/processing state)
- but as long as you can pub/sub or handle events easily having a single pipe/place the page is rendered is ideal
```

```
oh dang query params as cache is kind of like the send 0 or more events take to me.

// Old thinking: Query params ARE the state
GET /products?color=red&minPrice=20
// "Show me red products over $20"

// New thinking: Query params ARE a cache key
GET /products?color=red&minPrice=20
// "Give me the cached view for this filter combination"

where the cache may be warm or not
```

```
you can also never think about the /update endpoint by doing the sse conn outside your morph function, so it's always present
```

```
like if you can assume every route has a single SSE connection it's a simpler mental model imo.

I think where i'm at:
- per-request morphing is a good place to start
- maybe res from request is good for initial morphing (loading/processing state)
- but as long as you can pub/sub or handle events easily having a single pipe/place the page is rendered is ideal
```

```
I literally use query params for resources as I think path params are overcomplicated

if youtube doesn't need them I don't
```

```
yep, so query params are VERY much like forms in that they are half baked in my opinion

people dump state into them BECAUSE SPA is anti-hypermedia, change my mind
```

```
Path params are terrible for router performance. They make routing more complicated than it need to be. Without them your routing can be a simple map.

My radical view
```

```
Yes!  If the current view is really a stream of updates think query parameter to my opinion make stuff really messy. That's the kind of stuff that I can see mostly being in the cookie. It really depends on how much you're sharing and how much you're caching
```

```
When that day comes, I hope all those concepts will be long engraved into my brain and I will have asked plenty of other even dumbest questions on the discord.. 

So yes, no state in the URL at all. State only lives on a backend session/db, mapped either by a hashed URL parameter, or a cookie 🤔 . I think I start to see your world
```

```
Sorry I keep coming back here, but because things are moving in my head, and the picture is drawing itself slowly.

I thing I get the appeal of that URL=ressource. Datastar acts at the page/document/resource level. To identify a page/resource, you have the URL. This is where it beings. That is the entry of the maze. 

After that, hypermedia rules the world, so the frontend is guided by the backend for the upcoming interactions on that page. You still have a direct teleportation possible outside of the maze, if the server returns a link to another page (or if you use the address bar of your browser as a cheat code). But otherwise, and with datastar, new full frames are patched at each of your actions, still moving inside that resource.

Say you hit f5 now. You are back at the entrypoint of the maze. This is the "restart level" of the game. And there are two kinds of games. 

The first one has no memory. It is stateless. It means your backend does not have a way to persist data. No database. So if you start over, you do your new path again from scratch.

However, there is a second kind of game. If the backend has a database, it means your gameboy has memory. You can restart/hit f5, and you exactly land, where you were before. But if a friend of yours takes your gameboy, or loads the same URL/resource in its browser, he is going to land exactly at your save point. Say it is a shared memory, shared state.

To have multiple players having their own save/state, the backend needs identification. And we are lucky, because there is this small database that is on the client side, and which is called the cookie store. So the backend can decide to store things here, on each player's database. Usually, it will be a player id so that the backend will be able to spawn the player where he was before on f5, and this point can be different than the other player.
```

```
So the elephant in the room is the word "state". I think it is hard to define. But with this game analogy, we can just say it is a checkpoint in the game for a particular resource URL.

But I think "state" is not something concrete. It represent the particular condition that someone or something is in at a specific time. And usually, you want to "restore state". So directly come back at a specific place and time instead of having to go through the whole game again. And to restore state, you need data.

In the web, people usually agree about data living either in cookies/local storage on the client side, or in a kind of database on the backend.

But the struggle is about URL and data. And the practice that is being pushed here on the Discord is that data that is in a URL should be for resource identification, not for restoring some state. Your URL is just here so that the backend knows which game to load.

And when you don't have the full story, it becomes hard to recognize a good URL which targets a resource vs data in the URL that would serve for restoring state.

/product/12 -> good, as we identify the product number 12
/products?color=red -> not good, as you are refering to the `products` resource, and your intent is to "load" the ones that have the color red.

You could though have /products/red which is a game where all products are red. Why not. But this is a different intent. You cannot then see blue product in that game.
```

```
And so I understand why Delaney does not like query params. Because they are not part of this story. It is hard to give them a good meaning in that way of seeing things.

So i still do not really understand why we would say they are for caching at the proxy level, but I think it is more about trying to give them purpose, as they exist in end. But they are not interesting as part of our story. And with them, the mistake of putting data that serves "state restoration" is easy to make.
```

```
I guess just for my experience query parameters end up being a dumping ground for things instead of a well thought out interface. In the name should tell you something, the query params are more for creating apis. Hypermedia is not an API, it has no versions
```

```
Okay, so working my first non-trivial D* page for a production app. Got the basic stuff working and I am now thinking about doing the thing where you leave the sse connection open to push updates to the client as changes to the resource are made elsewhere. Which I also grok.... but am not sure how to handle updates to the app while connections are open. My current legacy app is using a blue/green setup behind a reverse proxy so when I make an update to the app, I take down the non-active one, upgrade it, bring it back up, then toggle the proxy so new requests go to the new version, and the old version finishes any active work before shutting down.... But even assuming i wasn't doing this blue/green thing and just restarted the app, any long lived connections would just die, right?
```

```
they'd auto reconnect

You have to make sure your server doesn't cleanly end the connections though when you restart

You can end connection cleanly, just need to send some sort of event or element patch to client so they would reconnect. 
I am sending event graceful-shutdown on window and my long lived listeners restart on it.
```

```
any long-lived SSE connection will drop the moment that app instance goes down, whether you’re doing blue/green or a simple restart. 
the usual approach is to just let the client auto reconnect and reload whatever state it needs, since SSE streams are meant to be disposable anyway. 
as long as your endpoint is safe to reconnect to and your client handles retries cleanly, deployments won’t cause any real issues beyond that quick reconnect.
```

```
You don't want push to poll over the network because it kills your comprehension and latency

its the same thing you push an event to the browser anf it goes to the server to get the data
```

- Server push: server push updates to clients without waiting
- Client pull: client decides whether it want updates or not

```
3 times as many trips.  Push is a single trip down. Push pull is down, up, down.

Push everything goes down a compressed stream and you get compounding compression for the duration of the connection over N events/messages.

Push pull you get separate compression per message so can be at least two orders of magnitude worse compression. It's also way more CPU intensive.

Push pull makes clients stamped the server.
```

- https://data-star.dev/examples/progressive_load