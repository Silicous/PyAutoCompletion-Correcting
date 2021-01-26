#!/usr/bin/python3

from big import *
from langmodel import out_model
from colorama import Fore, Style
import readline
import language_tool_python

# Change to
tool = language_tool_python.LanguageToolPublicAPI('en-US')


class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = options  # our suggestions.
        self.matches = []  # suggestion that matches current pattern

    # ALSO, IT WOULD BE BETTER TO WRITE A METHOD, THAT CLEANS AND ADD WORDS TO OUR SUGGESTION LIST
    # (see code with '%%%' mark)
    # I use 3 times same algorithm, but with different input list,
    # so it adds data to readline's history buffer differently.

    # A method to check word, find suggestion or correct it
    def __check_word(self, text):
        # first level of suggestions
        self.matches = [s for s, n in self.options if s.startswith(text)]

        # second level of suggestions, in case we don't have matches from the first level
        if not self.matches:
            self.matches = [s for s, n in self.options if s.startswith(text.lower())]

        # third level of suggestions, in case we don't have matches from the first two levels
        if not self.matches:
            correct = tool.check(text.lower())  # all suggestions to correct our word
            self.matches = correct[0].replacements

        self.matches = self.matches[:10]  # Just to not mess up the output

    # There ar
    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches

            # all our words in current input, delimiter is space
            buffer = readline.get_line_buffer().split()

            # if we have more than one word - use more advanced algorithm
            if len(buffer) > 1:
                joined_buffer = " ".join(buffer[:-1])
                readline.add_history(joined_buffer)
                if text:
                    self.__check_word(text)

                    # %%%
                    if len(self.matches) > 1:
                        readline.clear_history()
                        for each in self.matches:
                            readline.add_history(" ".join(buffer[:-1]) + ' ' + each)
                else:
                    # use language modeling to predict next word (works bad, better corpus and/or model should be used)
                    self.matches = [w for w in [*dict(out_model[buffer[-2], buffer[-1]])] if w.isalpha()]
                    self.matches = self.matches[:10]

                    # %%%
                    if len(self.matches) > 1:
                        readline.clear_history()
                        for each in self.matches:
                            readline.add_history(" ".join(buffer) + ' ' + each)

            else:
                if text:  # cache matches (entries that start with entered text)
                    self.__check_word(text)

                    # %%%
                    if len(self.matches) > 1:  # if we have more than one - add to history, so we can manually choose
                        readline.clear_history() # clean buffer (but still have some ghost words, I don't know why)
                        for each in self.matches:
                            readline.add_history(each)
                else:  # no text entered, all matches possible
                    self.matches = []
        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None


# BUILD YOUR COMPLETER FROM A LIST OF WORDS (need a dictionary)
# frequency_list = FreqDist(i for i in corpus_words)
# I've already prepared my corpus, see big.py

if __name__ == "__main__":
    completer = MyCompleter(corpus_words)  # parse corpus to a Completer
    readline.set_completer(completer.complete)  # uses some kind of bash line

    readline.parse_and_bind('tab: complete')  # pretty default thing, no other options, unfortunately

    # Input/Output. Give colors for better look
    entered = input(f"{Fore.CYAN}Input:{Style.RESET_ALL} ")
    print(f"{Fore.MAGENTA}You entered:{Style.RESET_ALL}", entered)

