import pyautogui
import time
import pydirectinput
import keyboard
import threading, sys
from pynput import mouse

def mining_forward():
    global terminated
    if not placing_torch:
        pydirectinput.keyDown("shift")
        pydirectinput.mouseDown()
        pydirectinput.keyDown("w")
    if keyboard.is_pressed("u"):
        pydirectinput.keyUp("w")
        pydirectinput.mouseUp()
        terminated = True
    if keyboard.is_pressed("p"):
        pydirectinput.keyUp("w")
        pydirectinput.mouseUp()
        time.sleep(10)
        pydirectinput.keyDown("w")
        pydirectinput.mouseDown()

def timer():
    torch_time = time.time()
    while not found_diamonds and not terminated:
        mining_forward()
        if(time.time() > torch_time + 10):
            torch_time = time.time()
            place_torch()

def place_torch():
    pydirectinput.keyUp("w")
    global placing_torch
    global torches_placed
    global torch_inv_pos
    torches_placed += 1
    if torches_placed % 64 == 0:
        torch_inv_pos += 1
        if torch_inv_pos > 9:
            torch_inv_pos = 2
    placing_torch = True
    pydirectinput.mouseUp()
    pydirectinput.moveRel(700, 400)
    pydirectinput.press(str(torch_inv_pos))
    pydirectinput.rightClick()
    pydirectinput.press('1')
    pydirectinput.moveRel(-700, -400)
    placing_torch = False
    pydirectinput.keyDown("w")


if __name__ == '__main__':
    time.sleep(5)
    found_diamonds = False
    placing_torch = False
    terminated = False
    torches_placed = 0
    torch_inv_pos = 2
    timer()
    pydirectinput.keyUp("shift")