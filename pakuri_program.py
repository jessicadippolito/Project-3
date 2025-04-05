from pakuri import *
from pakudex import *

if __name__ == '__main__':
    obj1 = Pakuri("pukachu")
    pakudex = [obj1]

    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        capacity = input("Enter max capacity of the Pakudex: ")
        if capacity.isnumeric() == False:
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
                array = my_store.get_species_array()
                if array == None:
                    print("Error: No such Pakuri!")
                    continue
                exists = False
                for i in range(0, len(array)):
                    if name == array[i]:
                        print(f"Species: {my_store.my_pakudex[i].species}")
                        print(f"Attack: {my_store.my_pakudex[i].attack}")
                        print(f"Defense: {my_store.my_pakudex[i].defense}")
                        print(f"Speed: {my_store.my_pakudex[i].speed}")
                        exists = True
                if exists == False:
                    print("Error: No such Pakuri!")
                continue
            elif selection == '3':
                if len(my_store.my_pakudex) == int(my_store.capacity):
                    print("Error: Pakudex is full!")
                    continue
                name = input("Enter the name of the species to add: ")
                if my_store.add_pakuri(name):
                    print(f'Pakuri species {name} successfully added!')
                else:
                    print("Error: Pakudex already contains this species!")
                continue
            elif selection == '4':
                name = input("Enter the name of the species to evolve: ")
                array = my_store.get_species_array()
                exists = False
                for i in range(0, len(array)):
                    if name == array[i]:
                        my_store.my_pakudex[i] = Pakuri.evolve(my_store.my_pakudex[i])
                        print(f'{name} has evolved!')
                        exists = True
                if exists == False:
                    print("Error: No such Pakuri!")
                continue
            elif selection == '5':
                my_store.sort_pakuri()
                print("Pakuri have been sorted!")
            elif selection == '6':
                print("Thanks for using Pakudex! Bye!")
                break
            else:
                print("Unrecognized menu selection!")
                continue
        break

