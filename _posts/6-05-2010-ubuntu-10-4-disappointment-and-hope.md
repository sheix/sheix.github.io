---
layout: post
title: Ubuntu 10.4&#58; Disappointment and hope
---

Well. I've updated it again, and as usual after the upgrade i wish i never did that. It's even not so bad. But it is annoying: couple of small bugs, one major hardware problem, disappointment and hope. 

Shwai-shwai. 

First of all - and I mean it - may be users should be given an option if they do want to keep the interface, that was already customized by them and upgrade only what's "under the hood"? For couple of days after update I looked for volume control, that disappeared from the panel, and i was glad to find it again today in applets, with some kind of strange name(it's no "volume control" or "sound meter").

Another thing - that my scanner stopped working. Actually it works, and it works great in any OS, except Ubuntu 10.4 (No way, I don't know what's the code name). I've tried reinstalling the driver from Samsung site(Hey, they're good - they do support Linux). From graphic interface it fails to find a scanner without any error message, but I've checked the console and got the message that says:
"netdiscovery: relocation error: /lib/tls/i686/cmov/libnss_files.so.2: symbol strcmp, version GLIBC_2.0 not defined in file libc.so.6 with link time reference"
I found out that netdiscovery is some utility provided by Samsung, looks like it isn't opensource. So I wish I could re-compile it with new libs. And i still didn't found the way-around this problem. Well, strcmp should be simple, right? Students learn it on the very first course of C :)

There are some other people that stuck with similar MFP's. I wrote an quick email to Samsung tech support, may be I'll get some answer.

And Mark Shuttleworth on his very last interview said that upgrading to new release is like Russian Roulette for the users, but added, that the Community will take care for all of them. And I, like agent Mulder, want to believe him :)    
