class Pakudex:
    def __init__(self,capacity = 20):
        self.capacity = capacity
        self.size = 0
        self.my_pakudex = []

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity


    def add_pakuri(self,species):
        if self.size == self.capacity:
            return False
        for each_pakuri in self.my_pakudex:
            if each_pakuri.get_species() == species:
                return False
        self.my_pakudex.append(Pakuri(species))
        self.size += 1
        return True
