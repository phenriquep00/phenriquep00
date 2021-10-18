#! /usr/bin/env python3

import player
import pyautogui
from time import sleep

# player
player = player.Player('fairywartal')

# accept mission
coordinates = [
    (1806, 1015),
    (1584, 177),
    (1516, 242),
    (1004, 356),
    (387, 629),
    (312, 865),
    (672, 245)
]
for _ in coordinates:
    if _[0] == 1004:
        sleep(1)
    pyautogui.click(_)
    sleep(1)

# defeated makai
sleep(2)
player.join_room('tercessuinotlim')

