class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Emma', 23)
p2 = Person('Omar', 34)

print("P1's name is " + p1.name + " and their age is " + str(p1.age))
print("P2's name is " + p2.name + " and their age is " + str(p2.age))

