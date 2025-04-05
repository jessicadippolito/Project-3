from pakuri import Pakuri

class Pakudex:
    def __init__(self,capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.my_pakudex = []

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        array = []
        if self.size == 0:
            return None
        else:
            if len(self.my_pakudex) == 0:
                return None
            else:
                for i in range(0,len(self.my_pakudex)):
                    array.append(self.my_pakudex[i].species)
        return array

    def get_stats(self,species):
        if isinstance(self.my_pakudex,list):
            return [self.attack,self.defense,self.speed]
        else:
            return None

    def sort_pakuri(self):
        self.my_pakudex.sort()

    def add_pakuri(self,species):
        if len(self.my_pakudex) == int(self.capacity):
            print("Error: Pakudex is full!")
            return False
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species.species:
                print("Error: Pakudex already contains this species!")
                return False
        self.my_pakudex.append(species)
        print(f'Pakuri species {species.species} successfully added!')
        self.size += 1
        return True

    def evolve_species(self,species):
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species.species:
                each_pakuri = Pakuri.evolve(each_pakuri)
                return True
        return False


