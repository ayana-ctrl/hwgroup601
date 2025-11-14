class Animal:
    def __init__(self, name, age):
        self.__name= name 
        self.__age= age 

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

class Dog(Animal):
   def make_sound(self):
      print(f'{self.make_sound} издает звук "гаф-гаф" ')

class Cat(Animal):
   def make_sound(self):
      print(f'{self.make_sound} издает звук "мяу-мяу" ')


dog = Dog ('Саша', 2)
cat = Cat('Алекс', 3)

dog.make_sound()
cat.make_sound()

dog.set_name('Снежок')
dog.set_age(1)

cat.set_name('Люмиер')
cat.set_age(5)

print(f'{dog.get_name} is {dog.get_age} years old')
print(f'{cat.get_name} is {cat.get_age} years old')