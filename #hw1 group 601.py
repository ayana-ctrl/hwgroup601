#hw1 group 601
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

        print(f'Здравствуйте! Меня зовут {self.name}, я родился(ась) в {self.birth_date}, '
              f'моя профессия — {self.occupation}, высшее образование {education_status}.')

# создаём объекты
person_sean = Person(name='Шон', birth_date='1830-04-09', occupation='учитель по пианино', higher_education=True)
person_aya = Person(name='Ая', birth_date='2145-12-20', occupation='архитектор безопасности', higher_education=True)
person_denise = Person(name='Денис', birth_date='2006-07-01', occupation='солистка сопрано оркестра', higher_education=False)

# список и вывод
people = [person_sean, person_aya, person_denise]

for person in people:
    person.introduction()