class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self,j):
        for i in range(0,j):
            self.health -= 1
        return self
    def run(self,j):
        for i in range(0,j):
            self.health -= 5
        return self
    def display_all(self):
        print 'I am a', self.name
        print self.health
        return self

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self,j):
        for i in range(0,j):
            self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self,j):
        for i in range(0,j):
            self.health -= 10
        return self
        



animal1 = Animal('monkey')
animal1.walk(3).run(2).display_all()

dog = Dog('dog')
dog.walk(3).run(2).pet(1).display_all()

dragon = Dragon('dragon')
dragon.fly(3).display_all()