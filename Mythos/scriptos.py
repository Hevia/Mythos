from random import *

def file_open(file_name):
    f = open(file_name, 'r')
    data = f.read()
    splitty = data.split("\n")
    return_list = []
    for i in splitty:
        return_list.append(i)
    return return_list


timeline = []
adj = file_open("allAdj.txt")


def creation_myth():
    rand = randrange(0, 1)
    birth_nouns = ["hatched", "birthed", "constructed"]
    birth_objects = ["Egg", "Ball", "Skeleton"]
    origin_templates = ["Time began when our universe was", "The universe as know it was", "In nothingness our world was"]

    birth_obj = ""
    birth_obj = choice(adj) + ' '  + choice(birth_objects)

    if rand == 0: 
        birth_method = choice(birth_nouns)
        origin_method = choice(origin_templates)

        timeline.append(f"{origin_method} {birth_method} from a {birth_obj}")
    else:
        birth_method = choice(birth_nouns)
        origin_method = choice(origin_templates)

        timeline.append(f"{origin_method} {birth_method} from a {birth_obj}")




def gen_name():
    name = ""
    words = ["que", "way", "eel", "ruu", "tish", "yar", "uub", "iek", "oy", "pe", "ah", "sha", "dor", "feek", "goo", "moo", "rabi", "doku", "baca", "szum", "lan", "ski", "-", "-"]
    for i in range(randrange(2, 3)):
        name += choice(words)
        
    return name

def gen_power():
    powers = file_open("allPowers.txt")
    actions = file_open("allActions.txt")
    the_power = choice(actions) + " " + choice(powers)

    return the_power   

def gen_being():
    being = ""
    attributes = ["giant", "huge", "tiny", "", "meek", "strong"]
    beings = ["god", "goddess"]
    being = choice(attributes) + " " + choice(beings)
    return being



class Character:
    def __init__(self, name, being, age, kind, adj, power):
        self.name = name
        self.age = age
        self.being = being #Is it a god, centaur, hero
        self.kind = kind
        self.adj = adj
        self.power = power
        self.hates = []
        self.loves = []
        self.children = []
        self.parents = []

    def __str__(self):
        return self.name

    def setParent(self, parent):
        self.parents.append(parent)

    def setChild(self, child):
        self.children.append(child)
        child.setParent(self)

    def printGod(self):
        print(self.name, "the", self.adj, self.age, "year old", self.being, "of", self.kind, "has the power to", self.power)

    def printFamilyTree(self, depth):
        for child in self.children:
            for brace in range(depth):
                print(" | ", end="")
            print(child.name)
            child.printFamilyTree(depth + 1)
