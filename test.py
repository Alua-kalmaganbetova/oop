import random

class movies:
    def __init__(self,name,data,cast,money):
        self.name = name
        self.data = data
        self.cast = cast
        self.money = money 

Iron_man = movies(name='Железный человек', data='2008', cast='Роберт Дауни-младший, Джон Фавро, Гвинет Пэлтроу.', money='140 000 000 $')
Spider_man = movies(name='Человек-паук', data='2022', cast='Том Холланд, Зендея, Тоби Магуйар, Эндрю Гарфилд.', money='200 000 000 $')
Black_widow = movies(name='Черная вдова', data='2021', cast='Скарлетт Йохансон, Флоренс Пью, Рэйчел Вайс.', money='200 000 000 $')



        


print('Список фильмов:\n Железный человек \n Человек-паук: нет пути домой \n Черная вдова')
film = input('Введите также как в списке: ')


n = random.randint(1,30)

if film == 'Железный человек':
    inf = 'Да'
    while inf == 'Да':
        inf = input('Хотите узнать подробную информацию? ')
        if inf == 'Нет':
            break
        inf1 = input('Что Вы хотите узнать: \n Год выхода \n Бюджет фильма \n Актерский состав \n')
        if inf1 == 'Год выхода':
            print(Iron_man.data)
        elif inf1 == 'Бюджет фильма':
            print(Iron_man.money)
        elif inf1 == 'Актерский состав':
            print(Iron_man.cast)
    else:
        print(f'Ваш номер билета:{n}')
elif film == 'Черная вдова':
    inf = 'Да'
    while inf == 'Да':
        inf = input('Хотите узнать подробную информацию? ')
        if inf == 'Нет':
            break
        inf1 = input('Что Вы хотите узнать: \n Год выхода \n Бюджет фильма \n Актерский состав \n')
        if inf1 == 'Год выхода':
            print(Black_widow.data)
        elif inf1 == 'Бюджет фильма':
            print(Black_widow.money)
        elif inf1 == 'Актерский состав':
            print(Black_widow.cast)
    else:
        print(f'Ваш номер билета:{n}')
else:
    inf = 'Да'
    while inf == 'Да':
        inf = input('Хотите узнать подробную информацию? ')
        if inf == 'Нет':
            break
        inf1 = input('Что Вы хотите узнать: \n Год выхода \n Бюджет фильма \n Актерский состав \n')
        if inf1 == 'Год выхода':
            print(Spider_man.data)
        elif inf1 == 'Бюджет фильма':
            print(Spider_man.money)
        elif inf1 == 'Актерский состав':
            print(Spider_man.cast)
    else:
        print(f'Ваш номер билета:{n}')





        

