import pyautogui
import numpy as np
import time
import keyboard
import random as rm

def countdown(seconds):
    while seconds > 0:
        print(seconds)
        time.sleep(1)
        seconds -= 1


countdown(5)
print("Программа запущена!")

def get_pixel_color(x, y):
    # Создаем скриншот экрана
    screenshot = pyautogui.screenshot()

    # Преобразуем скриншот в массив numpy
    image_array = np.array(screenshot)

    # Получаем RGB цвет пикселя
    pixel_color = image_array[y, x]

    # Возвращаем массив [R, G, B]
    return pixel_color.tolist()

start_time = time.time()  # Время начала цикла
total_time = 0  # Общее время, прошедшее во всех циклах
cycle_count = 0  # Количество циклов
cars_count = 0 # Количество купленных машин

while not keyboard.is_pressed('f11'):

    #  Поиск аук (меню)
    time.sleep(1.0)

    while not get_pixel_color(330,200) == [255, 222, 57]:
        pyautogui.press('enter')
        time.sleep(0.2)
    time.sleep(0.3)
    #  Проверка на наличие
    if (get_pixel_color(710,271) == [247, 247, 247]):
        time.sleep(0.3)
        while not get_pixel_color(690,400) == [52, 23, 53]:
            pyautogui.press('y')
            time.sleep(0.1)
        time.sleep(0.05)
        pyautogui.press('down')
        time.sleep(0.15)
        pyautogui.press('enter')
        time.sleep(0.15)
        pyautogui.press('enter')
        time.sleep(rm.uniform(4,5))
        pyautogui.press('enter')
        time.sleep(rm.uniform(0.5,0.55))
        pyautogui.press('esc')
        time.sleep(rm.uniform(0.5,0.55))
        pyautogui.press('esc')
        cars_count += 1
    else:
        pyautogui.press('esc')

    # Вычисление времени, прошедшего за текущий цикл
    cycle_time = round(time.time() - start_time,2)

    total_time += cycle_time  # Добавляем время текущего цикла ко времени всех циклов

    print(f"Прошло времени за цикл {cycle_count + 1}: {cycle_time} секунд")

    cycle_count += 1  # Увеличиваем счетчик циклов

    start_time = time.time()  # Обновляем время начала цикла

total_min = total_time/60
print(f"Общее время: {round(total_min,2)} минут")
print(f"Всего куплено {cars_count} машин")