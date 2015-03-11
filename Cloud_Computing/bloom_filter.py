class BloomFilter:
    def __init__(self):
        self.m = 32
        self.filter = [0 for x in range(self.m)]

    def add_element(self, x):
        h1 = ((x**2 + x**3))%self.m
        h2 = ((x**2 + x**3)*2)%self.m
        h3 = ((x**2 + x**3)*3)%self.m
        self.filter[h1] = 1
        self.filter[h2] = 1
        self.filter[h3] = 1

    def check_element(self, x):       
        h1 = ((x**2 + x**3))%self.m
        h2 = ((x**2 + x**3)*2)%self.m
        h3 = ((x**2 + x**3)*3)%self.m
        return self.filter[h1] == 1 and self.filter[h2] == 1 and self.filter[h3] == 1