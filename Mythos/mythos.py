from random import randint, randrange
from scriptos import * 

#Imports .txt files for the nouns and adjectives to determine god hood and stuff
f = open("allNouns.txt", 'r')
data = f.read()
splitty = data.split("\n")
nouns = []
for i in splitty:
    nouns.append(i)

data = None
splitty = []

f = open("allAdj.txt", 'r')
data = f.read()
splitty = data.split("\n")
adj = []
for i in splitty:
    adj.append(i)

data = None
splitty = []

f = open("allPowers.txt", 'r')
data = f.read()
splitty = data.split("\n")
powers = []
for i in splitty:
    powers.append(i)

data = None
splitty = []

f = open("allActions.txt", 'r')
data = f.read()
splitty = data.split("\n")
actions = []
for i in splitty:
    actions.append(i)






pantheon = []
for i in range(5):
    randName = genName()
    randNoun = randrange(0, (len(nouns)-1))
    randAdj = randrange(0, (len(adj)-1))
    randAge = randrange(0, 5999)
    #gender = genBeing()
    randPower = genPower(powers, actions)
    
    pantheon.append(Character(genName(), genBeing(), randrange(0, 5999), nouns[randNoun], adj[randAdj], randPower))

for i in pantheon:
    i.printGod()


#(self, name, being, age, kind, adj, power):