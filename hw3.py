class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

def introduction(self):
        if self.__higher_education:
            education_status = 'имею'
        else:
            education_status = 'не имею'

            print(f'Здравствуйте! Меня зовут {self.name}, я родился(ась) в {self.birth_date},' 
              f'моя профессия — {self.occupation}, высшее образование {education_status}.')
        


class Classmate(Person):
     def __init__(self, name, birth_date, occupation, higher_education, group_name):
      super().__init__(name, birth_date, occupation, higher_education) 
      self.group_name=group_name
 
     def introduction(self):
          if self.__higher_education:
            education_status = 'имею'
          else:
           education_status = 'не имею'

          print(f'Привет меня зовут {self.name}. Моя профессия {self.occupation}',
          f'я учился c Шоном в группе {self.group_name}, высшее образование я {education_status}')



class Friend(Person):
    def __init__(self,name,birth_date,occupation,higher_education, hobby):
     super().__init__(name, birth_date, occupation, higher_education) 
     self.hobby= hobby

    def introduction(self):
          if self.__higher_education:
            education_status = 'имею'
          else:
            education_status = 'не имею'

          print(f'Привет меня зовут {self.name}. Моя профессия {self.occupation}',
         f'Моя хобби{self.hobby}. Высшее образование я {education_status}')



classmate_1= Classmate('Ада','1832.12.17','пианистка','False', '601' )
classmate_2 = Classmate ('Карло', '1833.05.13', 'пианист', 'False', '601')
    
friend_1= Friend('Аиша', '1832.12.17', 'хирург', 'True', 'чтение')  #Ада-Аиша близнецы поэтому одно день рождение
friend_2 = Friend ('Карло', '1835.08.06', 'художник', 'False', 'рисовать')

classmate_1.introduction()
classmate_2.introduction()
friend_1.introduction()
friend_2.introduction()