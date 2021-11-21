---
layout: post
title: 5 Essential Linux tools replacements and how to install them - script
---

It took me some time, but I wrote an installation script for some tools which I mentioned earlier and some new ones.

The script is published on [github](https://raw.githubusercontent.com/sheix/stuff/master/scripts/install_linux_tools.sh) and it installs the following tools:

* fd v8.1.1
* lsd 0.20.1
* duf 0.6.2
* jq 1.6
* bat 0.18.3
* zoxide latest with script
* mcfly 0.5.9

To run the script it should be downloaded and have run permissions:

```
wget https://raw.githubusercontent.com/sheix/stuff/master/scripts/install_linux_tools.sh
chmod +x install_linux_tools.sh
./install_linux_tools.sh
```

Note, that the script will work only on machines with x64 architecture.

When supported, it'll add man entries.
