---
layout: post
title: Two constructors
---
When looking in the code of some project I've found something like:

    public Class() {}
    static Class() {}

What should this do?

After short investigation I found that there are both constructors are working. Cool :)

Sample code:

    using System;

    namespace TwoCtors
    {
        internal class Someclass
        {
            public Someclass()
            {
                Console.WriteLine(  "I'm public ctor  ");
            }
    
            static Someclass()
            {
                Console.WriteLine(  "I'm static c'tor  ");
            }
        }

        class Program
        {
            static void Main(string[] args)
            {
                Someclass s = new Someclass();
                Someclass d = new Someclass();
            }
        }
    }

And the output is:

    I'm static c'tor
    I'm public ctor
    I'm public ctor
    Press any key to continue . . .

Surprised I was...
