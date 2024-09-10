# Inheritance: 'is-a'
# Composition: 'has-a'
class Engine():
    def __init__(self, engine_type= '[unknown]'):
        self.engine_type = engine_type
class Vehicle():
    def __init__(self, seats=1):
        self.num_of_seats = seats
class Airplane(Vehicle):  #airplane is a vehicle
    def __init__(self, model, engine, seats =1):
        super().__init__(seats)
        self.airplane_model = model
        self.airplane_engine = Engine(engine)  #airplane has an engine

    def airplane_info(self):
        print('{} with \n{} type of engine and \n {} passenger seats\n' .\
              format(self.airplane_model,
              self.airplane_engine.engine_type,
              self.num_of_seats))

boing = Airplane(model="tata", engine="bump", seats=11)
airbus = Airplane(model="hero",engine="honda", seats=15)

for plane in (boing, airbus):
    plane.airplane_info()
