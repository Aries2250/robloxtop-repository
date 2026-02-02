import random 

colors = ['красный', 'синий', 'зеленый', 'желтый', 'фиолетовый', 'оранжевый', 'розовый', 'коричневый', 'черный', 'белый']
def get_random_color():
    return f'ваш случайно выбранный цвет: {random.choice(colors)}'
print(get_random_color())