from random import randint, randrange

def genName():
    name = ""
    words = ["que", "way", "eel", "ruu", "tish", "yar", "uub", "iek", "oy", "pe", "ah", "sha", "dor", "feek", "goo", "moo", "rabi", "doku", "baca", "szum", "lan", "ski", "-", "-"]
    rando = randrange(0, (len(words)-1))
    for i in range(randrange(2, 3)):
        rando = randrange(0, (len(words)-1))
        name += words[rando]
        
    return name


def genPower(powers, actions):
    power = ""
    randoP = randrange(0, (len(powers)-1))
    randoA = randrange(0, (len(actions)-1))
    power += actions[randoA]
    power += " "
    power += powers[randoP]

    return power   

def genBeing():
    being = ""
    attributes = ["giant", "huge", "tiny", ""]
    beings = ["god", "goddess", "centaur", "giant", "hero", "herorine", "elf", "fairy", "sphinx", "wyvern", "dragon", "cerberus", "minotaur", "chimera"]
    rando = randrange(0, len(beings)-1)
    randoA = randrange(0, len(attributes)-1)

    being += " " + beings[rando]
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

# class Religion:
#     def __init__(self, name, age, kind):
#         self.gods = {}
#         self.age = age
#         self.name = name
#         self.kind = kind
#         self.supreme = None

#     def addGod(self, name, age, kind, adj, power, worship, parents=None):
#         self.gods[name] = God(name, age, kind, adj, power, worship)

#         if parents is None:
#             self.supreme = self.gods[name]
#         else:
#             for parent in parents:
#                 try:
#                     self.gods[parent].setChild(self.gods[name])
#                 except KeyError:
#                     print("Parents don't exist")

#     def getGod(self, name):
#         try:
#             return self.gods[name]
#         except KeyError:
#             return None

#     def printHeirarchy(self):
#         print("The Heirarchy of {0}".format(self.name))

#         print(self.supreme.name)
#         self.supreme.printFamilyTree(1)