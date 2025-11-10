class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby


classmate_1 = Classmate('Ада', '1832-12-17', 'пианистка', False, '601')
classmate_2 = Classmate('Карло', '1833-05-13', 'пианист', False, '601')

friend_1 = Friend('Аиша', '1832-12-17', 'хирург', True, 'чтение') 
friend_2 = Friend('Карло', '1835-08-06', 'художник', False, 'рисование')


# не уверенна что корректно 
print(f'Привет, я одноклассница Шона, меня зовут {classmate_1.name}, '
      f'я родилась в {classmate_1.birth_date}, моя профессия — {classmate_1.occupation}, '
      f'высшее образование я {"имею" if classmate_1.higher_education else "не имею"}, '
      f'я учусь в группе {classmate_1.group_name}.\n')
print(f'Привет, я одноклассник Шона, меня зовут {classmate_2.name}, '
      f'я родился в {classmate_2.birth_date}, моя профессия — {classmate_2.occupation}, '
      f'высшее образование я {"имею" if classmate_2.higher_education else "не имею"}, '
      f'я учусь в группе {classmate_2.group_name}.\n')
print(f'Привет, я подруга Шона, меня зовут {friend_1.name}, '
      f'я родилась в {friend_1.birth_date}, моя профессия — {friend_1.occupation}, '
      f'высшее образование я {"имею" if friend_1.higher_education else "не имею"}, '
      f'моё хобби — {friend_1.hobby}.\n')
print(f'Привет, я друг Шона, меня зовут {friend_2.name}, '
      f'я родился в {friend_2.birth_date}, моя профессия — {friend_2.occupation}, '
      f'высшее образование я {"имею" if friend_2.higher_education else "не имею"}, '
      f'моё хобби — {friend_2.hobby}.\n')
