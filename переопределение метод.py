class Person:
    def __init__(self,name):
        self.name=name
    def breathe(self):
        print('Человек дышит')
    def walk(self):
        print("Человек идет")
    def combo(self):
        self.breathe()
        self.walk()
    def __str__(self):
        return f'Person {self.name}'
class Doctor(Person):
    def breathe(self):
        print(f"Доктор дышит")
    def __str__(self):
        return f"Doctor {self.name}"
p=Person('Jon')
d=Doctor('Ray')
p.combo()
d.combo()

