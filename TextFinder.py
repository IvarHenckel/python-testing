import re
from abc import ABC, abstractmethod

class WordCounter(ABC):    # (ABC) is what we are extending
    @abstractmethod
    def process(self, word):
        pass

    @abstractmethod
    def report(self):
        pass

class SingleWordCounter(WordCounter):
    
    def __init__(self, wordToCount):
        self.wordToCount = wordToCount
        self.counter = 0

    def process(self, word):
        if word == self.wordToCount:
            self.counter += 1

    def report(self):
        print(f"SingleWordCounter found {self.counter} occurances of {self.wordToCount}")

class MultiWordCounter(WordCounter):
    
    def __init__(self, wordsToCount):
        self.wordCounter = {}
        for word in wordsToCount:
            self.wordCounter[word] = 0

    def process(self, word):
        if word in self.wordCounter:
            self.wordCounter[word] = self.wordCounter[word] + 1

    def report(self):
        print(f"MultiWordCounter reporting occurances:")
        for key in self.wordCounter:
            print(f"    {self.wordCounter[key]} occurances of {key}")

class GeneralWordCounter(WordCounter):
    
    def __init__(self):
        self.wordCounter = {}

    def process(self, word):
        self.wordCounter[word] = self.wordCounter.get(word, 0) + 1

    def report(self):
        print("GeneralWordCounter reporting occurances:")
        top = sorted(self.wordCounter.items(), key=lambda item: -item[1])
        for i in range(5): # for key in self.wordCounter:
            print(f"    {top[i][1]} occurances of {top[i][0]}")            

def main():
    counters = [
        SingleWordCounter("nils"), 
        SingleWordCounter("norge"), 
        MultiWordCounter(["skåne", "lappland", "småland", "blekinge", "medelpad"]),
        GeneralWordCounter()
    ]
    skipWords = set()
    f = open("undantagsord.txt", "r")
    for line in f:
        for word in line.split():
            skipWords.add(word.lower())
    f.close()
    f = open("nilsholg.txt", "r")
    for line in f:
        filteredLine = line.replace('.', ' ').replace(',', ' ').replace('?', ' ').replace('!', ' ').replace('\'', ' ').replace(':', ' ').replace(';', ' ').replace('\"', ' ')
        for word in filteredLine.split():
            w = word.lower()
            if w not in skipWords:
                for counter in counters:
                    counter.process(word.lower())
    f.close()
    for counter in counters:
        counter.report()

if __name__ == '__main__': # The purpose is actually that if we run this like a script we will run main. It also signals that you can run it like a script.
    # If we import this module main will not be run
    # Also nice explicit starting point
    main() 

