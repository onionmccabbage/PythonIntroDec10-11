

class WG():
    '''name (non-empty string) aligment (goodie or baddie) materials (tuple of values) '''
    def __init__(self, n, a, m):  
        self.name = n
        self.align = a
        self.materials = m
    @property
    def name(self):
        return self.__name # generally the get will return the mangled value (__)
    @name.setter
    def name(self, n):
        if type(n)==str and n !='':
            self.__name = n
        else:
            self.__name = 'default' # or we could raise an exception




    def __str__(self):
        return f''  

# exercise the code
wallace = WG('Wallace', 'Goodie', ('plasticene','silicone'))
feathers = WG('Feathers McGraw' ,'Baddie', ('wire', 'silicone'))