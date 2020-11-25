class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.dict1 = {"wage": wage, "bonus": bonus}
        self._income = self.dict1["wage"] + self.dict1["bonus"]

class Position(Worker):
    def get_full_name(self):
       return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income
    
posit = Position("Albert", "Furmanov", "director", 350000, 75000)
print(posit.get_full_name())
print(posit.get_total_income())

