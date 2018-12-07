import random as rd
import json
from Grammars import *

# Used to split .txt elements on a new line and append to a list
def file_open(file_name):
    f = open(file_name, 'r')
    data = f.read().split("\n")
    return_list = []
    for i in data:
        return_list.append(i)
    return return_list

# Used during the generation process
adj = file_open("data/characters/adjectives.txt")
nouns = file_open("data/characters/nouns.txt")
creatures = file_open("data/creatures.txt")

def gen_creatures():
    creatures_list = []
    name = ""

    for i in range(rd.randrange(3, 6)):
        name += rd.choice(adj)
        name += " "
        name += rd.choice(creatures)
        creatures_list.append(name)
        name = ""
    
    return creatures_list

def gen_society():
    with open('data/World_Master.json') as data_file:
        world_master = json.load(data_file)

    # This is what we will use to populate data for our society
    data = rd.choice(world_master['Ecosystems'])
    creatures = gen_creatures()
    
    new_society = Society(data, creatures)
    new_society.pantheon = gen_pantheon(new_society.pantheon, new_society.required_gods)
    return new_society


def creation_myth(god_one, god_two, origin_entity):
    timeline = ["S"]
    timeline = expansion(timeline)

    timeline = expand_agents(timeline, "N", god_one)
    timeline = expand_agents(timeline, "N2", god_two)
    timeline = expand_agents(timeline, "CH", origin_entity)

    timeline = to_string(timeline)
    return timeline


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
    for i in range(rd.randrange(2, 3)):
        name += rd.choice(words)
    return name


def gen_region():
    climates = file_open("data/world/climates.txt")
    region = ""
    region += rd.choice(climates)
    region += " "
    words = file_open("data/characters/names.txt")
    for i in range(rd.randrange(2, 3)):
        region += rd.choice(words)
    return region


def gen_homeland():
    region = ""
    words = file_open("data/characters/names.txt")
    for i in range(rd.randrange(2, 3)):
        region += rd.choice(words)
    return region



def gen_being():
    being = ""
    attributes = ["giant", "huge", "tiny", "", "meek", "strong"]
    beings = ["god", "goddess"]
    being = rd.choice(attributes) + " " + rd.choice(beings)
    return being


# No longer needed but will leave it here in case
def gen_power():
        powers = file_open("data/characters/powers.txt")
        actions = file_open("data/characters/actions.txt")
        the_power = rd.choice(actions) + " " + rd.choice(powers)
        return the_power   




class Character:
    def __init__(self):
        self.name = gen_name()
        self.gender = rd.choice(["god", "goddess"])
        self.kind = None
        self.adj = rd.choice(adj)
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
        print(self.name + " the " + self.adj + " " + self.gender + " of the " + self.kind)

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


test_gods = ["Sun", "Moon", "Earth", "Ocean"]

# We use this to add or create new pantheons based on whatever list we throw at it
def gen_pantheon(pantheon, gods):
        for i in gods:
            new_god = God()
            new_god.kind = i
            pantheon.append(new_god)
        return pantheon

class Society:
    def __init__(self, data = None, creatures = None):
        self.name = gen_name() 
        self.climate = data['name']
        self.culture = gen_culture()
        self.required_gods = data['Required_Gods']
        self.required_holidays = data['Required_Holidays']
        self.pantheon = []
        self.creatures = creatures
        self.creation_myth = None

    def print_pantheon(self):
        for i in self.pantheon:
            i.printGod()

    def print_creatures(self):
        for i in self.creatures:
            print(i)
    
    def print_society(self):
        print("------------------------------------------------------")
        print("The " + self.culture + " " + self.name + " of the " + self.climate)
        print("------------------------------------------------------")
        self.print_pantheon()
        print("------------------------------------------------------")
        self.print_creatures()
        print("------------------------------------------------------")
        print("\n")

    

    