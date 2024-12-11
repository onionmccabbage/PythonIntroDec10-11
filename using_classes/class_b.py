

class WG():
    '''name (non-empty string) aligment (goodie or baddie) materials (tuple of values) '''
    __slots__ = ['__name', '__align', '__materials']
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
    @property
    def align(self):
        return self.__align
    @align.setter
    def align(self, a):
        # check the lower-case version of the text
        if type(a)==str and a.lower() in ('goodie', 'baddie'):
            self.__align = a
        else:
            self.__align = 'goodie' # sensible default
    @property
    def materials(self):
        return self.__materials
    @materials.setter
    def materials(self, m):
        if type(m)==tuple:
            self.__materials = m
        else:
            self.__materials = ('plasticene')
    def __str__(self):
        # construct a string containing all the materials
        s = ''
        for m in self.__materials:
            s += f'\t{m}\n'
        return f'''{self.name} is a {self.align}\n{s}'''

# exercise the code
wallace = WG('Wallace', 'Goodie', ('plasticene','silicone'))
feathers = WG('Feathers McGraw' ,'Baddie', ('wire', 'silicone'))
print(wallace)
print(feathers)