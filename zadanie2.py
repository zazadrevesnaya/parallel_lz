import multiprocessing

lock = 0
def init_lock(l):
    global lock
    lock = l

def appending_numbers(number):
    global lock
    with lock:
        with open("data.txt", "a") as file:
            file.write(f'{number}\n')

def process_pool():
    numbers = range(100)
    my_lock = multiprocessing.Lock()
    with multiprocessing.Pool(processes=10, initializer=init_lock, initargs=(my_lock,)) as pool:
        pool.map(appending_numbers, numbers)
    print('файлы записаны')

def main2():
    process_pool()
