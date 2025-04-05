from pakuri import *
from pakudex import *

if __name__ == '__main__':
    obj1 = Pakuri("pukachu")
    pakudex = [obj1]

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        capacity = int(input("Enter max capacity of the Pakudex: "))
        if type(int(capacity)) != int:
            print("Please enter a valid size.")
            continue
        my_store = Pakudex(capacity)
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
            if selection == "1":
                array = my_store.get_species_array()
                print("Pakuri In Pakudex:")
                for i in range(0,len(array)):
                    print(f'{i+1}. {array[i]}')
                continue
            elif selection == '2':
                name = input("Enter the name of the species to display: ")
                species = Pakuri(name)
                if isinstance(species, Pakudex) == False:
                    print("Error: No such Pakuri!")
                else:
                    print(f"Species: {Pakuri.get_species(species)}")
                    print(f"Attack: {Pakuri.get_attack(species)}")
                    print(f"Defense: {Pakuri.get_defense(species)}")
                    print(f"Speed: {Pakuri.get_speed(species)}")
                continue
            elif selection == '3':
                name = input("Enter the name of the species to add: ")
                species = Pakuri(name)
                my_store.add_pakuri(species)
                continue
            elif selection == '4':
                name = input("Enter the name of the species to evolve: ")
                species = Pakuri(name)
                array = my_store.get_species_array()
                exists = False
                for i in range(0, len(array)):
                    if name == array[i]:
                        species = Pakuri.evolve(species)
                        print(f'{name} has evolved!')
                        exists = True
                if exists == False:
                    print("Error: No such Pakuri!")
                continue
            elif selection == '6':
                print("Thanks for using Pakudex! Bye!")
                break
            else:
                print("Unrecognized menu selection!")
                continue

