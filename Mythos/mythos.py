from random import *
from scriptos import * 
from scriptos import timeline

#Imports .txt files for the nouns and adjectives to determine god hood and stuff
nouns = file_open("allNouns.txt")
adj = file_open("allAdj.txt")

pantheon = []
creation_myth()
print(timeline)

for i in range(5):
    pantheon.append(Character(gen_name(), gen_being(), randrange(0, 5999), choice(nouns), choice(adj), gen_power()))

for i in pantheon:
    i.printGod()

