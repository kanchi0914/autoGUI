from pynput.keyboard import Key, Listener
import threading
import tkinter as tk
import key_inputer
import sys

def on_press(key):
    global is_running
    try:
        if (key.char == 'q'):
            if is_running:
                is_running = False
                var.set("停止中")
            else:
                is_running = True
                var.set("動作中")
    except AttributeError:
        pass


def on_release(key):
    pass


def process1():
    while True:
        if is_running:
            key_inputer.input()


def process2():
    with Listener(
        on_press = on_press,
        on_release= on_release
    ) as listener:
        listener.join()

is_running = False

thread = threading.Thread(target=process1)
thread2 = threading.Thread(target=process2)

root = tk.Tk()
root.geometry("300x150")
root.attributes("-topmost", True)
root.title("Danron_AutoGacha")
var = tk.StringVar()
var.set("停止中")
label0 = tk.Label(root, text="qキーで開始/停止")

label0.pack()
label = tk.Label(root, textvariable=var)
label.config(font=("MS Gothic", 20))
label.pack()


if __name__ == '__main__':
    thread.setDaemon(True)
    thread2.setDaemon(True)

    thread.start()
    thread2.start()

    root.mainloop()