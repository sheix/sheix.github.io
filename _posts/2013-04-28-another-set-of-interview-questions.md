---
layout: post
title: Another set of interview questions
---

Sometimes I think that one can turn job interviews into sport. All participants, answer their questions! Now you need training from college, read books, past experience! Heart is pumping blood to the brain, you're excited, ready, steady, go! You can got the first prize, the job or lose and get experience. No one should underestimate this too. Next time you'll have your chance.

The fact that I wrote this paragraph means nothing but that I was on another job interview. Keeping myself in shape. It's not like it's bad where I am now. But I think that there are purpose in trying to get some more.

Technical questions was usual ones, technologies, your last project, your last bug. The riddles were more interesting.

First of them was to reverse order of words in sentence. Easy solution (x) gives only partial points. To get all you'll need low level language solution, and with time complexity O(n) and additional space complexity of O(1). The algorithm should be like this:

Find the first space from the end of the line
From the end of the line, to the space found, switch letters their places
Return on steps 1 and 2 until the beginning of the line
Read the line backwards

Tricky one. The fact that interviewer used window instead of whiteboard helped a lot :)

Second one was to find if the given IP address is in given range. The answer was so simple, that I was confused at first place and started to write spaghetti of ifs, and than, like asked the interviewer: "May be I'll turn it into some long and just compare the numbers?"

This was enough to pass, but I thought later that the solution is not cross-platform enough. Long should be presented as 4 bytes, that may vary. Anyway this problem can be solved too.

Third question was about writing a function, which is given two rectangles returns the rectangle that is an intersection of them.

My approach was to start from the simpler case. I've dropped one dimension. Solved this for line, and than expanded the solution to rectangles.

This looked easy, but the second interview with some more interesting questions to share with you, failed me to get the job. But I take it easy. Really. I'm fine, I just got an experience bonus :) And the riddles - they will come soon :)
