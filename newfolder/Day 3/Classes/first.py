class Car:
    def __init__(self,wheels,make,model):
        self._wheels = wheels
        self._make = make
        self._model = model
        self._owned = True

    def get_make(self):
        return self._make

car1 = Car(4,"Ford")
# print(car1)
# print(car1.get_make())
# print(car1._wheels)