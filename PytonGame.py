#!/usr/bin/env python
import random
import os
print('Добро пожаловать в Квест.')
print('Вы Рыцарь')

#меч
#def sword(life = 0, power = 1):
sword = None
    #return('life': life,'power': power)

#def apple(life = 1, power = 0):
apple = None
    #return('life': life,'power': power)

#Враг
#def enemy():
enemy_helth = None
enemy_strength = None
    #return ('life': life, 'power': power)

#рыцарь
#def knight():
knight_helth = 10
knight_strength = 10
    #return ('life': life, 'power': power)

#Этап
stage = 1

#Победа
wins = 0

#МАКСИМАЛЬНЫЕ ПОБЕДЫ
wins_count = 10
#обьекты
object_list = ('best', 'sword', 'apple')

#здоровье и сила
def strength_helth_gen() -> int:
    value = random.randint(5, 15)
    return value

#Выбор обьекта

def change_object(obj: tuple) -> str:
    return random.choice(obj)

#h its = enemy(self)
#for hit in hits:
   # enemy.shield -= enemy.shield

    #if knight.shield <= 0:
        #running = False

#функция выбора
#def choice_step(mapping):
    #step = random.randint(1, 3)
    #return mapping[step]

#def game_cycle(step):
    #return game_cycle[step]





if __name__ == "__main__":
    #hero_map = {
       # 1: sword,
        #2: apple,
       # 3: enemy
   # }
    #func = choice_step(hero_map)
   # print('Ваш враг:',func())
    #print(type(func()))
    #print(func.get())


    #обработка ввода
    def key_handler() -> str:
        while True:
            user_key = input()
            if user_key not in ['1', '2']:
                print('не знаю такое действие')
                continue
            else:
                break
        return user_key
    print('Рыцарь и враг')
    print('')


# начало циклов
    while wins < wins_count:
       print('Шаг:', stage)
       next_object = change_object(object_list)
       print(f'Рыцарь.сила: {knight_strength},здоровье: {knight_helth}')
       print('Введите 1 - что бы атаковать 2- уйти с позором')
       if next_object == 'beast':
           enemy_helth = strength_helth_gen()
           enemy_strength = strength_helth_gen()
           print(f'Враг. сила: {enemy_strength},здоровье: {enemy_helth}')
           print('Введите 1 - что бы атаковать 2- уйти с позором')
       if next_object == 'apple':
            apple = strength_helth_gen()
            print('Яблоко + здоровье')
            print('Введите что бы сьесть - 2 ')
       if next_object == 'sword':
            sword = strength_helth_gen()
            print(f'Меч, сила атаки: {sword}')
            print('Введите 1 - что бы взять 2 - пройти мимо')
       user_key = key_handler()

       if user_key == '1':
           if next_object == 'apple':
                knight_helth += apple
                print(f'Здоровье: {apple}')
           if next_object == 'sword':
                knight_strength = sword
           if next_object == 'beast':
                knight_helth -= enemy_helth
                enemy_strength -= knight_strength
                if knight_strength <= 0:
                    break
 #убитое чудовище
                if enemy_helth <= 0:
                    wins += 1
                    print('Враг повержен')


       if user_key == '2':
            if next_object == 'apple':
                knight_helth += apple
                print(f'Увеличение здоровья + {apple}')

stage +=1
print('')
if wins == wins_count:
    print('Победа')
else:
    print('Конец игры')




