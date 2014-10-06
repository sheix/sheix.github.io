---
layout: post
title: Easy to change
---

In our capitalistic world software is the tool for fulfilling the business needs. In order to sell, in order to be competitive software have to evolve. You can't imagine Windows 3.11 on today's computers. IPhone 3 is not an option. Software becomes more complicated in our microwaves, fridges, cars, thermostats. There are two ways of growing - to the width and to the depth. In my opinion - width is providing more functionality, while depth growth is enhancing current - making stuff work better, faster, taking less resources. This time I would talk about growing to the sides, while next time I'll talk about fixing and improving software product.

Fast, safe, easy
Market is fast. If you do not deliver a feature in time, your competitor do. In order to work faster, workbench should be ready when the carpenter starts his work. In terms of software engineering, workbench is framework. Programmer expects that adding a feature will be as simple as writing code. So, business requirements already should be ready for him. Also, the architecture should allow fast extension. If feature demands adding UI components - project should have UI layer, and clear vision of working with it, while it's collaboration with graphic designers or binding mechanisms and design pattern in use. Those have to be consistent, once MVC there always be MVC, until it's decided to rewrite this part. If change includes adding an algorithm, algorithm layer should exist, and algorithms have to be provided by some kind of factory.

That means that project manager that wants to start adding features fast should ready the ground. With help of architects design should be proposed to answer the needs of the goal project. All people who will work in team, should be trained well on the design.

Another preparation for work should be in the infrastructure. Fast builds, continuous integration, integrated issue tracker and good source control system is a must. All above is actually time-consumers and should work as fast and seamless as possible. All routine tasks should be automated. Documentation should be generated from code.

The loop of requirement analysis, design, code and test/verification should be as fast as possible. In my point of view, that means that tasks should be small, well-defined and testable.

That brings me to second point I want to talk about: testing.

One of the most common programmers' fears is breaking something existing by adding functionality to software code. Regression testing can help overcome that fear. Once, done manually, by programmer himself or by quality assurance person, it could took long time. Waiting for the feedback paralyzes work. Automatic regression tests were introduced - faster, but complex and complicated. And still slow. And demanded maintenance. It's still debated, but in my opinion, that muda, that wasted time, may be greatly reduced by replacing those test with much faster unit test suite. Unit tests are the safety net for the code. TDD, technique that makes best coverage by promising no untested code by its definition greatly helps. To make unit tests work, however, couple of steps should be taken. First, check-ins that fail any of tests should be disallowed. Second, any functionality related code change have to be covered by test. Also, architecture should allow painless testing: keywords are Dependency injection, Programming to interfaces, layered structure. Everyone have to comply working by these principles. Whenever rules are broken, safety net is tearing apart. Classes and modules shouldn't depend tightly on each other - this way mocking external dependencies is simpler.

Downside of unit testing that it's not 100% can replace regression testing. UI, databases, hardware and integration can't be tested this way. Anyway, relying on passed unit tests reduces waiting time and eliminates amounts of bugs prior QA or Customer phase.

Code covered by unit tests, where each unit does what it supposed to do and does it right, is safer to change.

Easy to extend
Ideally, if you have your code is built from blocks, which are connected by interfaces to each other, it would be great if you can change the block easy.

For example of the change, let's see replacing method in code: we can replace 

    QuickSort(array);

With

    MergeSort(array);

Interface is same, change is only in one place, so it does the job. But what if change is in more than one place? Searching and replacing may be annoying, fast switch is impossible and in any case, this way is prone to errors. So even if change is needed through large codebase, it should happen once. Dependency Injection is technique that solves this problem. Specify the interface, use only it through the code and switch between implementation on the fly. Depending on framework, there even may be no work with code needed - only configuration change. Using DI container technique also implies better performance: objects that their lifetime is long will be created once, less memory leaks and simpler testing, are additional pros of using dependency injection. 
The cons are additional maintenance and need to train the programmers to think and work in DI in mind. Example for previous case would be:

    var sorter = container.Resolve<ISorter>();
    sorter.Sort(array);

and in some configuration there should be:

    container.Register(Component.For<ISorter>().ImplementedBy<MergeSort>());

Also, the interface ISorter should be referenced by both implementations.


So, to the conclusion. Extending product easily is a hard work. Investment in training, infrastructure and process improvements are critical. To keep stuff working the right way, team have to understand and support management, and management should support the teams. But when on track, using of mentioned techniques leads to quality, safe and extendable code, which, in its turn, makes the product standing out between the competitors.
