from random import *
from scriptos import * 



def main():
    #Imports .txt files for the nouns and adjectives to determine god hood and stuff
    nouns = file_open("data/allNouns.txt")
    adj = file_open("data/allAdj.txt")
    pantheon = []
    timeline = creation_myth()
    user_input = ""

    print("Welcome to Mythos! Mythology generation at your fingertips!")
    print("[g] - generate gods, [c] - generate creation myth, [e] - exit")

    user_input = input("Enter in a command to get started: ")

    while(user_input != 'e'):

        if user_input == 'g':
            pantheon = []
            for i in range(5):
                pantheon.append(Character(gen_name(), gen_being(), randrange(0, 5999), choice(nouns), choice(adj), gen_power()))

            for i in pantheon:
                i.printGod()
        
        if user_input == 'c':
            timeline = ""
            timeline = creation_myth()
            print(timeline)

        user_input = input("Enter another input: ")




if __name__ == "__main__":
    main()