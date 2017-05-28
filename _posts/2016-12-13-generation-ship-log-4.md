---
layout: post
title: Generation Ship, Log 4
---

Usually in the first days of month I release another version of Generation Ship. And this month is not exception, so, here it is: [version 0.0.6](https://sheix.itch.io/generation-ship). One of the major  improvements is windows bundle - which you can download and play without any prerequisites, just unpack a zip file. Linux and MacOS versions are still not bundled with java because right now I can't test them on real machines. Due to low-level nature of libgdx rendering, I had not succeeded to test the game on virtual machines. 

With the help of a friend I found a critical bug in the MacOS version and fixed it. 

In addition, there were different minor bugfixes and refactorings. Selecting probes and planets became more intuitive, and hints what'll happen on mouse click were added. 

Generally, 0.0.6 was under usability sign. It didn't prevented me from changing some balance in planets harvesting, and its something that will be constantly improved. Right now the game is too simple to win, and does not give an incentive to explore, and this is what I'm planning to change. 

In the last couple of days I worked on creating a framework of testing and releasing the game. So I went on a bug hunt, and found a lot of annoyances. I would share the framework I worked on in one of my next posts.

Next release, in a month will consist of all those fixed. Mostly balance and rendering, but there should be some new surprizes, too. I decided that before I develop new features, I should take care of bugs and refactorings. This is also a point on one of my favorite [lists](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/) in the internet.
