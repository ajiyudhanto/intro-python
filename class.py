class Person:
    def __init__(self, name):
        self.name = name
    
    def talk (self):
        print('i am ' + self.name)


person = Person('aji')

person.talk()
print(person.name)

class Male(Person):
    def hair (self):
        print('short hair')


class Female(Person):
    def hair (self):
        print('long hair')

male1 = Male('AJI')
print(male1.hair())