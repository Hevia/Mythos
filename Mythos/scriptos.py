import random as rd
from Grammars import *




# Used to split .txt elements on a new line and append to a list
def file_open(file_name):
    f = open(file_name, 'r')
    data = f.read().split("\n")
    return_list = []
    for i in data:
        return_list.append(i)
    return return_list

adj = file_open("data/characters/adjectives.txt")
nouns = file_open("data/characters/nouns.txt")


def gen_region():
    climates = file_open("data/world/climates.txt")


def creation_myth(god_one, god_two, origin_entity):
    timeline = ["S"]
    timeline = expansion(timeline)

    timeline = expand_agents(timeline, "N", god_one)
    timeline = expand_agents(timeline, "N2", god_two)
    timeline = expand_agents(timeline, "CH", origin_entity)

    timeline = to_string(timeline)
    return timeline

# Our temporary generate society function
def gen_society():
    cultures = file_open("data/world/cultures.txt")
    society = {}
    god_one = gen_name()
    god_two = gen_name()
    origin_entity = Primordial()
    society['name'] = gen_name()
    society['culture'] = rd.choice(cultures)
    society['Creation Myth'] = creation_myth(god_one, god_two, origin_entity.name)
    return society

def gen_culture():
    cultures = file_open("data/world/cultures.txt")
    culture = rd.choice(cultures)
    return culture



def hero_story(pantheon, society):
    hero = Hero(gen_name(), "Hero", rd.choice(adj))
    worshipped_god = rd.choice(pantheon)
    villan_god = rd.choice(pantheon)
    hero.society = society['name']

    # This is currently the hacky way of making sure we don't end up with the same god
    while(villan_god == worshipped_god):
        villan_god = rd.choice(pantheon)

    hero.hates = villan_god.name
    hero.loves = worshipped_god.name

    return hero


def gen_name():
    name = ""
    words = file_open("data/characters/names.txt")
    for i in range(rd.randrange(2, 4)):
        name += rd.choice(words)
        
    return name

def gen_being():
    being = ""
    attributes = ["giant", "huge", "tiny", "", "meek", "strong"]
    beings = ["god", "goddess"]
    being = rd.choice(attributes) + " " + rd.choice(beings)
    return being

def gen_power():
        powers = file_open("data/characters/powers.txt")
        actions = file_open("data/characters/actions.txt")
        the_power = rd.choice(actions) + " " + rd.choice(powers)
        return the_power   




class Character:
    def __init__(self):
        self.name = gen_name()
        self.gender = rd.choice(["god", "goddess"])
        self.adj = rd.choice(adj)
        self.kind = rd.choice(nouns)
        self.power = gen_power()
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

    def printFamilyTree(self, depth):
        for child in self.children:
            for brace in range(depth):
                print(" | ", end="")
            print(child.name)
            child.printFamilyTree(depth + 1)
    
    
class God(Character): 
    def printGod(self):
        print(self.name, "the", self.adj, self.gender,  "has the power to", self.power)

class Hero(Character):
    def __init__(self, name, gender, adj):
            self.name = name
            self.age = 0
            self.gender = gender 
            self.adj = adj
            self.hates = ""
            self.loves = ""
            self.children = []
            self.parents = []
            self.story = ""
            self.society = ""
    
    def print_myth(self):
        print(self.name + " The mighty hero of " + self.society + " bested " +self.hates + " with help from " + self.loves) 



class Society:
    def gen_pantheon(self, gods):
        for i in gods:
            new_god = God()
            new_god.kind = i
            self.pantheon.append(new_god)

    def __init__(self):
        self.name = gen_name()
        self.home = gen_name()
        self.culture = gen_culture()
        self.required_gods = ["Sun", "Moon", "Earth", "Ocean"]
        self.required_holidays = ["sacrifical", "feast", "celebratory"]
        self.pantheon = gen_pantheon(required_gods)
        self.creation_myth = None
        self.holidays = None
    
    def print_society(self):
        print("The " + self.culture + " " + self.name + " people of " self.home)
        print("")