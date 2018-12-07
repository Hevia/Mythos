import random as rd
from scriptos import * 



def main():
    # Imports .txt files for the nouns and adjectives to determine god hood and stuff
    
    adj = file_open("data/characters/adjectives.txt")
    pantheon = []
    society = None
    society = gen_society()
    user_input = ""
    test = ""
    test_gods = ["Sun", "Moon", "Earth", "Ocean"]

    print("Welcome to Mythos! Mythology generation at your fingertips!")
    print("[g] - generate gods,  [s] - society")
    print("[h] - troubleshooting, , [e] - exit")

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
            society.print_society()

        elif user_input == 'h':
            test = gen_homeland()
            print(test)


        user_input = input("Enter another input: ")




if __name__ == "__main__":
    main()