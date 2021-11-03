import pyautogui
from time import sleep


class Player():

    def __init__(self, classe):
        self.classe = classe
    
    def move(self, x, y, wait):
        pyautogui.click(x, y)
        sleep(wait)
        

    def join_room(self, room_name: str, private=False):

        if room_name == 'tercessuinotlim':  # go to tercessuinotlim
            self.join_room('citadel')
            
            coordinates = [
                (1762, 619),
                (970, 698),
                (1210, 424),
                (1591, 496),
                (1251, 672)
            ]

            times = [3.2, .3, .5, 6.2, 2.8]

            for _ in range(5):
                self.move(coordinates[_][0], coordinates[_][1], times[_])

            pyautogui.press('enter')
            sleep(.2)
            pyautogui.typewrite('/join tercessuinotlim')
            pyautogui.press('enter')

        else:

            pyautogui.press('enter')

            if private:
                pyautogui.typewrite(f'/join {room_name}-55555')
            else:
                pyautogui.typewrite(f'/join {room_name}')
            
            pyautogui.press('enter')
        
        sleep(4)

    def attack(self, className, times):
        if className is 'vhl' or className is 'Void Highlord':
            for _ in times:
                pyautogui.press('4')
                sleep(1)
                pyautogui.press('5')
                sleep(1)
                pyautogui.press('3')
                sleep(1)
                pyautogui.press('2')
                sleep(1)
        pass

    def collect_item():
        pass

    def accept_mission():
        pass

    def complete_mission():
        pass
