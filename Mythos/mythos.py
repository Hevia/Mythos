from random import randint, randrange
from scriptos import * 

#Imports .txt files for the nouns and adjectives to determine god hood and stuff
f = open("allNouns.txt", 'r')
nouns = splitty(f)

f = open("allAdj.txt", 'r')
adj = splitty(f)

f = open("allPowers.txt", 'r')
powers = splitty(f)

f = open("allActions.txt", 'r')
actions = splitty(f)


#Generates and prints the gods
pantheon = []
for i in range(5):
    rand_noun = randrange(0, (len(nouns)-1))
    rand_adj = randrange(0, (len(adj)-1))
    rand_power = gen_power(powers, actions)
    
    pantheon.append(Character(gen_name(), gen_being(), randrange(0, 5999), nouns[rand_noun], adj[rand_adj], rand_power))

for i in pantheon:
    i.printGod()
