import pyautogui #needs instalation
import time
import keyboard #needs instalation
import sys

print("This program was made by Mika#0224, to pause the typing press escape, and if you wanna end the spamming early then just cancel the script in your terminal while the script is paused. ")
time.sleep(1)
message_spam = input("Alright, so what message do you want to spam? ")
try:
    spam_amount = range(int(input("How many times do you want to spam the message? ")))
    spam_time = float(input("How many seconds do you want between the messages? "))
except ValueError:
    print("Bruh that ain't even a number")
    time.sleep(2)
    sys.exit()

print('Messages will start sending in 5 seconds')
time.sleep(5)

print('Typing spam...')
try:
    for i in spam_amount:
        time.sleep(spam_time)
        pyautogui.write(message_spam)
        pyautogui.press('enter')
        if keyboard.is_pressed('escape'):
            pyautogui.alert('Typing paused, press ok to continue typing.')

    print("Spamming completed, program closing in 3 seconds...")
    time.sleep(3)

except KeyboardInterrupt:
    print("Spambot canceled, program closing in 3 seconds...")
    time.sleep(3)