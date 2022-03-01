import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, file):
        words = file
        self.lst = []
        self.no_of_lines(words)

    def no_of_lines(self, words):
        file = open(words, 'r')
        count = 0
        for line in file:
            line = line.strip()
            count += 1
            self.lst.append(line)
        print(count, " words read")

    def random(self):
        random_num = random.randint(0, len(self.lst)-1)
        return self.lst[random_num]


class SpecialWordFinder(WordFinder):
    def no_of_lines(self, words):
        file = open(words, 'r')
        for line in file:
            line = line.strip()
            if line.strip() and not line.startswith("#"):
                self.lst.append(line)
        print(len(self.lst), " words read")


wf = WordFinder("words.txt")
animals = SpecialWordFinder("animals.txt")
