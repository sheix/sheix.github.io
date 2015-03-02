---
layout: post
title: How do I saved the day again
---

After couple of lightning storms and voltage spikes, my HDD (my bad, I still use one) went nuts. Error indicating superblock read failure welcomed me instead of booted computer last time I restarted it. 

I've tried to boot from ubuntu-gnome 14.10 livecd, but with no avail. Somehow the tool I always used to create bootable usb sticks didn't succeeded on creating this one. I startet to dig deeper into the forums. I guessed that the fix is still possible.

I wanted to run fsck, so I needed to launch bash, when last thing I seen was GRUB prompt. I found out that it can be achieved pretty easily be adding 

    "init=/bin/bash" 

on the end of kernel line (from [here](http://help.fonality.com/TroubleshootingFAQ/Premises_(PBXtra,_Trixbox,_Dell)_FAQ/Server_Hardware_Troubleshooting/Hard_Drive_Recovery_Procedure)) . I've got root prompt, and it was a beginning. I identified that /dev/sda5 was problematic partition (it's where my home is). Running fsck yielded no result, and I tried to look for other solution. First of all, I learned that I can see all connected drives by running lsblk command [here](http://www.cyberciti.biz/faq/linux-list-disk-partitions-command/) . And the last piece of puzzle was restoration of suberblock from [backup](http://www.cyberciti.biz/tips/surviving-a-linux-filesystem-failures.html) : 

    e2fsck -f /dev/sda5  ; solution did not worked, but that's fine
    mke2fs -n /dev/sda5
    e2fsck -f -b 32768 /dev/sda5

And than I pressed "y" around couple hundred times. And reboot -f and... booted back to good old ubuntu.

Now doing backups :)
