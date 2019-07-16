---
layout: post
title: My first opensource contribution
---

As far as I learned about opensource software I understood it's importance. I've read in some blog post that great way to learn to program is to join an opensource project, to fix a bug or add a feature. I even advised it to "newcomers" of the trade. But I never succeeded in this until now. I've tried, but it always was hard. I couldn't build a project on my PC. I couldn't decipher make files, or C++ code. I've looken on opensource projects which I adored and I couldn't contribute even a typo fix. Unti  l yesteday.

I learned about what Linux is around 14-15. Now I'm 34. 20 years, 7 of them working as full-stack developer, 4 - at CS B.Sc, 2 - in high school, with major in Programming and Russian Literature. Year here and there writting scripts for it job or home computer management. Years of using Linux and other free as a beer and a freedom software. And now I'm giving back.

It's not a lot. Around 100 lines of code, not including tests. It's not on general use project, some would say on a niche one. But it's a first step to me. 

And it went smooth. I've used the library more than a year and spotted common pattern of things I was doing again and again on my own, which, I thought, could be the part of that library. I've impemented it in my code, then made a fork of an original project and learned it a bit. I've found right places where to put additional code, learned code style of maintainer of the project, changed and tweaked my code a bit to support thing or two I've didn't seen before and all of this while writting tests to cover my new functions.
What helped me, is a "CONTRIBUTING.md" file, which described the flow to do in order to apply a patch to code. Thanks to IBM too, where I learned about github flow, what pull request is, and how to fork and merge back code. 

So I was ready, and I run the tests on my machine and pushed the code (not before checking out legal issues with our chief architect - because I'm full-time employed and by contract code that I write usually don't go to public domain).

The maintainer of the project talked to me shortly, and accepted to merge my PR in less than a day. And it went straight to next release. So here it is, ladies and gentelman, kotlin assertions library, [kluent v.1.53 ](https://github.com/MarkusAmshove/Kluent) as for now.