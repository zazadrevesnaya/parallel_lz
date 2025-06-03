import asyncio
import random

async def create_file(filename):
    with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
        file.write(f"data {filename}")
    print(f"Файл {filename} создан.")

async def reading_file(filename):
    delay = random.uniform(0.1, 5)  
    await asyncio.sleep(delay)
    print(f"Файл {filename} прочитан за {delay:.2f} сек.")

async def main():
    tasks = [
        asyncio.create_task(create_file(f"filezad3_{i}")) for i in range(10)
    ]
    await asyncio.gather(*tasks)
    tasks = [
        asyncio.create_task(reading_file(f"filezad3_{i}")) for i in range(10)
    ]
    await asyncio.gather(*tasks)

def main3():
    asyncio.run(main())
