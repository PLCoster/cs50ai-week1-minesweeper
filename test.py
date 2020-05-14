from minesweeper import Sentence
import random

test = set([1,2,3,4,5])
test2 = set([1,2,3,4,5])

print(random.choice(list(test)))

sentence = Sentence(test, 4)
sentence2 = Sentence(test, 4)

sentencelist = [sentence, sentence]

print(sentence2 in sentencelist)

print(test2.issubset(test))
print(test is test2)
print(test - test2)

print(test)

print(set(test))

if set():
  print('Empty set is true')