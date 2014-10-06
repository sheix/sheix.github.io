First of my three eases is "Easy to understand". The importance of this principle is unquestioned by everyone except people that do "job security" by producing highly obscured code. You can refer to http://TheDailyWTF.com for detailed examples. If you keep reading past this, I suggest that you're not such kind of person. If you understand the other's code - it easier to work on it, spot bugs, fix and understand. If teammate understands your code, you will be bothered much less and have much more appreciation. In general, producing code that is easy to read is profitable for individual and company alike. 


#Short
 
Short sentences are easier to understand. Example from chemistry: Di-hydrogen Monoxide versus Water. But there can be over-shortening: H2O. While not so bad in case of sciences, in business applications abbreviations can lead to constant WTF state. So common naming, without shortening to letters is the way to do. Also, Uncle Bob points to scope rule - while scope of some concept is small, name could be longer, while scope of concept is broad, name should be short. Compare:

    Transaction.Start();

Is broad concept, it happens for every transaction.

    RefundTransaction.GetRefundReceiptDetails();

Is more specific, can be explained better.

Also, simplification and shortening tendency is seen, for example, in C# evolution - while looping started in c style as

    for (int i=0;i<Collection.Count;i++)
    {
      if (Collection[i].property > 10)
      Result.Add(Collection[i]);
    }

evolved through

    foreach (var item in Collection) 
    {
      If (item.property >10) Result.Add(item);
    }

to LINQ statements, that can be written in one line, like this:

    Result = Collection.Where(m => m.property > 10);

Keeping clarity of intention and short record with almost no boilerplate code.


#Clear

Being clear means that code means what it should do, variables names are matching their content, and there is no clutter around. For example 

    lpszVarName 

is cluttered. lpsz is trash. Get a Visual Studio, even Express Edition will do. Using Linux - not a problem - get CodeBlocks. Stop coding in notepad. If you want to know what type variable is - just hover a mouse on it. If you say that you don't want to move your hands from the keyboard - get ThinkPad or Latitude, they have that funky mouse thing between G and H.  

Also, this name is contaminated with short-cut. Var for variable is fine when it comes from the language. See, if you'll just call this entity: 

    Name

You will lose entirely nothing. It's shorter and it means the concept behind it.


#Strict 

Variable, Class, Function, Method, Property, Every concept in programming usually have it's name. Yep, there are anonymous stuff, but it's pretty good. Zen Programmers says, that the ideal code is no code at all. But currently let's say it's out of scope. When it comes to naming, the name of every column in database, in every smallest temporary variable should say what it means. If it's key, call it a key, if it's counter - call it counter, if it's ordered collection of key-value pairs of unique identifier and location on map call it SortedList<Location> locations. In functions or methods name have even more meaning - because function can have side effects, which are undesired by their own. So function name should be exactly what it does. I'm thinking of some exercise: Try adding a suffix for each side effect to a function name. It'll end in ridiculously long name, but you'll see that in this case you will be or able to refactor it to a list of sub-routines which do exactly the same, or extract the meaning of what you've done and call the whole concept with a new, more abstract, name. 


#No Magic

Somehow software developer, system administrators, computer technicians and other people that "do stuff" with the computers are thought to have some "magic" aura. No, we're not wizards. You don't have to be long-bearded man to fix some router or make a complicated web-site. So, even if you're thought a guru, there is really no need to use magic in the code. By magic i mean:
* Magic numbers
* Magic constants
* Magic operations

With numbers it's pretty simple. I think there no need to use numbers almost at all in the code. We all understand, that 1 is usually added for next, and zero means absence of some value, and we all know that 42 is the answer to the ultimate question of life, the universe, and everything. But if you mean to add length of menu item to it's x staring position to get where the menu item ends, it's much better to write:

    itemLength = 100; 
    ...
    var endMenu = startMenu + itemLength;

than to make us guess what:

    var endMenu = startMenu + 100;

means. Almost always I'll prefer using class members on variables, leaving inner scope declarations for stuff that really shouldn't be influenced from outside code, like algorithm implementation details, counters and so on. 

#Magic constants
Also, some people are sure that there is magic in numbers. Numerology, Gematria. Everyone in the company should know that 0x7777DEAD is code for some error that happens each Friday, 13, with the full moon in the clouds. 24 is the number of output channels. 2 speakers. Wait, what happens if there's user with 5.1 home theater? By the way, functions that returning error codes, are considered magic constants too. Absolutely evil. They should be handled exactly as magic numbers - by giving them meaningful name, single assignment, and usage of this identifier in every place needed.

#Magic operations
Sometimes there is need (or no need) to optimize code for performance. For example, one of techniques used for this was using shift instead of multiplication. Another example I think of is bit-wise operations. While pretty common in firmware and real-time programming, it can be pretty non-self explaining in "pure" software. Such kind of optimization should be rewritten due to two reasons I can think of: 1) It's not clear 2) If some platform-specific knowledge is used to make this optimization (x86 shift is faster than multiplication by power of 2) is not guaranteed to be same across all other platforms code can run on. If there is a reason not to rewrite it, the reason should be explained in comment line above.


#Consistent
The only reason not to follow those advises is consistency of code base. When there are more than one teammate in the development team, they do have set of rules, of how code should look. Those rules may be unspoken, may use some industry standard, you may have some document explaining it, configuration file for an IDE or StyleCop policy that prevents check-ins. And the best way to write code here - is to follow that policy. When code is consistent, it's easy to everyone to read it. You may not like curly braces placement or Hungarian notation, but if it's common in your team or company - you have to work this way. 

In addition, consistency may change by agreement with other team members to set new rules and policies. Evolving is needed, due to modern tools and practices. I encourage to try to set new standards in every team. It's just striving to be better. But, if it was not accepted, it's yours to comply to current rules.    

While writing the article, I've made some changes to mind map, I've extended it, here it is: 

[Mindmap picture]

Change and extension is the essence of working with software. Next time I would like about what is an "Easy to extend". 
