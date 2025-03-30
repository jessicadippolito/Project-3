from pakuri import *

if __name__ == '__main__':
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = input("Enter max capacity of the Pakudex: ")
    if type(int(capacity)) != int:
        print("Please enter a valid size.")
        capacity = input("Enter max capacity of the Pakudex: ")
    print(f'The Pakudex can hold {capacity} species of Pakuri.')
    while True:
        print()
        print("Pakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")
        print()
        selection = input("What would you like to do? ")
        if selection == '2':
            name = input("Enter the name of the species to display: ")
            species = Pakuri(name)
            if species not in Pakuri:
                print("Error: No such Pakuri!")
            else:
                print(f"Species: {Pakuri.get_species(species)}")
                print(f"Attack: {Pakuri.get_attack(species)}")
                print(f"Defense: {Pakuri.get_defense(species)}")
                print(f"Speed: {Pakuri.get_speec(species)}")
        if selection == '6':
            print("Thanks for using Pakudex! Bye!")
            break
