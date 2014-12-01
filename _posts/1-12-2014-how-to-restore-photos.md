---
layout: post
title: How to restore photos
---

So my dad accidentally shift-deleted all family photo albums. At the same second he called me and told me about this. 

Somehow I remembered that one can't simple un-delete files from ext4 file system. I read about ext4undelete, but somehow that didn't fit well. I had to launch something from remote, and didn't had another boot media at parents' house. 

I almost gave up, but recalled about tool called photorec, that saved me more than once in the past. Despite that in UI it says ext2/ext3 only - it works with ext4 too! In ubuntu it comes in 'testdisk' package.

It worked for 20 hours and ended up with about 9000 folders, each with ~500 files. "Ok, most of them is junk", I thought to myself. Need to extract only jpegs. Some bash magic with find and mv and -- {} +, and I ended up with one directory. But it consisted of 650000 files. Nautilus and Gnome Commander failed to open it in reasonable time and got stuck. I used find again and removed all files less than 2 megabytes in size. It removed only 15k of them. 

Now I need to write another script that will sort the files back in folders.

I'm not the first one who've done this.

Learned from:

[http://stackoverflow.com/questions/19880246/move-only-files-recursively-from-multiple-directories-into-one-directory-with-mv#19881331]
[http://askubuntu.com/questions/201568/how-to-move-only-a-specific-amount-of-images-from-a-folder]
