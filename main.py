from zadanie1 import main1
from zadanie2 import main2 
from zadanie3 import main3
import asyncio
import time

def main():
    print('1 задание')
    main1()
    time.sleep(1)
    print('2 задание')
    main2()
    time.sleep(1)
    print('3 задание')
    main3()
    
if __name__ == '__main__':
    main()