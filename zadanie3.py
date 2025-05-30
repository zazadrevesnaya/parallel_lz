import threading
import time
import random

def writings_file(filename, data):
    with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
        file.write(data)

def reading_file(filename):
    with open(f"{filename}.txt", 'r', encoding='utf-8') as file:
        file.read()
        time.sleep(random.uniform(0.1, 5))  
    print(f"Данные прочтены из файла {filename}")

start = time.time()
threads = []

for i in range(10):
    thread = threading.Thread(target=writings_file, args=(f"filezad3_{i}", "data"))
    thread.start()
    threads.append(thread)

for t in threads:
    t.join() 

for i in range(10):
    reading_file(f"filezad3_{i}") 

