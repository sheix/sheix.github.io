---
layout: post
title: Easy to fix
---

I'm not sure exactly, but from my experience, and, applying the famous Pareto rule: 20% of work is actual software development and 80% - bug fixing. So, how I can help in making the most time-consuming process shorter and possibly easier? As a person, whose first programming job was, let me be honest, fixing bugs for 2 years, I know a lot about them :).

First thing, is "to fight the bug, we must understand the bug". You must know where the bug lives. The best map to bug's hideout is well written log. If you know what happened at a point of failure, what was the system status, it's much easier to spot an error. Tools that can help us are well known stack trace, memory dumps, logs. I world recommend log4j family of loggers.  

Another point, that dev team must know that bug is actually happened, something crashed or gave incorrect result. Reports that are coming from local QA team, or clients that are collaborative are handled instantly, and that's fine. All other issues have to make their way to the developers which should sort and then fix them. Microsoft's error reporting is example for it (by the way, Pareto rule strikes again - 80% of bug reports are eliminated by fixing 20% of most reported issues). Android and IOS also have a mechanisms for reporting. Even if you somehow can't integrate automatic error sending back to you, as a manager, you must provide a way of feedback, even if it's forum, email or support phone number. Great platform for discussions (and not only for programmers) is Discourse - simple at installing, managing and participating.

Also, one of best way of knowing that error did happened is falling. Have one or zero places in your program, where you do the error handling. Don't swallow exceptions with catch blocks without rethrow, don't catch all exceptions on each level, avoid using exception handling as flow control mechanism. Exception should be propagated to a layer where it's logged, reported to user(if needed) and handled. Decision may be some kind of recovery or restart, ignoring the error or failure of software. This idea is called sometimes: "Samurai principle": if you fall, fall fast. I consider returning error codes a bad practice - it prompts to handle it at every layer, instead of single place. In addition, it introduces magic constants and numbers. 

And when bug is found, and fix is almost done, I have one more advice for you: write an unit test that reproduces the bug and add it to the test suite. This way you'll understand reasons that led to bug in the first place, working on fix will be faster, and it'll give straight indication if bug is fixed. You will not need to run the application to check each minor change. And, as a bonus - you'll have a test that will prevent the bug from rising again in the future.

That's all for now. Hope that it have been useful :)

Here, take this:

[Raid picture]
