#! /usr/bin/env python3

import player
import pyautogui
from time import sleep

player = player.Player('foo')

sleep(1)
pyautogui.click(800, 800)

player.join_room(room_name='citadel', private=True)
