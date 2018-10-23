import random as rd
from scriptos import *

# 
rules = {
    "S":[ 
        ["The", "World", "began","when", "the", "NU", "V", "from", "a", "B"] 
    ], 
    "NU":[ 
        ["Adj","N"],
        ["Adj","N"],
        ["Adj","N"]
    ],
    "V":[ 
        ["hatched"],
        ["birthed"],
        ["crawled"]
    ],
    "Adj": [
        ["Giant"],
        ["Great"],
        ["Beautiul"]
    ],
    "B": [
        ["egg"],
        ["crack in the void"]
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


def to_string(result):
    return ' '.join(result)


# An example test you can run to see it at work
result = ["S"]
print(result) # Print our starting result
result = expansion(result) # Expand our starting list 
final = to_string(result)
print(final) # Print the final result

    