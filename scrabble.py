scores = { 'a' : 1
         , 'b' : 1
         , 'c' : 1
         , 'd' : 1
         , 'e' : 1
         , 'f' : 1
         , 'g' : 1
         , 'h' : 1
         , 'i' : 1
         , 'j' : 1
         , 'k' : 1
         , 'l' : 1
         , 'm' : 1
         , 'n' : 1
         , 'o' : 1
         , 'p' : 1
         , 'q' : 1
         , 'r' : 1 }

words = set()

import json

for i in range(2,13):
    with open('%i-letter-words.json' % i) as file:
        j = json.loads(''.join(file))
        words.update(d['word'] for d in j)
