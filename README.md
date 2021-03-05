# Chicken Story

**tl;dr**: Crowdsourced cheating at Microsoft's Club Bing game to get prizes.

(A lot of the details are from memory so I've recreated images and information as necessary.)

# About the game

[Club Bing](https://en.wikipedia.org/wiki/Club_Bing) is a set of games that ran from 2007-2012.  The games were all word games that you could play online to win points and those points could be used at the online prize store to buy prizes.  One of the games was called Chicktionary.  The goal was to use 7 letters to make as many words as possible.

![image](https://user-images.githubusercontent.com/109809/110149959-e62c5500-7d9b-11eb-924e-93d576ac3f7d.png)

The letter that you can use are on the bottom and the words that you need to make are in the little eggs at the top.  There was always one 7 letter word.

Back in the early days of it I'm told that it could be a huge revenue source to play.  Though they only allowed you to get one prize per address, it was easy enough to slap an apartment number on to the address of your single-family home and create lots of unique addresses.  Apparently the XBox controller had the best dollars/point so you could leave your computer running software to play the game nonstop.  I saw an old blog post about a guy that had nearly 100 Xbox controllers delivered to his house in a single day, which he promptly put on Ebay and sold.  Other prizes include telescopes, record players, Xboxes, Michael Kors wristwatch, North Face clothing, etc.  Everything said "Bing" on it.

Micrsoft ran the game to popularize their search engine, (Bing)[bing.com].  Everytime that you typed in an answer, your browser would search for it in another frame.  This perhaps convinces people to use Bing more but it also increases the number of users that appear to be using Bing, which means that Microsoft can demand more money from advertisers that want to appear on Bing.  I worked out that all the scripters playing Chicktionary were contributing to about 2% of all Bing searches.  I also did some envelope-math comparing Google's revenue and search numbers with that of Bing and the inflated search numbers on Bing surely led to more ad revenue then the cost of the prizes that they sent out.

# Scripting

There were a few scripts around to play the game automatically, often using [AutoHotKey](https://www.autohotkey.com/).  I wrote my own in VB.Net that had an embedded browser, which I called "Chicken" after Chicktionary and also because there was a pop-culture joke about Kuritza in my country.

![image](https://user-images.githubusercontent.com/109809/110156497-445d3600-7da4-11eb-8442-9d67dabc1d18.png)

Because the game was in Flash, it wasn't trivial to interact with the elements in the DOM so playing the game was a combination of DOM interactions, Go(<URL>), screenshots, and Windows API to simulate typing and clicks.

Microsoft isn't a bunch of dummies and they knew about cheaters.  They got better at tracking users that would complete puzzles too quickly and they would void their prizes.  They also got better at recognizing duplicate shipping address.  And of course, they used captchas.

## Captchas

You know, those squiggly letters that you have to type in to prove that you're human:

![image](https://user-images.githubusercontent.com/109809/110151548-da419280-7d9d-11eb-999e-fc2f0315f88e.png)

You'd think that this would be a deal-breaker for automation but it really isn't.  There are a dozen online captcha solving services.  They cost about $1 for 500 solved puzzles.  Club Bing popped up a captcha once every 4 games.  Each game earned you 20 tickets if you got all the words right and an Xbox was about 80,000 tickets, I think, so:

```
(1 Xbox / 80000tickets) * (20 tickets / game) * (4 games / captcha) * (500 captchas / 1USD) = 1 Xbox for 50 cents
```

Pretty good deal.  Also, it would take you 80 days because you could only earn 1000 tickets per day but you could run a few different accounts so at the end of 80 days you'd pick up a few Xboxs.

Also, the captcha solver this explains why scripting was so popular.  Those services that solve captchas have affiliate programs.  The script that does the solving sends an affiliate code along with the request and the the affiliate gets a bit of the money.  So script writers were incentivized to share the script far and wide and write the best one.

# Cat-captcha

Around 2010 Microsoft switched the captcha algorithm from squiggly letters to [Asirra](https://www.microsoft.com/en-us/research/wp-content/uploads/2007/10/CCS2007.pdf).  Asirra looks like this:

![image](https://user-images.githubusercontent.com/109809/110153581-7b314d00-7da0-11eb-929a-83f463931a92.png)

Each of those images is a thumbnail of a cat or a dog.  To solve the puzzle, you need to get 11 out of 12 correct identifications of cats.

When Club Bing switched to this, the entire cheating community around Club Bing crashed.  I got to work.

The first thing that I tried was sending cats and dogs to the captcha service.  Back in 2010 those captcha services were *not* some highly advanced image recognition.  They were just people in Bangladesh answering your queries.  I tried to work out how much they earned:

```
(2000 work hours / year) * (1 captcha / 5 seconds) * (1USD / 500 captchas) = $2880 / year working full-time.
```

Maybe half went to the owner of the website because, you know, capitalism, so the workers were probably earning about as much as a receptionist according to [some randomly selected website](https://destinationscanner.com/average-salary-in-bangladesh/).

I wanted to see if they could solve Asirra.  Here's the image that I sent:

![image](https://user-images.githubusercontent.com/109809/110156903-c51c3200-7da4-11eb-89b0-4212df87e258.png)

The service that I used, [de-captcher](https://de-captcher.com/), returned the "correct" answer:

```
cat or dog?
```

Hmm.  Not perfect.  I sent it a few more times and after 4 tries I eventually got the right answer:

```
dog
```

This did not bode well for me.  First of all, I need 12 of them and 11 needed to be correct.  Assuming that it would take me 4 tries each time to find a worker in Bangladesh to do it correctly, that would be 44 requests.  The cost of an Xbox just went up to $22!  Obscene!  I needed a better solution.

# Why not just use deep learning?

This was 2010, remember?  Deep learning was not as far along back then.  [This paper from Stanford](https://crypto.stanford.edu/~pgolle/papers/dogcat.pdf) shows that they were able to use machine learning to get puzzles right about ~10% of the time.  That's not great!  There was also a [token-bucket](https://en.wikipedia.org/wiki/Token_bucket) scheme that would lock you out temporarily for getting too many wrong in a row on Club Bing.  Though the token-bucket didn't run on the test server, it *did* run on Club Bing.

# The harvest

Microsoft research put up a website to show off the new Asirra technology.  It had a testing ground where you could try it out and it would let you know if you got it right.  Look at the image again:

![image](https://user-images.githubusercontent.com/109809/110153581-7b314d00-7da0-11eb-929a-83f463931a92.png)

See that little "Adopt me" button?  That's there because Asirra was a partnership with [petfinder.com](https://www.petfinder.com/).  Petfinder is a pet adoption service with many listings.  When you clicked on the "Adopt me" button, it would take you to that pet's profile.  The profile of course included the species: cat or dog.

Again, Microsoft is not a bunch of dummies.  They know that you're going to try to click adopt me on each image and get the right answer.  What they do is invalidate the puzzle after the first time that you click adopt me.  So you only get one answer.  My idea was to write a program to collect all the info and make a mapping from image to number: 0 means unknown, 1 means dog, 2 means cat.  Not too difficult.

The time to learn a pet's species was pretty quick but I didn't know how many pets I needed to learn.  The Asirra website claimed 3.1 million.  Really?

# Inverse birthday paradox

Most people know the [birthday paradox](https://en.wikipedia.org/wiki/Birthday_problem):  Despite there being a full 365 days in a year, you only need 22 people in a room to have a 50-50 chance that two of them have the same birthday.  If `d=365` and `n=22` then you can work out the probability like this:

![image](https://user-images.githubusercontent.com/109809/110160217-f565cf80-7da8-11eb-8b75-47ecd2a51c89.png)

The inverse is that if you know that 22 people in a room gives you a 50-50 shot at finding two people with the same birthday, you can reverse the equation to compute how many days there are in a year.

Likewise, if I query the Asirra servers and keep track of every image seen, how long until I get a duplicate?  I can do that, see how many images until I get a duplicate, and then do it again and again, many times.  Then I take the median of all those trials and run it through the equation above, in reverse, to figure out the number of images.  Sure enough, my answer was pretty much 3.1 million.

# Distributed harvest

I put my script on USB thumb drives and handed them out to friends.  I also wrote a merge program that would combine the databases.  Every day or two my friends would hand back their USB thumbdrives and I would merge all the databases and put them on all the thumbdrives so that the harvesters wouldn't be duplicating efforts.  The harvesters only clicked "Adopt me" on unknown images so we didn't have too much duplication and we were making good progress.

# Can we go faster?

After 2-3 weeks, we had collected around 1.5 million images.  It was getting to where the puzzle was sometimes nearly solved out of the database.  However, there were some holes in the database that would never fill because the "Adopt me" link was broken.  Maybe the pet was already adopted or delisted for some other reason?

But there was another way to get a right answer: Guess.  Asirra would let you know if you solved a puzzle correctly.  Here's what I measured:

* `adopt_time`: How long it takes to click on an "Adopt me" link, load petfinder.com, and get the answer.
* `adopt_success_rate`: Probability that clicking "Adopt me" gets me the answer.
* `guess_time`: How long it takes to submit a guess and learn if I solved the puzzle correctly.

Assuming 50-50 cats-to-dogs (it was more like 40-60 but whatever), I could work out an equation for how many pets I'm learning per second using adopt me:

```
adopt_learning_rate = 1 / adopt_time * adopt_success_rate
```

I could also work out the learning rate for guessing.  If there are `n` unknown pets then my odds of guess right are 1 in 2<sup>n</sup>.  And when I get it right, I learn all `n` of them.:

```
guess_learning_rate = n / guess_time * (1 / 2**n)
```

Setting those two to equal and solving for n, I was able to calculate that if I knew 7 or more out of the 12 pets, I could just guess the rest of them and it would be faster than trying to click on adopt.  I put this code into the harvester and a couple week later my friends and I had a database that was complete enough to work.

# Solution server

Microsoft Research did a good job but they made a couple mistakes.  First of all, they never rate-limited their service.  This is what let the harvester work so well.  Another mistake that they made was in how they handed out correct solutions.

There are three parties in the captcha process:

1. The captcha provider (Microsoft Asirra or Google reCaptcha)
2. The captcha server (Club Bing or whoever else needs it)
3. The captcha user (Whoever is playing Club Bing games)

One way you *could* make it work is for the server to ask the provider for a puzzle and an answer.  Then the server sends the puzzle to the user, the user solves it, sends it back, and the server confirms it.

![image](https://user-images.githubusercontent.com/109809/110165143-b6874800-7daf-11eb-9281-bb4c07f049d6.png)

This is a bad idea.  Now it's up to your server to do all the processing.  And if you want to change how things work, every server using the provider will need to update their website.  And now the server can be the most efficient harvester ever.

Here's how it actually worked (Asirra in the middle this time, for easier reading):

![image](https://user-images.githubusercontent.com/109809/110165783-a58b0680-7db0-11eb-945b-24a8c9afe209.png)

Now the server doesn't need to know the details about how it works, nor does the server even have the answer.  But here's where Microsoft made a mistake:
* There was a rate-limit on the Club Bing so you couldn't get too many wrong in a row but there was no rate limit on Asirra.
* There was no check on the IP address of the token.

So it was easy for me to create the cats-be-gone.kicks-ass.org website which served up valid tokens.  Like this:

![image](https://user-images.githubusercontent.com/109809/110167286-c8b6b580-7db2-11eb-83d4-fdc02b1dc39e.png)

Though the token IP addresses were not checked, their timestamp was.  Tokens that were more than an hour old were invalidated, probably in part to keep Microsoft's servers from having to hold them around forever.  The Cats Be Gone server actually generated them a head of time and always kept 20 on hand so that they'd be ready to go as needed.

# Making it a business (lifetime revenue: $0)

Talking with my friends I thought, "Hey, let's open the server to everyone and make a business out of it!"  People were already used to paying captcha for the service so I figured they could pay me instead.  I'd charge $1 per 200 solutions, which is double the going rate of $1/500 but then again, I had no competition.  I publicized the script on [one of the most popular forums](https://thebot.net/threads/club-bing-bot-chicken-beta-with-automatic-cat-captcha.15723/page-5) for this kind of stuff and opened a Google Store to accept payments.  Pretty cringey looking back on it.

There was plenty of chatter on the forums about how this is some by-pass and not solver and so the tickets earned would get invalidated when it came time to buy a prize.  That was something that had happenned in the past.  People were rightly suspicious.  But with no alternative and such a cheap price, I got some customers anyway and eventually had like $50 in potential sales.  *Wow, I'm rich!*  Yeah right, even the Bangladeshis were getting a better return on their time.

I shortly after cancelled all the orders because Microsoft defenses finally defeated Cats-Be-Gone.

# The Microsoft empire strikes back

Microsoft tried a few things to defeat my cheating all along.  One of the first things that they tried was renaming all their images.  *It was a total disaster and I had to start all over because I only ever mapped from filename to cat/dog!*

Nah, just kidding.  I had already downloaded all the images.  I mean, 3.1 million images at 1MB each, it was *only* 3.1 Terabytes.  Even back then 3 Terabytes was affordable.  It didn't matter at all.  I figured that they might try something so I ran a downloading harvester.

Another thing that they tried was tweaking the images.  They would randomly select 10-20 pixels in the image and adjust the color, which was more than enough to break any cryptographic hash that I might have used to store a mapping from `SHA1(image) -> cat/dog`.  But I didn't use that either.  I used [MinHash](https://en.wikipedia.org/wiki/MinHash).

# Image Hashing v1: MinHash

MinHash is super-simple: Pick a ten pixels out of the image and concatenate their values.  And that's it.  So long as you always pick the same ten pixels, it'll work.

If Microsoft modifies a couple pixels here and there, no big deal.  What are the odds that we collide?  And even if we do, it'll probably be just 1 of the 12 images so I can send a guess for that image.  Worst case, try again.

It worked fine.  I also had the server update itself whenever it got a guess right so the database was filling itself in over time.

# Microsoft defeats Cats Be Gone

Microsoft eventually rate limited on Asirra so it was no longer possible for a single Cats-Be-Gone server to create token.  And they started to associated tokens with IP addresses so the Cats-Be-Gone server was pointless.  And most of all, they wiped out the 3.1 million images from petfinder.com and got a brand-new batch.

I couldn't harvest them because of rate-limiting and I couldn't sell them because of the IP address check so I gave up entirely on making a measely business out of it.  But I still felt some obligation to the clients and I did want to win some prizes still so I turned to crowd-sourcing.

# Crowdsourcing

I knew that some of the users would be willing to answer captchas themselves so I adjusted the client to ask the server for answers, get them, and then ask the user to fill in any unknowns.  The client would then send the results back to the server.

To make it somewhat difficult for a malicious user to fill my database with junk, I encrypted all communications with a hard-coded key and I ran a .Net obfuscator on the releases to make it harder to find.  It would only prevent casual users from wrecking the database but it was good enough.  The only people that did figure out how to access the database through reverse engineering were those who wanted to download the whole thing.  And I decided that I don't care so I let it happen.

Also, all the hashing was in the client code now and I knew that minhash wasn't robust so I switched to pHash.

# pHash

[pHash](https://www.phash.org/) is great.  The idea is like this:

1. Convert the image to black and white.
2. Gaussian blur.
3. Shrink to a uniform square shape.
4. Perform a discrete cosine transform on it.
5. Discard all but the 64 most significant values.
6. For each value, record a `1` is it's above the median, otherwise a `0`.
7. Now you have a 64-bit hash.

pHash has a library for this and it's, of course, not in Visual Basic .Net so I implemented it myself, cutting corners where possible because I didn't need it to be very perfect.

# Convert to black and white

Pretty easy, just convert the RGB value of each pixel to intensity.  There are a few ways but this one is on Wikipedia:

```
Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
```

Here's the result for a koala:

