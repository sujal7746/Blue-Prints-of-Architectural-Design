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
        self.number_of_bells = 10
        def ring_bell(self, bell= 1):   #add new method
            print('ringing bell number {}'.format(bell))
        def info(self):         #overwrite base class method
            super().info()         #CALL METHOD IN BASE CLASS
            self.ring_bell()    #add new method call
kukku = Cathedral(type_of='tea',name="teapoint")  #argument pass by name
kukku.info()