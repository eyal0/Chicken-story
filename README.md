# Chicken Story

**tl;dr**: Crowdsourced cheating at Microsoft's Club Bing game to get prizes.

(A lot of the details are from memory so I've recreated images and information as necessary.)

# About the game

[Club Bing](https://en.wikipedia.org/wiki/Club_Bing) is a set of games that ran from 2007-2012.  The games were all word games that you could play online to win points and those points could be used at the online prize store to buy prizes.  One of the games was called Chicktionary.  The goal was to use 7 letters to make as many words as possible.

![image](https://user-images.githubusercontent.com/109809/110149959-e62c5500-7d9b-11eb-924e-93d576ac3f7d.png)

The letter that you can use are on the bottom and the words that you need to make are in the little eggs at the top.  There was always one 7 letter word.

Back in the early days of it you could get a lot of prizes.  Though they only allowed you to get one prize per address, it was easy enough to slap an apartment number on to the address of your single-family home and create lots of unique addresses:

* 123 Main St. Apt #1, Anywhere, YZ, USA
* 123 Main St. Apt #2, Anywhere, YZ, USA
* 123 Main St. Apt #3, Anywhere, YZ, USA

Apparently the XBox controller had the best dollars/point so you would leave your computer running to gather points on multiple accounts, then use all the points to buy up controllers.  There was a post on a forum with a photo of a guy that received like 100 Xbox controllers by UPS in a single day.  He promptly put them on Ebay and sold them.  Other [prizes](https://www.cheapassgamer.com/topic/164690-live-se-club-bing-thread-3-no-macrobotreturn-fraud-talk/) included:

* Telescope
* Record player
* Xbox
* Michael Kors wristwatch
* North Face clothing
* Inflatable Kayak
 
Everything said "Bing" on it.

Micrsoft ran the game to popularize their search engine, [Bing](bing.com).  Everytime that you typed in an answer, your browser would search for it in another frame.  This perhaps convinces people to use Bing more but it also increases the number of users that appear to be using Bing.  And that number helps Microsoft demand more money from advertisers that want to appear on Bing search results.  I worked out that all the scripters playing Chicktionary were contributing 2-4% of all Bing searches.  I also did some back-of-the-envelope math comparing Google's revenue and searches/month with that of Bing and figured out that Microsoft was getting a pretty good return on the game.  The appearance of [Bing being more popular](https://en.wikipedia.org/wiki/Club_Bing#Bing) probably brought in more ad dollars than the prizes cost.

# Scripting

There were a few scripts around to play the game automatically, often using [AutoHotKey](https://www.autohotkey.com/).  I wrote my own in VB.Net that had an embedded browser, which I called "Chicken" after Chicktionary and also because there was a funny TV sketch about Kuritza in my country.

![image](https://user-images.githubusercontent.com/109809/110156497-445d3600-7da4-11eb-8442-9d67dabc1d18.png)

Because the game was in Flash, it wasn't easy to interact with the elements in the DOM so playing the game was a combination of:

* DOM interactions
* `browser.Go(<URL>)`
* screenshots and searching pixels
* Windows API to simulate typing and clicks

**Microsoft isn't a bunch of dummies.**  They knew about cheaters.  They got good at tracking users that would complete puzzles too quickly and they would void their prizes.  They also got better at recognizing duplicate shipping address.  And of course, they used **captchas**.

## Captchas

You know, those squiggly letters that you have to type in to prove that you're human:

![image](https://user-images.githubusercontent.com/109809/110151548-da419280-7d9d-11eb-999e-fc2f0315f88e.png)

You'd think that this would be a deal-breaker for automation but it isn't.  There are a dozen [online captcha solving services](https://prowebscraper.com/blog/top-10-captcha-solving-services-compared/).  They cost about [$1 for 500 solved](https://de-captcher.com/) puzzles.  Club Bing popped up a captcha once every 4 games.  Each game earned you 20 tickets if you got all the words right and an Xbox was 55,000 tickets.

```
(1 Xbox / 55000tickets) * (20 tickets / game) * (4 games / captcha) * (500 captchas / 1USD) = 1 Xbox for 73 cents
```

Pretty good deal.  Also, it would take you 55 days because you could only earn 1000 tickets per day.  But you could run a few different accounts so at the end of 55 days you'd pick up a few Xboxs.  Cheaper prizes even faster: A video game was 5000 tickets.

The captcha solving service explains why cheating was so popular:  Those services have affiliate programs.  The script that does the solving sends an affiliate code along with the request and the the affiliate gets a bit of the money that the user is paying.  So script writers were incentivized to share the script far and wide and write the very best one.

# Cat-captcha

Around 2010 Microsoft switched the captcha algorithm from squiggly letters to [Asirra](https://www.microsoft.com/en-us/research/wp-content/uploads/2007/10/CCS2007.pdf).  Asirra looks like this:

![image](https://user-images.githubusercontent.com/109809/110153581-7b314d00-7da0-11eb-929a-83f463931a92.png)

Each of those images is a thumbnail of a cat or a dog.  To solve the puzzle, you need to get 12 out of 12 correct identifications of cats, or 11 out of 12 twice in a row.

When Club Bing switched to this, the entire cheating community around Club Bing halted.  I went to work.

The first thing that I tried was sending cats and dogs to the captcha service.  Back in 2010, those captcha services were *not* some highly advanced image recognition.  They were just [people in Bangladesh answering your queries](https://www.nytimes.com/2010/04/26/technology/26captcha.html).  I tried to work out how much they earned:

```
(2000 work hours / year) * (1 captcha / 5 seconds) * (1USD / 500 captchas) = $2880 / year working full-time.
```

Maybe half went to the owner of the website because, you know, _capitalism_, so the workers were probably earning about as much as a receptionist according to [some randomly selected website](https://destinationscanner.com/average-salary-in-bangladesh/).

I wanted to see if they could solve Asirra.  Here's the image that I sent:

![image](https://user-images.githubusercontent.com/109809/110156903-c51c3200-7da4-11eb-89b0-4212df87e258.png)

The service that I used, [de-captcher](https://de-captcher.com/), returned this answer:

```
cat or dog?
```

*Technically* correct but not what I wanted.  I sent it a few more times:

![image](https://user-images.githubusercontent.com/109809/110195805-37206580-7dfd-11eb-9579-2f1fdd4f541f.png)![image](https://user-images.githubusercontent.com/109809/110195815-3e477380-7dfd-11eb-8009-b49ad9b5b708.png)![image](https://user-images.githubusercontent.com/109809/110195820-43a4be00-7dfd-11eb-9bf9-f1585e5dddae.png)![image](https://user-images.githubusercontent.com/109809/110195828-4b646280-7dfd-11eb-8d41-0f3c80bb1832.png)

It took four tries to get a useful answer:

```
dog
```

This did not bode well for me.  First of all, I need 12 of them.  Assuming that it would take me 4 tries each time to find a worker in Bangladesh to do it correctly, that would be 48 requests.  The cost of an Xbox just went up to $35!  And if they get even 1 wrong I have to double that.  Obscene!  I needed a better solution.

# Why not just use deep learning?

This was 2010, remember?  Deep learning was not as far along back then.  [This paper from Stanford](https://crypto.stanford.edu/~pgolle/papers/dogcat.pdf) shows that they were able to use machine learning to get puzzles right about ~10% of the time.  That's not great!  (Mostly they were just noticing the color green because dogs are more likely to be on a lawn than cats.)

There was also a [token-bucket](https://en.wikipedia.org/wiki/Token_bucket) scheme that would lock you out temporarily for getting too many wrong in a row.  Though the token-bucket didn't run on the Asirra test server, it *did* run on Club Bing.

# The Harvest: A new hope

Microsoft research put up a website to show off the new Asirra technology.  It had a testing ground where you could try it out and it would let you know if you got it right.  Look at the image again:

![image](https://user-images.githubusercontent.com/109809/110153581-7b314d00-7da0-11eb-929a-83f463931a92.png)

See that little "Adopt me" button?  That's there because Asirra was a partnership with [petfinder.com](https://www.petfinder.com/).  Petfinder is a pet adoption service with many listings.  When you clicked on the "Adopt me" button, it would take you to that pet's profile.  The profile of course included the species: cat or dog.

Again, **Microsoft is not a bunch of dummies**.  They know that you're going to try to click `Adopt me` on each image and get the right answer.  So what they do is invalidate the puzzle **and** all the adoption links after the first time that you click adopt me.  So you only get one answer.

My idea was to write a program to do it a lot and gather a mapping from image to number: 0 means unknown, 1 means dog, 2 means cat.  I called it the "Harvest" in keeping with the chicken/farmer theme.

Each attempt went pretty quickly but I didn't know how many pets I needed to learn.  The Asirra website claimed 3.1 million.  Was it really 3.1 million?

# Inverse birthday paradox

Most people know the [birthday paradox](https://en.wikipedia.org/wiki/Birthday_problem):  Despite there being a full 365 days in a year, you only need 22 people in a room to have a 50-50 chance that two of them have the same birthday.  If `d=365` and `n=22` then you can work out the probability like this:

![image](https://user-images.githubusercontent.com/109809/110160217-f565cf80-7da8-11eb-8b75-47ecd2a51c89.png)

The inverse is that if you know that 22 people in a room gives you a 50-50 shot at finding two people with the same birthday, you can reverse the equation to compute how many days there are in a year.

Likewise, if I query the Asirra servers and keep track of every image seen, how long until I get a duplicate?  I did an experiment:

```
define trial as:
   initialize images_seen to an empty list
   while images_seen has no duplicates:
       fetch a puzzle
       add all images in the puzzle to images_seen
   return the size of images_seen
```

For each trial, I requested puzzles until I got a duplicate cat or dog in the trial.  I ran many trials and kept track of how many images until the first duplicate.  Then I took the median of all those trials which told me about how many pets need to be seen to have a 50-50 change of a duplicate.  Then I ran it through the equation above, in reverse, to figure out the number of images.  Sure enough, my answer was pretty much 3.1 million.

# Distributed harvest

I put my script on USB thumb drives and handed them out to friends.  I also wrote a merge program that would combine the databases.  Every day or two my friends would hand back their USB thumbdrives and I would merge all the databases and put them back on all the thumbdrives so that the harvesters wouldn't be duplicating efforts.  The harvesters only clicked "Adopt me" on unknown images so keeping the distributed databases current prevented duplicated work.

# Can we go faster?

After 2-3 weeks, we had collected around 1.5 million images.  It was getting to where the puzzle was sometimes nearly solved out of the database.  However, there were some holes in the database that would never fill because the "Adopt me" link was broken.  Maybe the pet was already adopted?  I added another result to the database:

* Unknown
* Cat
* Dog
* Broken link

But there was another way to get a right answer: Guess!

Asirra would let you know if you solved a puzzle correctly.  Here's what I measured:

* `adopt_time`: How long it takes to click on an "Adopt me" link, load petfinder.com, and get the cat/dog answer.
* `adopt_success_rate`: Probability that clicking "Adopt me" gets me the answer and not just a broken link.
* `guess_time`: How long it takes to submit a guess and learn if I solved the puzzle correctly.  (This was faster than petfinder.com loading times.)

Assuming 50-50 cats-to-dogs (it was more like 40-60 but whatever), I could work out an equation for how many pets I'm learning per second using `adopt me`:

```
adopt_learning_rate = 1 / adopt_time * adopt_success_rate
```

I could also work out the learning rate for guessing.  If there are `n` unknown pets then my odds of guessing right are 1 in 2<sup>n</sup>.  But when I get it right, I learn all `n` of them:

```
guess_learning_rate = n / guess_time * (1 / 2**n)
```

Setting those two to equal and solving for n, I was able to calculate that if I knew more than 7 of the 12 pets, I could just guess the rest of them and it would be more effective than `adopt me`.  I put this into the harvester and a couple weeks later my friends and I had a database that was complete enough to work.

# Cats Be Gone: A Solution Server

Microsoft Research did a good job but they made a couple protocol mistakes.  First of all, they never rate-limited their service.  This is what made the harvester possible.  Second, they didn't handle proofs-of-work correctly.

There are three parties in the captcha process:

1. The captcha provider (eg, Microsoft Asirra or Google reCaptcha)
2. The captcha server (eg, Club Bing or whatever web server)
3. The captcha user (eg, Club Bing players)

One way you *could* make it work is for the server to ask the provider for a puzzle and an answer.  Then the server sends the puzzle to the user, the user solves it, sends it back, and the server confirms it.

![image](https://user-images.githubusercontent.com/109809/110165143-b6874800-7daf-11eb-9281-bb4c07f049d6.png)

This is a bad idea for a few reasons:
1. Now it's up to your server to do all the processing.  What if the server screws it up?
2. If Asirra ever wants to change the protocol, every server will need to update their website.
3. A pretend server could become the most efficient harvester ever.

Here's how it actually worked (Asirra in the middle this time for easier reading):

![image](https://user-images.githubusercontent.com/109809/110165783-a58b0680-7db0-11eb-945b-24a8c9afe209.png)

Now the server doesn't need to know the details about how it works.  The server doesn't even have the answer!  But here's where Microsoft made a mistake:
* There was a rate-limit on Club Bing so you couldn't get too many wrong in a row but there was no rate limit on Asirra.
* There was no check on the IP address of the token.

So it was easy for me to create the cats-be-gone.kicks-ass.org website which served up valid tokens over HTTP.  Like this:

![image](https://user-images.githubusercontent.com/109809/110167286-c8b6b580-7db2-11eb-83d4-fdc02b1dc39e.png)

(Though the token IP addresses were not checked, their timestamp was.  Tokens were only valid for an hour.  The Cats Be Gone server actually generated them ahead of time and always kept 20 on hand so that they'd be ready to go as needed.)

My friends and I used the server for a while with success and it got better over time as the server's guesses netted new answers.

# Making it a business (lifetime revenue: $0)

Talking with my friends I thought, "Hey, let's open the server to everyone and make a business out of it!"  People were already used to paying captcha for the service so I figured they could pay me instead.  I'd charge $1 per 200 solutions, which was more than the going rate of $1/500 but I had no competition.  I publicized the client on [one of the most popular forums](https://thebot.net/threads/club-bing-bot-chicken-beta-with-automatic-cat-captcha.15723/page-5) for this kind of stuff and opened a Google Store to accept payments.  Pretty cringy looking back on it!

There was plenty of chatter on the forums about how this is some by-pass and not solver and so the tickets earned would get invalidated when it came time to buy a prize.  In the past there had been problems with captcha by-passers.  People were rightly suspicious.  So I gave it away free for a while.  And after it started to prove itself and with no alternatives, I got some customers and had $50 in potential sales.  *Oh wow I'm rich now!*  Yeah, right!  Even the Bangladeshis were getting a better return on their time.

I promised that I wouldn't process the charge until 10% of the payment was spent and I'd refund unhappy customers, to prove that it works.  But just a week later I cancelled all the orders because Microsoft defenses finally defeated the idea.

# The Microsoft empire strikes back

Microsoft tried a few things to defeat my cheating all along.  One of the first things that they tried was renaming all their images.  **This was a total disaster and I had to start all over because I only ever mapped from filename to cat/dog!**

Nah, **just kidding**.  I had already downloaded all the images.  I mean, 3.1 million images at 1MB each, it was *only* 3.1 Terabytes.  Even back then 3 Terabytes was affordable.  It didn't affect me at all.  I figured that they might try something like this so I ran a downloading harvester.

Another thing that they tried was tweaking the images.  They would randomly select 10-20 pixels in the image and adjust the color.  That would be more than enough to break any cryptographic hash that I might have used, like a map with `SHA1(image), -> cat/dog`.  But I didn't use that either.  I used [MinHash](https://en.wikipedia.org/wiki/MinHash).

# Image Hashing v1: MinHash

MinHash is super-simple: Pick a ten pixels out of the image and concatenate their values.  And that's it.  So long as you always pick the same ten pixels, it'll be consistent

![image](https://user-images.githubusercontent.com/109809/110188438-eb5bc500-7dd8-11eb-8bc2-099ffac9e5e1.png)

If Microsoft modified a couple pixels here and there, no big deal.  What are the odds that we collide?  And even if we do, it'll probably be just 1 of the 12 images so I can send a guess for that image.  Worst case, get a new puzzle and try again.

It worked fine.  I also had the server update itself whenever it got a guess right so the database was filling itself in over time.

# Microsoft defeats Cats Be Gone

Microsoft eventually rate limited Asirra so it was no longer possible for a single Cats-Be-Gone server to create tokens for everyone.  *And* they started to associate tokens with IP addresses so the Cats-Be-Gone server tokens were worthless for sale.  *And worst of all*, they wiped out the 3.1 million images from petfinder.com and got a brand-new batch.

I could no longer harvest them because of rate-limiting and I couldn't sell them because of the IP address check so I gave up entirely on making a measely business out of it.  I never processed any payments.  But I still felt some obligation to the clients and I _did_ want to win some prizes still so I turned to crowd-sourcing.

# Crowd-sourcing

I knew that some of the users would be willing to answer captchas themselves so I adjusted the client to ask the server for answers, get them, and then ask the user to fill in just the unknowns.  The client would then send the results back to the server to update the database.

To make it somewhat difficult for a malicious user to fill my database with junk, I encrypted all communications with a hard-coded key and I ran a .Net obfuscator on the releases to make it harder to find.  It would only prevent casual users from wrecking the database but it was good enough.  The only people that did figure out how to access the database through reverse engineering were those who wanted to download the whole database.  I decided that I don't care so I let it happen.

Also, because I didn't have the images, now all the hashing was in the client code now and I knew that MinHash wasn't robust so I switched to pHash.

# Image hash v2: pHash

[pHash](https://www.phash.org/) is great.  The idea is something like this:

1. Convert the image to black and white.
2. Gaussian blur.
3. Shrink to a uniform square size.
4. Perform a discrete cosine transform on it.
5. Discard all but the 64 most significant values.
6. For each value, record a `1` is it's above the median, otherwise a `0`.
7. Now you have a 64-bit number!

pHash has a library for this and it's, obviously, not in VB.Net so I implemented it myself.  Nowadays you'd just use a library but I'll go through how pHash works because it's pretty cool.

## Convert to black and white

Pretty easy, just convert the RGB value of each pixel to brightness.  There are a few ways but this one is on Wikipedia:

```
Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
```

Here's how you do it in python:

```
from PIL import Image
image = Image.open('dog.jpg')
image.show()
for x in range(image.size[0]):
    for y in range(image.size[1]):
        (r, g, b) = image.getpixel((x,y))
        brightness = 0.2126 * r + 0.7152 * r + 0.0722 * b
        new_pixel = tuple([int(brightness)] * 3)
        image.putpixel((x,y), new_pixel)
image.show()
```

![image](https://user-images.githubusercontent.com/109809/110178982-84ccac00-7dc4-11eb-88cf-1ab297ff0ed7.png)

Pretty simple.

## Gaussian Blur

You replace each pixel with a weighted sum of the pixels around it.  Here is a blur with radius of 8.

![image](https://user-images.githubusercontent.com/109809/110180447-06253e00-7dc7-11eb-9409-fa908cf967ec.png)

(I'll skip the shrink step because it's pretty boring and obvious.)

## Discrete-cosine transform

The [discrete-cosine transform](https://en.wikipedia.org/wiki/Discrete_cosine_transform) is kind of like the Fourier transform in that you can convert your series of numbers from one form to another and also invert it.  `inverse_dct(dct(image)) == image`  You don't have to know all all about frequency analysis.  Just know that you can take a matrix of numbers, like a black and white image, and convert it to another matrix of numbers.  And you can convert it back.

Unlike the Fourier transform, DCT is made from cosines instead of powers of e so all the results are real numbers and there are no imaginary numbers.  It is the technique that [JPEG](https://en.wikipedia.org/wiki/JPEG#Discrete_cosine_transform) uses to shrink your images.

[Here's some code](https://stackoverflow.com/a/60794544/4454) that I found online that does it in python.  I modified it a little.  Here's the important bit:

```python
im = rgb2gray(imread('dog.jpg'))   #read in the image to grayscale
imF = dct2(im)                     #DCT
fraction = 1
for y in range(len(im)):
    for x in range(len(im[y])):
        if x > len(im[y])//fraction or y > len(im)//fraction:
            im[y][x] = 0           # blacken pixels that aren't in the top left corner
            imF[y][x] = 0          # blacken pixels that aren't in the top left corner
im1 = idct2(imF)                   # inverse DCT
```

![image](https://user-images.githubusercontent.com/109809/110188634-a84e2180-7dd9-11eb-8c97-9c20995c0dd3.png)

We read in an image and perform a DCT on it.  Then we blacken some fraction of that original image and also the same fraction of the transformed image.  And then invert transform.  Here's what it looks like with nothing blackened:

![image](https://user-images.githubusercontent.com/109809/110188664-bef47880-7dd9-11eb-8755-a93c482d07bc.png)

No surprise there.  The DCT is invertible so it makes sense that the output is the same as the input.  It's a little strange the DCT image is just black; we'll get to that soon!

Let's see what happens when we throw away three-quarters of the image:

![image](https://user-images.githubusercontent.com/109809/110188731-fb27d900-7dd9-11eb-973f-a8e0c66014fc.png)

The DCT transformed image still looks pretty good despite losing three-quarters of the information.  Let's blacken even more.

![image](https://user-images.githubusercontent.com/109809/110190628-7345cd00-7de1-11eb-8d6f-544029ce30e8.png)

The original loses a lot of data but the DCT image is still looking reasonable!  That's the power of the DCT: All the important bits are in one corner and we can throw away the rest.

Now let's zoom in on the top left corner of the DCT image, the part that we didn't throw away.

![image](https://user-images.githubusercontent.com/109809/110190705-dd5e7200-7de1-11eb-98d2-7af2d3bc28f3.png)

That's just the top-left of the DCT image.  We can see that all the significant bits were in the corner.  That's why the DCT worked even though we threw away so many bits: We threw away the bits that don't matter.  It only works well on photos but that's what we want to deal with anyway.

To encode this into a number we use the method that I mentioned before: Looking at just the top-left 64 numbers, encode a `1` if the value is above the median, otherwise `0`.  The result is a 64-bit number with half `0`s.  There are (64 choose 32) such numbers, more than 10<sup>18</sup> and **way** more than the 3.1 million images that we want to encode so we're unlikely to have a collision.

Now we just need an efficient way to store all those numbers for searching.

## Vantage Point Trees

A [vantage point tree](https://fribbels.github.io/vptree/writeup) is a sort of binary tree that works like this: For each node, you specify a center and a radius.  If the point that you're looking for is inside the radius, go left.  If it's outside, go right.  Continue until you find your answer.

![image](https://user-images.githubusercontent.com/109809/110194917-68e2fd80-7df8-11eb-989d-19d36861826a.png)

The advantage of this tree is that you can define distance anyway you like.  For our image hash, we want to weigh all the bits evenly so we use a [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance).  A hamming distance is the count of how many bits are different between two numbers.

```
                  01101010111001
                  10100010010010
difference bits:  ^^  ^   ^ ^ ^^
Hamming distance is 7
```

The hash works pretty well with the Hamming distance because it turns out that if two images are nearly the same but don't have the same hash, the Hamming distance will be small.

# Chicken with pHash

Now that we were going fully crowd-sourced, it didn't seem fair at all to charge any money.  But I continued to host the server so that everyone share puzzle answers.  I served up Asirra results for free and collected new answers as they got reported.  Every couple days I would regenerate the tree with the latest data and restart the server.  At peak I would get around 10 queries per second on my home-made VB.Net HTTP server.  I had about 2000 unique users in total.  I also calculated about how many points users were collectively earning using Chicken and the average value of a point based on selling stuff on ebay.  Chicken was probably responsible for around 1 million dollars of prizes all told.

Eventually Microsoft pixelated **and** rotated the images being served.  They got so distorted that pHash was at a loss.  They were also cracking down in other ways.  For example, my entire country was banned from all of Club Bing.  In 2012, Club Bing shut down.

I never got an Xbox and my inflatable Kayak never arrived.  I mostly just sent prizes as a surprise to friends and family.  The only thing that I got for myself was a cheap telescope and a jacket that I like.
