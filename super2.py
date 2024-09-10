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
    def __init__(self, **kwargs):              #accept unknown number of positional arguments
        super().__init__(**kwargs)            #forward positional arguments to base/super class

kukku = Cathedral(type_of='tea',name="teapoint")  #have to use keywords now
kukku.info()