---
layout: post
title: 5 Essential Linux tools replacements and how to install them
---

I never liked the syntax of several linux commands. I can't use `find` to find files. `top` was never top choice for process monitor (well, I was spoiled by Windows). And in the end, I'm too lazy to read `man`s. I need `tl;dr`.

And then I see this article about [5 linux essential tools replacements](https://opensource.com/article/20/6/modern-linux-command-line-tools). It's like someone read my mind (or old linux tools are really not so much comfortable).

The list of tools mentioned in the article:

```
ncdu  //instead of du
htop  //instead of top
tldr  //instead of man
jq    //instead of sed/grep for json files
fd    //instead of find
```


But not everithing is great. Because those tools are not standard yet, and in Centos 7 most of them is not installed trivially.

fd
---

To get a `fd` working on centos, I had to download .tar.gz file from github [releases](https://github.com/sharkdp/fd/releases) page, untar it (hey, this one could use a modern version too) and install to `/usr/local/bin` directory. 


```
wget https://github.com/sharkdp/fd/releases/download/v8.1.1/fd-v8.1.1-arm-unknown-linux-musleabihf.tar.gz
tar -xvf fd-v8.1.1-arm-unknown-linux-musleabihf.tar.gz
cd fd-v8.1.1-arm-unknown-linux-musleabihf
cp ./fd /usr/local/bin/
cp ./fd.1 /usr/local/share/man/man1/
mandb
```


tldr
---
Note that `tldr`'s pagea are in internet and this client needs `curl` to be installed in order to work. Installation instructions: 

```
cd /usr/local/bin
wget https://raw.githubusercontent.com/raylee/tldr/master/tldr
chmod +x tldr
```


ncdu && htop && jq
---

These utilities got it's way into CentOS repositories and can be installed with `yum install -y ncdu htop jq`.


credits: 
---
[fd installation](https://enting.org/how-to-install-fd-on-centos/)

[tldr client](https://github.com/raylee/tldr-sh-client)
