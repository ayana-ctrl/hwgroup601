class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

def introduction(self):
        if self.higher_education:
            education_status = 'имею'
        else:
            education_status = 'не имею'

        print(f'Здравствуйте! Меня зовут {self.name}, я родился(ась) в {self.birth_date}, моя профессия — {self.occupation}, высшее образование {education_status}.')
        
class Classmate(Person):
     def __init__(self, name, birth_date, occupation, higher_education, group_name):
      super().__init__(name, birth_date, occupation, higher_education) 
      self.group_name=group_name
 
     def introduction(self):
         self.introduction()
         
class Friend(Person):
    def __init__(self,name,birth_date,occupation,higher_education, hobby):
        self.hobby= hobby

    def introduction(self):
        self.introduction()

classmate_1= Classmate('Ада','1832.12.17','пианистка','False', '601' )
classmate_2 = Classmate ('Карло', '1833.05.13', 'пианист', 'False', '601')
    
friend_1= Friend('Аиша', '1832.12.17', 'хирург', 'True', 'чтение')  #Ада-Аиша близнецы поэтому одно день рождение
friend_2 = Friend ('Карло', '1835.08.06', 'художник', 'False', 'рисовать')

classmate_1.introduction() # не уверенна корректно ли 
print(f'Привет я одноклассница Шона меня зовут {classmate_1.name}, я родилась в {classmate_1.birth_date},'
      f' моя профессия {classmate_1.occupation},высшее образование я {classmate_1.higher_education}, я учусь в группе {classmate_1.group_name} \n')
classmate_2.introduction()
print(f'Привет я одноклассник Шона меня зовут {classmate_2.name}, я родился в {classmate_2.birth_date}, '
      f'моя профессия {classmate_2.occupation},высшее образование я {classmate_2.higher_education}, я учусь в группе {classmate_2.group_name}\n ')

friend_1.introduction()
print(f'Привет я подруга Шона меня зовут {friend_1.name}, я родилась в {friend_1.birth_date}, моя профессия {friend_1.occupation},'
      f' высшее образование я  {friend_1.higher_education}, мое хобби {friend_1.hobby} \n')
friend_2.introduction()
print(f'Привет я друг Шона меня зовут {friend_1.name}, я родился в {friend_1.birth_date}, моя профессия {friend_1.occupation},'
      f' высшее образование я  {friend_1.higher_education}, мое хобби {friend_1.hobby} \n')