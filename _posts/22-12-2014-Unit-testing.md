---
layout: post
title: Unit testing
---

Last week I tried myself again in training. I gave one hour session on unit testing to my new coworkers. I felt like uncle Bob himself, explaining the red-green-refactor cycle. 

The hour was split in 2 parts, in first half hour I talked about unit testing in general, explained it pros and cons, showed the borders. I threw in TDD, mocks and stubs. In second part, I coded a class that does some string processing, showed how dependency injection works outside of container. I adapted all I knew from .NET world to their Java counterparts. Instead of familiar [NUnit](http://www.nunit.org/) and [MStest](http://en.wikipedia.org/wiki/Visual_Studio_Unit_Testing_Framework), I used [jUnit](http://junit.org/), and instead of [moq](https://github.com/Moq/moq4) I used [Mockito](https://github.com/mockito/mockito). I found using annotations for mocks convenient, and more clean than creating an objects in .net, on other hand moq and its syntax of lambda setup and verify looks much better to me. In Mockito, there is inconsistency - *verify* works on mock object, but setup, and it doesn't matter which : by *stub* or by *when* - on method call.

In general, practice of TDD and unit tests coverage is contributing much more to the project in the team. Tests serve as a documentation of an intent, provide safety. It's crucial that everyone in the team understands benefits of unit testing. Automated tests speed up development of complicated pieces of code, makes changes and expansions easier. TDD leads to right, low-cohesion, architecture.

I found the [answer](http://stackoverflow.com/questions/237000/is-there-hard-evidence-of-the-roi-of-unit-testing) on stackoverflow.com, that shows that there were researches conducted to show an impact on development speed and quality. 

In my opinion, the quality of a codebase is important for any software project that includes more than 100 lines of code. Taking into account that even small software projects tend to grow in size, even the smallest of them should be covered with tests from the beginning.

I shall continue to read "Clean Coder" right now :)
