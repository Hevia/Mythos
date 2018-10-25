import random as rd
from scriptos import * 



def main():
    # Imports .txt files for the nouns and adjectives to determine god hood and stuff
    
    adj = file_open("data/characters/adjectives.txt")
    pantheon = []
    society = {}
    user_input = ""

    print("Welcome to Mythos! Mythology generation at your fingertips!")
    print("[g] - generate gods,  [s] - society")
    print("[h] - hero story, , [e] - exit")

    user_input = input("Enter in a command to get started: ")

    while(user_input != 'e'):

        if user_input == 'g':
            pantheon = []
            for i in range(5):
                pantheon.append(God())

            for i in pantheon:
                i.printGod()

        elif user_input == 's':
            society = gen_society()
            print(society)

        elif user_input == 'h':
            hero = hero_story(pantheon, society)
            hero.print_myth()


        user_input = input("Enter another input: ")




if __name__ == "__main__":
    main()