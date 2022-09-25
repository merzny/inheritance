class Person:
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
    def info(self):
        print('Parent class')
        print(self)
class Doctor(Person):
    def __init__(self,name,surname,age):
        super().__init__(name,surname)
        self.age=age
    def __str__(self):
        return f'Doctor {self.name} {self.surname}'
d=Doctor('Jack','Horn',35)
d.info()
