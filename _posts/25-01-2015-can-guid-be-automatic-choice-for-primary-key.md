---
layout: post
title: Can GUID be automatic choice for the primary key?
---

Lately the discussion came on: if one should use Globally Unique Identifiers ([GUID](http://en.wikipedia.org/wiki/Globally_unique_identifier)) as column identifiers(primary keys) at database.

The arguments against using it were: readability, performance penalty and cumbersomeness.

I'll try to answer why it's still preferable than other key types, and also to see where GUID fails to be a good table key. 

First of all GUID is long. While Int is usually 4 bytes, GUID is 16. It's hard to read. It's hard to enter manually. It's hard to remember. It's representation as long hexadecimal string is awful. But... well, in my opinion database key isn't something that should be used by user anyway. GUID shouldn't be shown in any place in UI interface, not as field, not in URL, not in caption. Let's keep GUIDs for computers. For them it's just 128 bits. And that's great. It means no one will interfere with them. All joins that are performed on unique identifiers will not be harmed by typos. In ideal world, people won't see those id's. And because our world is not ideal, we invented copy-paste mechanism.

When performance is coming to play, I can point to [this](http://www.informit.com/articles/printerfriendly/25862) article. It says that all basic actions except insert are slower by 1.1 than integer auto-increment. By the way, tests were done on now legacy hardware, and I expect from CPUs with more bits in registers to crunch GUIDs faster. Inserting is slower due to random nature of keys. Its just taking more time to find where to put the key because it's non-sequential. Technique to overcome this issue is shown in above article. The GUIDs made partly sequential - partly random bring inserting to large tables overhead to same 1.1 factor. 

Jeff Atwood mentions in his [article](http://blog.codinghorror.com/primary-keys-ids-versus-guids/) that GUID can be generated without central authority. Almost all programming languages can generate GUID by themselves. Looking back at my experience this knowledge and design could keep me away of trouble and days debugging at least once.

Another point, that the GUID, when used as a key is a surrogate key. It means that all other columns at table can have arbitrary values, without any constraints at all.

Some other points I can say that they're pros of using GUIDs are:
* They're collision-safe for distributed databases
* It's easier to merge tables when GUIDs are keys
* You can store orders of magnitude more data than with int key

Cons are:
* It's better not to use GUID as clustering key because of weak([Kimberly Tripp](http://www.sqlskills.com/blogs/kimberly/guids-as-primary-keys-andor-the-clustering-key/) would say *Horrible*) performance
* It's still slower even for non-clustering keys - but in this case upgrading to SSDs can eliminate the delays.

To conclusion, in most cases Globally Unique Identifier can be used as a primary key for tables. I believe that only in cases where performance is a great deal and amount of data is lesser than integer types can handle, non-GUID key must be used. If performance is not the issue it's no question, and when amounts of data are becoming "the big data", GUID is only option for distinct database row.




