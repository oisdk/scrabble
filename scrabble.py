scores = { 'a' : 1
         , 'b' : 3
         , 'c' : 3
         , 'd' : 2
         , 'e' : 1
         , 'f' : 4
         , 'g' : 2
         , 'h' : 4
         , 'i' : 1
         , 'j' : 8
         , 'k' : 5
         , 'l' : 7
         , 'm' : 3
         , 'n' : 1
         , 'o' : 1
         , 'p' : 3
         , 'q' : 10
         , 'r' : 1
         , 's' : 1
         , 't' : 1
         , 'u' : 1
         , 'v' : 4
         , 'w' : 4
         , 'x' : 8
         , 'y' : 4
         , 'z' : 10 }

words = set()

import json

for i in range(2,13):
    with open('words/%i-letter-words.json' % i) as file:
        j = json.loads(''.join(file))
        words.update(d['word'] for d in j)

def score(word):
    return sum(map(scores.__getitem__, word))

from itertools import permutations

def all_words(letters):
    return (''.join(p) for i in range(1, len(letters)+1) for p in permutations(letters, i))

def best(letters):
    best_score, best_word = 0, None
    for word in filter(words.__contains__, all_words(letters)):
        s = score(word)
        if s > best_score:
            best_score, best_word = s, word
            print(best_word)
    return best_word
