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

    f.close()
    return return_list

# Use this to read our JSON files for general world data
def open_json(file_name):
    with open(file_name) as data_file:
        data = json.load(data_file)
    return data



def parse_seasons():
    year = []
    season_data = open_json('data/Seasons.json')

    for j in range(0, len(season_data["Seasons"])):
        year.append(Season(
            season_data["Seasons"][j]["name"],
            season_data["Seasons"][j]["climate"],
            season_data["Seasons"][j]["animals"],        
            season_data["Seasons"][j]["plants"]
        ))
    
    return year
   
def parse_culture(food_stock, population, delta):
    cultures = open_json('data/cultures.json')
    cultures = rd.choice(cultures["Cultures"])

    new_society = Society(cultures["name"], food_stock, population)

    start_agent = Agent(
        cultures["Hunting"],
        cultures["Foraging"],
        cultures["Religious"],
        cultures["Rituals"],
        delta
    )

    new_society.set_agents(start_agent)
    
    return new_society

    

# This is the 'master' function we call 
# it calls all other needed for world creation
def gen_society(food_stock, population, delta):
    # init the seasons
    # Myths are generated each seasonal period over the course of a year
    year = parse_seasons()

    # init the world
    node_elements = ['animals', 'vegetation', 'water', 'nature']
    world_graph = World(node_elements)

    # init the society and the agents
    society = parse_culture(food_stock, population, delta)

    


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
    def __init__(self, hunting = 1, foraging = 1, religious = 1, ritual = 1, delta = 0.5):
        self.hunting = hunting
        self.foraging = foraging
        self.religious = religious
        self.ritual = ritual
        self.delta = delta

    def __str__(self):
        pass

class Hunters(Agent):
    def __init__(self, hunting = 1, foraging = 1, 
    religious = 1, ritual = 1, delta = 0.5, ability = 0.5):
        super().__init__(hunting, foraging, religious, ritual, delta)
        self.ability = ability


class Season:
    def __init__(self, name, climate = 1, animals = 1, plants = 1):
        self.name = name
        self.climate = climate
        self.animals = animals
        self.plants = plants

# Our Society class
class Society:
    def __init__(self, culture, food_stock, population):
        self.name = gen_name() 
        self.culture = culture
        self.pantheon = [] 
        self.food_stock = food_stock
        self.population = population
        self.agents = []

    def set_agents(self, agents):
        self.agents.append(agents)

    def decision_sequence(self, agents):
        pass

    def __repr__(self):
        print("Society(name: {},  culture: {}, pantheon: {})".format(self.name, self.culture, self.pantheon))

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

    
# Mainly used to encapsulate data for storytelling
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
# node_elements = ['animals', 'vegetation', 'water', 'nature']
# graph = World(node_elements)
# graph.print_world()


def main():
    parse_culture(100, 100, 100)


if __name__ == "__main__":
    main()
