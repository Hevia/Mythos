import random as rd

# Used to split .txt elements on a new line and append to a list
def file_open(file_name):
    f = open(file_name, 'r')
    data = f.read().split("\n")
    return_list = []
    for i in data:
        return_list.append(i)
    return return_list

adj = file_open("data/characters/adjectives.txt")


def gen_region():
    climates = file_open("data/world/climates.txt")

def gen_society():
    cultures = file_open("data/world/cultures.txt")
    society = {}
    society['name'] = gen_name()
    society['culture'] = rd.choice(cultures)

    return society


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







def creation_myth():
    #0 - for egg origin
    #1 - for ex nihilo (God created the world out of nothing)
    #2 - Creation from chaos(expanse, void, abyss, disorder, primordial substance)
    #3 - World parent gods (Gods mating)
    #4 - World parent from a single god (The gods corpse or body gives life to the world)
    timeline = ""
    rand = rd.randrange(0, 4) 
    egg_birth_nouns = ["hatched", "birthed", "constructed"]
    egg_birth_objects = ["Egg", "Ball", "Skeleton"]
    egg_origin_templates = ["Time began when our universe was", "The universe as we know it was", "In nothingness our world was"]
    birth_obj = ""

    if rand == 0: 
        birth_method = rd.choice(egg_birth_nouns)
        origin_method = rd.choice(egg_origin_templates)
        birth_obj = rd.choice(adj) + ' '  + rd.choice(egg_birth_objects)
        timeline += (f"{origin_method} {birth_method} from a {birth_obj}")

    elif rand == 1:
        birth_method = rd.choice(egg_birth_nouns)
        origin_method = rd.choice(egg_origin_templates)
        birth_obj = "Empty"
        timeline += (f"{origin_method} {birth_method} from a {birth_obj}")


    return timeline




def gen_name():
    name = ""
    words = ["que", "way", "eel", "ruu", "tish", "yar", "uub", "iek", "oy", "pe", "ah", "sha", "dor", "feek", "goo", "moo", "rabi", "doku", "baca", "szum", "lan", "ski", "-", "-"]
    for i in range(rd.randrange(2, 3)):
        name += rd.choice(words)
        
    return name

def gen_power():
    powers = file_open("data/characters/powers.txt")
    actions = file_open("data/characters/actions.txt")
    the_power = rd.choice(actions) + " " + rd.choice(powers)

    return the_power   

def gen_being():
    being = ""
    attributes = ["giant", "huge", "tiny", "", "meek", "strong"]
    beings = ["god", "goddess"]
    being = rd.choice(attributes) + " " + rd.choice(beings)
    return being



class Character:
    def __init__(self, name, gender, age, kind, adj, power):
        self.name = name
        self.age = age
        self.gender = gender 
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

    def printFamilyTree(self, depth):
        for child in self.children:
            for brace in range(depth):
                print(" | ", end="")
            print(child.name)
            child.printFamilyTree(depth + 1)


class God(Character): 
    def printGod(self):
        print(self.name, "the", self.adj, self.age, "year old", self.gender, "of", self.kind, "has the power to", self.power)

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