from person import Person

class Employee(Person):
    def __init__(self,name,dep):
        super().__init__(name)
        self._dep = dep

