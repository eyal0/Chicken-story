# Chicken Story

**tl;dr**: Crowdsourced cheating at Microsoft's Club Bing game to get prizes.

(A lot of the details are from memory so I've recreated images and information where possible.)

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

Microsoft isn't a bunch of dummies and they knew about cheaters.  They got better at tracking users that would complete puzzles too quickly and they would void their point balance.  They also got better at recognizing duplicate address.  And of course, they used captchas.

## Captchas

You know, those squiggly letters that you have to type in to prove that you're human:

![image](https://user-images.githubusercontent.com/109809/110151548-da419280-7d9d-11eb-999e-fc2f0315f88e.png)

You'd think that this would be a deal-breaker for automation but it really isn't.  There are a dozen online captcha solving services.  They cost about $1 for 500 solved puzzles.  Club Bing popped up a captcha once every 4 games.  Each game earned you 20 tickets if you got all the words right and an Xbox was about 80,000 tickets, I think, so:

```
(1 Xbox / 80000tickets) * (20 tickets / game) * (4 games / captcha) * (500 captchas / 1USD) = 1 Xbox for 50 cents
```

Pretty good deal.  Also, it would take you 80 days because you could only earn 1000 tickets per day but you could run a few different accounts so at the end of 80 days you'd pick up a few Xboxs.

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

# The harvest

Microsoft research put up a website to show off the new Asirra technology.  It had a testing ground where you could try it out and it would let you know if you got it right.  Look at the image again:

![image](https://user-images.githubusercontent.com/109809/110153581-7b314d00-7da0-11eb-929a-83f463931a92.png)

See that little "adopt me" button?  
