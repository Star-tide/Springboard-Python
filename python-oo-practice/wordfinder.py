"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file):
        self.lst = self.grab_words(file)
        print(self.random_words())
    
    def __repr__(self):
        return f'Your words are currently: {self.word1} {self.word2} {self.word3}'

    def grab_words(self, file):
       with open(f'{file}') as f:
           lines = [line.rstrip() for line in f]
           return lines
    
    def random_words(self):
        self.word1, self.word2, self.word3 = random.sample(self.lst, 3)
        return f'{self.word1} {self.word2} {self.word3}'

