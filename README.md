# PyAutoCompletion-Correcting
*python 3.6+
Console program, that gives you some kind of autocomplete functionality

## What it can?

So... Everything, that standart autocompleters can. This program is mush simplier, and that's why:
* Naive way of spellchecking (first and second level is just forward for-each in word corpus)
* Third level is suggestion by autocorrecting the word. This is a pretty good tool, check it [here](https://github.com/jxmorris12/language_tool_python)
* When you type at least 2 word, you can try to predict next word by using a language model. I use [this solution](https://gist.github.com/mohdsanadzakirizvi/7830375ffbba9dc0ef91e12921bf3550), but you can use any other languge models. Feel free to modify my program.

