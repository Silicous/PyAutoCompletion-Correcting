# PyAutoCompletion-Correcting

A console program, that gives you some kind of autocomplete functionality. I made it as my project for the university.

## What it can?

So... Everything, that standart autocompleters can. This program is mush simplier, and that's why:
* Naive way of spellchecking (first and second level is just forward for-each in word corpus)
* Third level is a suggestion by autocorrecting the word. A pretty good tool is used, check it [here](https://github.com/jxmorris12/language_tool_python)
* When you type at least 2 word, you can try to predict the next word by using a language model. I use [this solution](https://gist.github.com/mohdsanadzakirizvi/7830375ffbba9dc0ef91e12921bf3550), but you can use any other language models.
Feel free to modify my program and use wherever you want.


## About files

You can see 3 python files: main, big and langmodel. Last 2 are modules, the first one is where all things go.
* Big.py - just a big word corpus. Sorted by occurrence in this text. (TODO put link here)
* Langmodel.py - a code for the language model. It can be used as a standalone script, so feel free to test.
