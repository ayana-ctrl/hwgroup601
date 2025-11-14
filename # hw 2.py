# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 

# p1= Person('Alice', 25)
# print(p1.name)
# print(p1.age)

# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age = age 

#     def greet(self):
#         print(f'Привет меня зовут {self.name}, мне {self.age} лет')

# p2 = Person('Bob', 30)
# p2.greet()

# class Car:
#     def __init__(self, brand = 'Toyota', year = 2020):
#         self.brand = brand 
#         self.year = year 

# c1= Car()
# c2= Car('Honda', 2019)
# print(c1.brand , c1.year)
# print(c2.brand , c2. year)

#  самостоятельное задание :
# class Pet:
#     def __init__(self, type , name):
#         self.type = type 
#         self.name = name 


#     def describe(self):
#       print(f' привет, у меня есть вид {self.type},его зовут {self.name}')
      
#     def speak(self):
#        if type:
#           make_sound = 'гав-гав'
#           return dog
#        if type:
#           make_sound = 'мяу-мяу'
#           return cat 
#        else:
#           print('другой вид животного')



# p1 = Pet('собака', 'саша')
# p1.describe()
# p1.speak()  

# p2 = Pet ('кошка', 'люмиэр')
# p2.describe()
# p2.speak()

# правильный вариант 
# class Pet:
#     def __init__(self, type, name):
#         self.type = type 
#         self.name = name 

#     def describe(self):
#         print(f' Привет, у меня есть {self.type}, его зовут {self.name} ')

    
#     def speak(self):
#         if self.type.lower == 'собака':
#             print('гав-гав')
#         elif self.type.lower == 'кошка':
#             print('мяу-мяу')
#         else:
#             print('это другое животное')



# p1 = Pet ('собака', 'итер')
# p1.describe()
# p1.speak()

# p2 = Pet('кошка', 'люмиэр')
# p2.describe()
# p2.speak()

from datetime import datetime

class Book:
    def __init__(self, title, author, year):
        self.title = title 
        self.author = author
        self.year = year 

    
    def describe(self):
        print(f' Книга {self.title}, написано {self.author}, в {self.year} году ')

    def age(self):
        curent_year = datetime.now().year
        return curent_year - self.year

b1 = Book('Мастер и Маргарита', 'Булгакова', 1961)
b1.describe
print('возраст книги', (b1.age))
