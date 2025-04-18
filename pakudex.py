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
        for i in range (0,len(self.my_pakudex)):
            if species == self.my_pakudex[i].species:
                return [self.my_pakudex[i].attack,self.my_pakudex[i].defense,self.my_pakudex[i].speed]
        return None

    def sort_pakuri(self):
        self.my_pakudex.sort()

    def add_pakuri(self,species):
        new_species = Pakuri(species)
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == new_species.species:
                return False
        self.my_pakudex.append(new_species)
        self.size += 1
        return True

    def evolve_species(self,species):
        for i in range(0,len(self.my_pakudex)):
            if self.my_pakudex[i].species == species:
                self.my_pakudex[i] = Pakuri.evolve(self.my_pakudex[i])
                return True
        return False


