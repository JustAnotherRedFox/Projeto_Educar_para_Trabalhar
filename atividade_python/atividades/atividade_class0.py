class Person:
    #constructor method
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

#instantiating object
regis = Person('Regis')
print(regis)

fabio = Person('Fabio')
print(fabio)
