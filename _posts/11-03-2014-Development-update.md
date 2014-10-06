---
layout: post
title: Development update
---

Greatly inspired by 7drl and the book I read(Game development principles by Alan Thorn), I use my spare time (and finally I have a bit of it) to work on my rogue-like game engine.

Yesterday I refactored it major refactoring, removing all components that were poorly designed, and left with the basic skeleton. At least there basic stuff works, and even no base test was broken. Actually, that means that don't have enough tests there.

Next thing in my plans will be level creation, I want to make it like INI files(and don't you hit me for that), which keep set of rules for generating level.

Each level description should include entry points, danger level modifier, exit points(not only Cartesian coordinates, but rules that should be met to move to the next level) and hardcoded layout(or rules for terrain generator, f.e. percent of water filling the level).

To check this out beforehand I have to implement some rendering, and here I still not sure if to go pure ASCII or to look for some graphic representation.

What I sure about, that my previous implementation of manual strategy (what controls the player) was totally wrong. I deleted it, and what it should be is a keyboard listener that writes relevant commands into the queue of a strategy. Some keypresses should be sent to outer circle of control, like commands to save or exit.Greatly inspired by 7drl and the book I read(), I use my spare time (and finally I have a bit of it) to work on my rogue-like game engine.

Yesterday I refactored it major refactoring, removing all components that were poorly designed, and left with the basic skeleton. At least there basic stuff works, and even no base test was broken. Actually, that means that don't have enough tests there.

Next thing in my plans will be level creation, I want to make it like INI files(and don't you hit me for that), which keep set of rules for generating level.

Each level description should include entry points, danger level modifier, exit points(not only Cartesian coordinates, but rules that should be met to move to the next level) and hardcoded layout(or rules for terrain generator, f.e. percent of water filling the level).

To check this out beforehand I have to implement some rendering, and here I still not sure if to go pure ASCII or to look for some graphic representation.

What I sure about, that my previous implementation of manual strategy (what controls the player) was totally wrong. I deleted it, and what it should be is a keyboard listener that writes relevant commands into the queue of a strategy. Some keypresses should be sent to outer circle of control, like commands to save or exit.

Ah, and I have to bring some dependency injection to the project, so functionality like adding new terrain types will be easier.

That's all for now, and I have to implement all this before moving forward. Keep waiting for updates!

Ah, and I have to bring some dependency injection to the project, so functionality like adding new terrain types will be easier.

That's all for now, and I have to implement all this before moving forward. Keep waiting for updates!
