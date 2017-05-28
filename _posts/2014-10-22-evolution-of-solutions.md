---
layout: post
title: Evolution of solutions
---

I've been sidetracked a little bit in the last month, from working on my rogue-like. I took a vacation and worked on some other topics that interest me.

Among those topics there was an implementation of  engine for genetic algorithms. I learned about them back in the University and never had a chance to use them on real world problems. Shay Bushinsky led the course back then, and he shown us, students, examples of what genetic algorithms may do. Basically, it's heuristics that behaves similar to the process of evolution. Solution is encoded in some form, and different encodings are representing the population. Each of possible solution is evaluated by a fitness function, best of them survive, worst are discarded. Survived ones are being mutated and crossing over each other. Mutation means that some part of the solution is changed randomly, and crossover - that two possible solutions are split in two parts, and each of part is connected to part from other parent, in order to produce a new solution.

Traditionally solutions are represented as bit strings, which are decoded to actual solutions. I took less generic approach, and used the C# objects as solutions. Fitness function, that evaluates an object and returns number should be defined by user, as well as mutation and crossover operators. In some sense it makes it harder to use, in other - more versatile. The operations on the members of the population now can be more complex and have more sense than bit-wise manipulations.

I've published the [project](https://github.com/sheix/genetic-generic-csharp) on github. Meanwhile it lacks documentation, but usage can be derived from the example.

In my plans to extend the development of this engine and to try it on different problems.