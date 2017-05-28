---
layout: post
title: How assumptions cause harm to your program product
---
Yesterday, after another session of Evolution, one of my friends told me that I was always kind of "fix stuff that doesn't work" guy. And yes, I was. Starting in childhood, motivated by great people around me, and being sure in myself, I looked for defects in stuff and fixed them. Creaking doors, broken toys, bicycles, bugs that prevented computer games to run. Looking for the reason, analyzing, fixing. For the new year I've asked for Legos and sets of tools.

Now I found myself in position of software engineer in some large company, more than 1000 employees. I am in the team with many names - dev support, product experts, release team. Our job is to prepare a product(also a large and complex one) to shipping to clients. And most of the time we're fixing bugs.

As part of working together for the goal of releasing quality product in time we all are supposed to do a good job. Burning with enthusiasm, I'm starting my day and see an issue in my list : "Loyalty club points not working"

(The product is merchandise suite)

Looking at description. Nothing. Looking at steps to reproduce:

1) Sell Item
2) See Points
3) ....

OK. Good. That's better. Let's see attachments. Oh, nothing again.

Now I have to look at person's name, who opened the issue, and whoever it'll be, call him to ask for details. Oh, he's on vacation.

Well. I'll wait with this one. Next.

"BU is not filtered by DMS on HQ level"

Attachments - 5 Mb log. Steps to reproduce empty. I have to guess. Or there's even no mention of what kind of enviroment is needed in order to reproduce the issue. As for me, I know what BU and DMS mean and how filtering works, and what about that guy, who joined the team two weeks ago?
Also, the log wouldn't help there. When something happens, it's logged, when something does not, log could help, but it's definetely not the only thing developer need to fix an issue.

Last one before going home. "Screen is not changing when clicking some button". Good, that should be easy, there are steps for reproduce, and attachment. Again 5 mb of server logs. Server. Oh. The face and the palm already hurt so much.

After days like this, complains to team leader (and QA team leader), begging for details, CC'ing half the company management with bug descriptions, I found nothing better than to write it all out.

There's couple of things I want to say to people that want me to fix stuff.

First, the among the reasons of bugs there is wrong assumptions. First, check carefully if the issue should be opened at all. Know the product, the behavior you see as erroneous may be perfectly right and intended to be so, or corrected to what you want by a simple checkbox in the properties.

Second, assumptions again. Don't assume that developer have exactly same environment as you. We have another architecture PC's, another amount of RAM, different OS, SQL version, peripherals connected. We may not even have the same software you have, because part of it is provided by third parties to system integration, and not to us, developers. Please describe exactly what you have around. May be this is not needed sometimes, but there's always better to have more details than you need than less. Pro Tip: when testing a system, ready a template that you'll copy to each issue you're opening in the template with the details.

Third, guess what, assumptions. Developer may not know what's obvious to you. Generally, he's a smart person, but definitely is not total base of knowledge. When it's obvious to you that some button's caption in the UI was translated by client to something else (How do I supposed to guess that "Return transaction" and "Post void" are same stuff?) or even to another language.

And last and not least, assumptions. It may be other developer assigned to bug and not one who originally coded stuff around. Usually the bad coder got promoted or left the company. So, the one who thought(we all hope) about the domain, design and architecture, probably wouldn't help. And even if you worked with the original dev, the new one surely doesn't know the domain as the first or may be someone who already done things around problematic code. And most of the time he also doesn't want to learn others' code, just to make stuff work again.

Remembering those points may surely make things go faster and may be even better. Defects would need less research, product will be shipped in time and client will be satisfied. Assumptions may be harmful! Don't forget it when you're submitting an issue in launchpad, your company's tracker or even calling ISP tech support. Usually people on other end of the line have mutual interest with you.
