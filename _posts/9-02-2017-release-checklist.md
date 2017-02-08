---
layout: post
title: Release checklist
---

Two months ago I've promised to write about framework I made myself to work on my latest project. So here it is, and I'm going to describe how did I came to this methodology.

So, I have background in computer sciences and being a software engineer for last 5 years. I used to work for large companies, where, usually, developers are surrounded and supported by team leaders, product managers, quality assurance engineers, software architects and release/configuration staff. 

One year ago, I started a hobby project, small game called "Generation Ship". Alone. In the beginning, there was one month of libGDX jam, I've done mostly code and assets. I've released the game, but later I decided to make it better. And I started to work. At first, I was writing code, drawing stuff, uploading files. There were multiple accidents when I provided broken file for downloading. I had too much ideas how to improve the game, but could not evaluate the time it'll take to implement or impact it will have on gameplay. It took me a lot of time to produce and verify working version. Code became complex. Things became harder. In addition, my beloved wife gave birth to our second child and therefore I had much less time for my hobby. 

Things had to be changed, if I wanted Generations Ship to continue travelling through space and time.

I started from scratch. As a mission, I've set to myself a statement :"to produce a quality* and interesting** game while on very limited*** time". I've tried it to start programming game before, but I always lost interest, or motivation, or found another project to delve into, or just procrastinated to the project death. It was not like this with Generation Ship. 

> <section>*</section> Quality - game works, end to end, with no crashes or unexpected behaviours.


> ** Interesting - game is not broken from the game design's definition. It's playable and winnable.


> *** Limited - if I have a hour to work in the evening, I'm lucky.

Around version 0.0.5, I've started to review whats going on and if it's any good. I've remembered that agile methodology is all about looking back and learning lessons.

Later I've came up with the following list:

1. Fix bugs/implement features 

2. Test implemented features

3. Play 5 games to check overall status

4. Fix critical issues

5. Write release notes

6. Build the artifacts

7. Upload to distributing platform

8. Update description and screenshots

9. Publish an update on social networks

10. Create new version and set its scope


Now I'll go step by step and tell in detail what I do in each one on them.

1. The most time I work on the game, I do work on coding and fixing stuff. There's always a learning too - new libraries to use, new tools. In addition, when you're alone - you're an artist, a composer, a designer. I used to keep a notepad to save ideas for later, not only for the code or game design, but also for sounds, music and art. In the very beginning of making a Generation Ship, I drew on paper all the screens. They do look different now, but this is the product of evolution of the game. 

2. Testing. Two phases, first - testing last implemented features and regression testing. Usually I do this with pen and paper. I write down bugs that I find and think of features and categorize them. Later, I use bitbucket's issue tracker for those I don't fix immediately.

3. Test play - both for regression testing and for checking out balance/gameplay issues. Done with pen and paper, too.

4. Fixing critical issues - any of issues that cause crash, won't launch situation, or, some critical malfunction - needs a fix. And than I go to step 3 again, to verify that no other functionality is broken.

5. I write down whatever changed since last release. It's nice to make it public, but it also provides me feedback about general direction of development for couple of last versions. For example, I've spotted that rendering and mode switching issues became more common with increased complexity of a game, so I decided to rewrite mode switching code. Eventually, this piece of code was of very poor quality.

6. I tried not to repeat myself doing manual labor, so I wrote couple of scripts that do building and packaging of assets. I used packr, libGDX's team tool, which is pretty simple and works out of the box. Almost no one will try to figure out how to launch your game if it's not straightforward. Tinkering for the sake of tinkering - is not as interesting as playing. I hope :)

7. I use itch.io, but it can be any other hosting: from own ftp server/dropbox public/google drive/steam if you're big enough. I like itch.io for it's audience, analytics and simple page editor. If you want feedback, you need to make game good-looking and discoverable, so...

8. Update page: let others know that project is alive. I put a date on the update, leave links to blog. 

9. I use personal facebook/twitter/google plus accounts. If you have more than hundred daily views/downloads, it's time to open and manage special account for a game. Also, the most downloads and feedback ever was correlated with posts on reddit.

10. Later on I take all of my records, bugs from previous versions, feedback from players, and narrowing the scope for the next version. I try to fix most annoying bugs, implement one or two significant features and close the technical debt on at least one unit. I keep every piece of feedback I've got, though I'm not oblige myself to implement every of it. I'm taking some time off the code and planning the release.


I have those steps in front of me whenever I decide that there's time to release. Ususally, it takes me a month to do all the coding and around two evenings to prepare and release the game. This framework demands a bit of discipline, and in my opinion, helps me to provide better results. Also, I'm open to changes and improvements - because everything is in progress, and a progress can't be stopped!

