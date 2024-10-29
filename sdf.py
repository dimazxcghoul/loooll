import time

import keyboard
import random
from datetime import datetime

possible_keys = ['enter', 'space', 'tab', 'backspace', 'esc', 'delete', 'end',
                 'page up', 'page down', 'up', 'down', 'left', 'right', 'shift', 'ctrl', 'alt']


start_game_time = datetime.now()

num_rounds = 4

tries = []

random_bind = possible_keys[random.randint(0,  len(possible_keys)-1)]


print(f'Время начала игры - {start_game_time.strftime('%H:%M:%S')}')

print(f'Нажмите клавишу: {random_bind} ')


while num_rounds > 0:
    time_start = time.time()
    keyboard.wait(f'{random_bind}')
    time_end = time.time()
    if time_end > 3:
        print('Время вышло!!! Вы ен успели')
    random_bind = possible_keys[random.randint(0, len(possible_keys) - 1)]
    print(f'Нажмите клавишу: {random_bind} ')
    num_rounds -= 1
    end_game_time = datetime.now()
    tries.append((time_end-time_start))
    print(f'Время реакции - {(time_end-time_start):.2f}')


print('-'*100)
print(f'Общее время игры: {(end_game_time - start_game_time).total_seconds():.2f} секунд')
print(f'Лучшее время реакции - {min(tries):.2f} сек')
print(f'Худшее время реакции - {max(tries):.2f} сек')
print(f'Среднее время реакции - {(sum(tries)/len(tries)):.2f} сек')


