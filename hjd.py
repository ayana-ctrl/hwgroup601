# class Soda:
#     def __init__(self, production , additive):
#         self.production = production
#         self.additive= additive


#     def snow_my_drink(self):
#         if self.additive:
#             lemon_additive = 'included'
#         else:
#            print('regular soda')

#         print(f'soda from {self.production}, have a {lemon_additive}')

# soda_cola= Soda('Coca cola', True)
# soda_jalal_abad =Soda ('Jalal-Abad', False)

# drinks = [soda_cola, soda_jalal_abad]

# for soda in drinks:
#     soda.snow_my_drink() ошибка 

# class Soda:
#     def __init__(self, ingredient = None):
#         if isinstance(ingredient, str): # чтобы на печате ввели только строку ни True ни целое число
#            self.ingredient = ingredient # первый if-else для того чтобы вычислить тип
#         else:
#          self.ingredient = None    

#     def show_my_drink(self):    # проверяет есть ли добавка
#        if self.ingredient:
#           print(f'Газировка и {self.ingredient}') 
#        else:
#           print('Обычная газировка')

# drink1= Soda()
# drink2= Soda('малина')
# drink3 =Soda(5)

# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()


# вторая задача:
class TriangleChecker:
    def __init__(self, sides):
        self.sides = sides

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted_sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ура, можно построить треугольник!'
                return 'Жаль, но из этого треугольник не сделать'
            return 'С отрицательными числами ничего не выйдет!'
        return 'Нужно вводить только числа!'
 
 
# Тесты
triangle1 = TriangleChecker([2, 3, 4])
print(triangle1.is_triangle())
triangle2 = TriangleChecker([77, 3, 4])
print(triangle2.is_triangle())
triangle3 = TriangleChecker([77, 3, 'Сторона3'])
print(triangle3.is_triangle())
triangle4 = TriangleChecker([77, -3, 4])
print(triangle4.is_triangle())