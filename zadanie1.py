import threading
import time
import random

def writing_file(filename, data):
        with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
            file.write(data)
            time.sleep(1)
        print(f"Данные записаны в файл {filename}")

#парралельное выполнение
start1 = time.time()
threads = []
for i in range(10):
    num = [random.randint(1,100) for o in range(100)]
    thread = threading.Thread(target = writing_file, args=(f"file_{i}" , f"num = {num}"))
    thread.start()
    threads.append(thread)
    res1 = time.time()-start1

time.sleep(5)
#последовательное выполнение
print('последовательное')
start2 = time.time()
for i in range(10):
    num = [random.randint(1,100) for o in range(100)]
    writing_file(f"file_1{i}" , f"num = {num}") 
res2 = time.time() - start2
print('последовательно',time.time() - start2)

for t in threads:
     t.join()
print("result1=", res1)
print("result2=", res2)
print('результаты:')
if res1 > res2:
    print('res1 > res2')
elif (res1 < res2):
    print('res1 < res2')
else:
    print('res1 = res2')
