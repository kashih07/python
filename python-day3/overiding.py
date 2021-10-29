class Animal:
    def __init__(self):
        print("from animal")
class Dog(Animal):
    def __init__(self):
        print("from dog..")
    def talk(self):
        print("bowww")
class Cat(Animal):
    def __init__(self):
        print("from cat..")
    def talk(self):
        print("meoww")
"""if __name__ == '__main__':
    a = Animal()
    c=Cat()
    a=c
    a.talk()
    Dog().talk()"""