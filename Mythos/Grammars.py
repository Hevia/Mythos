import random as rd
from scriptos import *


rules = {
    # Our world creation rules
    "S":[ 
        ["The", "World", "began","when", "NU", "V", "from", "a", "B"], # for egg origin 
        ["Legend", "has", "it", "that", "N", "and", "N2", "gave", "rise", "to", "our", "world"], # World parent gods (Gods mating)
        ["From", "the", "CH", "gave", "rise", "to", "N", "who", "created", "our", "world"], # Creation from chaos(expanse, void, abyss, disorder, primordial substance)
        ["From", "the", "BO", "of", "N", "V", "our", "world"] # Creation from a single parent
    ], 
    "NU":[ 
        ["N"],
        ["the","Adj","N"]
    ],
    "V":[ 
        ["hatched"],
        ["birthed"],
        ["crawled"]
    ],
    "Adj": [
        ["giant"],
        ["great"],
        ["beautiul"]
    ],
    "B": [
        ["egg"],
        ["crack in the void"]
    ],
    "BO":[
        ["forehead"],
        ["arm"],
        ["tail"],
        ["stomach"]
    ],

    # Our hero story genereation rules
    "HS":
    [
        [""]
    ]
}


# Used to parse any list of strings and insert them in place in a list 
def generate_items(items):
    for item in items:
        if isinstance(item, list):
            for subitem in generate_items(item):
                yield subitem
        else:
            yield item       

# Our expansion algo
def expansion(start):
    for element in start:
        if element in rules:
            loc = start.index(element)
            start[loc] = rd.choice(rules[element])
        result = [item for item in generate_items(start)]

    for item in result:
        if not isinstance(item, list):
            if item in rules:
                result = expansion(result)
    
    return result

def expand_agents(start, agent, agent_name):
    for element in start:
        if element == agent:
            loc = start.index(element)
            start[loc] = agent_name
        result = [item for item in generate_items(start)]

    return result



def to_string(result):
    return ' '.join(result)


class Primordial:
    def __init__(self):
        self.name = rd.choice(["chaos", "void", "stardust"])

    