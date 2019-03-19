import json
import random as rd
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt


def open_json(file_name):
    with open(file_name) as data_file:
        data = json.load(data_file)
    return data

world_size = 8
world = nx.erdos_renyi_graph(n = world_size, p = 0.5)
nx.draw(world)
plt.show()

print(world.nodes)
node_elements = ['animals', 'vegetation', 'water', 'nature']

def map_world(world_size, world_elements):
    mapping = {0:'center'}

    for i in range(1, world_size):
        mapping[i] = rd.choice(world_elements) + str(i)

    return mapping

mapping = map_world(world_size, node_elements)
print(mapping)
world = nx.relabel_nodes(world, mapping)

print(world.nodes)
