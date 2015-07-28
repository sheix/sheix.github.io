---
layout: post
title: Windows 7 and Ubuntu pitfalls
---

I bought myself a new SSD and decided to reinstall all of operating systems on my desktop computer.

I found out that I'm a bit rusty. Nevertheless - I took a day off my job and started to work. Backed up all the important stuff, done. That was easy part. Than I plugged my new drive into the case, ant tried to install Windows.

It was my first time with Windows 7, despite having the DVD's since my BA studies. So I was pleasantly surprised by much more friendlier installation wizard and optimized process, than its predecessors. I was given an option to partition all of the drives, like in Ubuntu installation. I started the installation and... Ooops, it even did not started. At 0% it failed with 0x80070015 error. 

I blamed cheap SATA cable(which was ok), bad media(turned out it was fine). I blamed myself for doing something wrong with USB Bluetooth adapter - why - because it's first google search result for error number. But finally I found a solution - it was so simple - but I did not know about it. I had to go to BIOS and switch SATA mode to AHCI. 

Windows installed, drivers downloaded, looks fast, works fast. Now it's time for something I know well - it will be peace of cake - Ubuntu installation!

"Ha", thought my karma.

I used Linux Live CD creator to put an image to the USB. First - Ubuntu 15.04. Failed with some error. Tried again. Same. Restart. Ok, another image - 14.10 GNOME-Ubuntu - same result. Nothing works. Restart again. Updated LiLi. Copied to another disk-on-key. Same. 

And only than I spotted that image I've downloaded is not supported by LiLi. Written in small letters. I downloaded and image from LiLi's dropdown - and it worked. Finally. Drivers and software, installed in two clicks. 

Including back ups - half day of work. Well, the result is what matters. Now all my apps run fast and I'm happy. Only if I had more time to play with it :)
