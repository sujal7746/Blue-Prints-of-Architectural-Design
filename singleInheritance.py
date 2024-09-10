#singleInheritance

class Building():
    def __init__(self, type_of, name):
        self.type_of_building = type_of
        self.name_of_building = name

    def build(self):
        print('building a {}'.format(self.type_of_building))
    def visit(self):
        print('Welcome to {}'.format(self.name_of_building))
    def info(self):
        return self.visit(), self.build()

class Cathedral(Building):
    pass
class Cafe(Building):
    pass

manohar = Cathedral('cathedral', 'Sitam Thakur')
manohar.info()
print()
Cafe('Cafe', "ria").info()