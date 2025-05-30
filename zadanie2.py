import multiprocessing

def appending_numbers(number):
    with open("data.txt", "a") as file:
        file.write(f'{number}\n')

if __name__ == "__main__":
    filename = "data.txt"
    with open(filename, "w") as file:
        file.write("")
    numbers = range(100)  
    with multiprocessing.Pool(processes=10) as pool:
        pool.map(appending_numbers, numbers)
    print('файлы записаны')
