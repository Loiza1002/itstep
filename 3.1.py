class Human:
    def __int__(self, name="Human"):
        self.name = name

class Auto:
    def __int__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)


    def print_passengers(self):
        if self.passengers != []:
            print(f"Name of {self.brand}) passengers:")
            for passengers in self.passengers:
                print(passengers.name)

        else: print(f"There are not  passengers in {self.brand}")

audi = Auto("AUDI")

nick = Human("Nick")
anna = Human("Anna")

audi.add_passenger(nick)

audi.print_passengers()