import random as rd
import json
from Grammars import *
import networkx as nx

# Used to split .txt elements on a new line and append to a list
def file_open(file_name):
    f = open(file_name, 'r')
    data = f.read().split("\n")
    return_list = []
    for i in data:
        return_list.append(i)
    return return_list

# Use this to read our JSON files for general world data
def open_json(file_name):
    with open(file_name) as data_file:
        data = json.load(data_file)
    return data

# Open files for generations
adj = file_open("data/characters/adjectives.txt")
nouns = file_open("data/characters/nouns.txt")
world_data = open_json('data/World_Master.json')
cultures = open_json('data/cultures.json')


# This is the 'master' function we call 
def gen_society():
    
    # This is what we will use to populate data for our society
    data = rd.choice(world_data['Ecosystems'])
    culture = rd.choice(cultures)
    new_society = Society(data, culture)
    return new_society


def gen_name():
    name = ""
    words = file_open("data/characters/names.txt")
    for i in range(rd.randrange(2, 3)):
        name += rd.choice(words)
    return name


class World:
    def __init__(self, world_size = 8, world_elements, mapping = {0:'center'}):
        self.size = world_size
        self.elements = world_elements
        self.mapping = mapping
        self.world = None # call a function
        
    def create_world(self):
        world = nx.erdos_renyi_graph(n = self.world_size, p = 0.5)

    def map_world(self):
        for i in range(len(self.mapping), self.world_size):
            self.mapping[i] = rd.choice(self.world_elements) + str(i)



class Agent:
    def __init__(self, hunting = 1, foraging = 1, religious = 1, ritualistic = 1):
        self.hunting = hunting
        self.foraging = foraging
        self.religious = religious
        self.ritualistic = ritualistic

# Our Society class
class Society:
    def __init__(self, data = None, culture):
        self.name = gen_name() 
        self.climate = data['name']
        self.culture = culture
        self.pantheon = [] 

    def print_pantheon(self):
        for i in self.pantheon:
            i.printGod()
    
    def print_society(self):
        print("------------------------------------------------------")
        print("The " + self.culture + " " + self.name)
        print("------------------------------------------------------")
        self.print_pantheon()
        print("------------------------------------------------------")
        print("\n")

    

class Character:
    def __init__(self):
        self.name = gen_name()
        self.gender = ""
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