import threading
import time
import random

def writing_file(filename, data):
    with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
        file.write(data)
        time.sleep(1)
    print(f"Данные записаны в файл {filename}")

def parallel():
    global res1  # Делаем переменную глобальной
    start1 = time.time()
    threads = []

    for i in range(10):
        num = [random.randint(1,100) for _ in range(100)]
        thread = threading.Thread(target=writing_file, args=(f"file_{i}", f"num = {num}"))
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    res1 = time.time() - start1
    print("Параллельное выполнение:", res1)
    time.sleep(5)

def posledovat():
    global res1  
    print('Последовательное выполнение')
    start2 = time.time()

    for i in range(10):
        num = [random.randint(1,100) for _ in range(100)]
        writing_file(f"file_1{i}", f"num = {num}")

    res2 = time.time() - start2
    print('Последовательно:', res2)

    print("Результаты:")
    if res1 > res2:
        print('Параллельное выполнение дольше')
    elif res1 < res2:
        print('Последовательное выполнение дольше')
    else:
        print('Одинаковое время выполнения')

def main1():
    parallel()
    posledovat()

