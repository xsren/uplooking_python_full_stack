class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


if __name__ == '__main__':
    dog = Dog()
    dog.run()

    cat = Cat()
    cat.run()
