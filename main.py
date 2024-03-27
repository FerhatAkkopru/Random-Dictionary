from random_word import RandomWords
from PyDictionary import PyDictionary

rw = RandomWords()
word = rw.get_random_word()
d = PyDictionary()
print(word)
print(d.meaning(word))
