import random as rd
import json
from Grammars import *
import networkx as nx
import matplotlib.pyplot as plt

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

# This is the 'master' function we call 
def gen_society():
    adj = file_open("data/characters/adjectives.txt")
    nouns = file_open("data/characters/nouns.txt")
    world_data = open_json('data/World_Master.json')
    cultures = open_json('data/cultures.json')
    
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


# The world is represented using a Graph database which agents navigate
class World:
    def __init__(self, world_elements, mapping = {0:'center'}, world_size = 8):
        self.size = world_size
        self.elements = world_elements
        self.mapping = mapping
        self.world = self.create_world() # call a function
    
    # We map the "locations" in the world to a dictonary 
    # We need this dictonary to relabel the graph's nodes later
    def map_world(self):
        for i in range(len(self.mapping), self.size):
            self.mapping[i] = rd.choice(self.elements) + str(i)

    # We use this to init our graph
    # We also relabel the nodes from numbers to locations
    def create_world(self):
        self.map_world()
        world = nx.erdos_renyi_graph(n = self.size, p = 0.5)
        world = nx.relabel_nodes(world, self.mapping)
        return world

    def print_world(self):
        print(self.world.nodes)
        nx.draw(self.world)
        plt.show()



class Agent:
    def __init__(self, hunting = 1, foraging = 1, religious = 1, ritualistic = 1):
        self.hunting = hunting
        self.foraging = foraging
        self.religious = religious
        self.ritualistic = ritualistic

    def __str__(self):
        pass

class Hunters(Agent):
    def __init__(self, hunting = 1, foraging = 1, religious = 1, ritualistic = 1, ability = 0.5):
        super().__init__(hunting, foraging, religious, ritualistic)
        self.ability = ability

# Our Society class
class Society:
    def __init__(self, data, culture):
        self.name = gen_name() 
        self.climate = data['name']
        self.culture = culture
        self.pantheon = [] 

    def __repr__(self):
        print("Society(name: {}, climate: {}, culture: {}, pantheon: {})".format(self.name, self.climate, self.culture, self.pantheon))

    def __str__(self):
        pass

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


# Testing ground
node_elements = ['animals', 'vegetation', 'water', 'nature']
graph = World(node_elements)
graph.print_world()