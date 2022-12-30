from random import randint
from colorama import Fore, Back, init; init(autoreset=True)
import time

class CreateTable_:
    def __init__(self, title: list[str] = None, data: list[list] = None):
        self.title = title
        self.data = data
    def __length__(self):
        return len(str(max([len(str(item)) for items in self.data for item in items]))), max(len(item) for item in self.title)
    def plotTable(self):
        longest_item = max(self.__length__()) + 2
        print(longest_item)
        if self.title:
            for title in self.title:
                title = title.upper()
                print(f"{title:{longest_item}}", end="")
    
class CreateTable:
    def __init__(self, title: list[str] = None, data: list[list] = None):
        self.title = title
        self.data = data
        assert len(self.title) == max(len(data) for data in self.data), "Length of title is not equal to length of data"
    def __length__(self):
        title_length = [len(title) for title in self.title]
        data_length = [len(str(max(m_data))) for m_data in zip(*self.data)]
        return title_length, data_length
    def plotTable(self):
        title_length, data_length = self.__length__()
        list_longest_data = [max(list_) + 2 for list_ in zip(title_length, data_length)]
        dashes_len = sum(list_longest_data) + len(list_longest_data) + 1
        
        print("╷", end="")
        print("─" * dashes_len, end="╷\n")
        if self.title:
            print("│", end=" ")
            for index, title in enumerate(self.title):
                endd = "│"
                if index == len(self.title) - 1:
                    endd = " "
                print(f"{Fore.CYAN}{title.center(list_longest_data[index], ' ')}", end=endd)
            print("│")
            print("│", end="")
            print("─" * dashes_len, end="│\n")
            
        if self.data:
            for data in self.data: 
                print("│", end=" ")
                for index, x in enumerate(data):
                    endd = "│"
                    if index == len(data) - 1:
                        endd = " "
                    print(f"{Fore.LIGHTCYAN_EX}{str(x).center(list_longest_data[index], ' ')}", end=endd)
                print("│")
        print("╵", end="")
        print("—" * dashes_len, end="╵")

import os
while True:
    blink = 1
    print(f"""{Fore.LIGHTWHITE_EX}FPS: {blink} FPS""")
    item = [[int(str(randint(0, 99)).zfill(2)) for _ in range(5)] for _ in range(10)]
    createTable = CreateTable(title=["Serial no.", "Temperature (°C)", "Acceleration (m/s²)", "Altitude (m)", "Pressure (pascal)"], data=item)
    createTable.plotTable()
    time.sleep(blink)
    os.system("cls")    
    del createTable
    del item