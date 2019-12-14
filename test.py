import pyautogui as pgui
import time

def do_loop():
    is_doing = True
    while True:
        if is_doing:
            time.sleep(1)
            print("running")
            pgui.press('down')
            time.sleep(1)
            pgui.press('enter')


if __name__ == '__main__':
    do_loop()