import pyautogui
import time
# import keyboard
import random
from pyperclip import copy
from wireless import connect
from excel_to_text_converter import stats

# pyautogui.displayMousePosition()

def click(x, y, double = False):
    pyautogui.click(x=x, y=y)
    time.sleep(0.3)
    if double:
        pyautogui.click(x=x, y=y)
        time.sleep(0.3)

def click_send():
    # clicks the send button
    found_it = pyautogui.locateOnScreen('images\\send.png')
    while not found_it:
        found_it = pyautogui.locateOnScreen('images\\send.png')
    click_object(found_it)

def click_object(thing, below = 0):
    x, y = thing[0], thing[1] + below
    if thing:
        click(x, y)

def minimize_all():
    time.sleep(2)
    found_it = pyautogui.locateOnScreen('images\\minus_sign.png')
    minus_signs = list(pyautogui.locateAllOnScreen('images\\minus_sign.png'))
    print(minus_signs)
    while len(minus_signs) > 1:
        # click the second minimize sign:
        click_object(minus_signs[1])
        minus_signs = list(pyautogui.locateAllOnScreen('images\\minus_sign.png'))
    print("done minimizing!")

def send(led_sign_id, message):
    minimize_all()
    connect(led_sign_id)
    # click the head group so that it doesn't change how the screens look
    found_it = pyautogui.locateOnScreen('images\\three_screens.png')
    while not found_it:
        found_it = pyautogui.locateOnScreen('images\\three_screens.png')
    click_object(found_it)
    found_it = pyautogui.locateOnScreen('images\\{0}.png'.format(led_sign_id))
    while not found_it:
        print("looking...")
        found_it = pyautogui.locateOnScreen('images\\{0}.png'.format(led_sign_id))
    click_object(found_it)
    # if the text box is available, click the text box
    found_it = pyautogui.locateOnScreen('images\\book.png')
    if found_it:
        click_object(found_it)
    else: # else, expand the first available program
        found_it = pyautogui.locateOnScreen('images\\plus_check_program.png')
        while not found_it:
            found_it = pyautogui.locateOnScreen('images\\plus_check_program.png')
        click_object(found_it)
        found_it = pyautogui.locateOnScreen('images\\book.png')
        while not found_it:
            found_it = pyautogui.locateOnScreen('images\\book.png')
        click_object(found_it)
    found_it = pyautogui.locateOnScreen('images\\mountains.png')
    while not found_it:
        found_it = pyautogui.locateOnScreen('images\\mountains.png')
    click_object(found_it, below = 50) # click the black text box
    pyautogui.hotkey('ctrl', 'a') # select existing text
    time.sleep(0.1)
    copy(message)
    pyautogui.hotkey('ctrl', 'v') # paste the new text
    click_send()

# keyboard.is_pressed('q') # returns True is q is pressed
# pyautogui.locateOnScreen(image_name) # returns position of the image
# if it's not there then just return false

'''
pyautogui.locateAllOnScreen(image_name) # this one finds all instances
while True:
    found_it = pyautogui.locateOnScreen('minus_sign.png')
    if found_it:
        print("I can see it")
        print(found_it[0], found_it[1], found_it)
    else:
        print("I am unable to see it.")
'''
# print (list(pyautogui.locateAllOnScreen("minus_sign.png")))
# send()

# send(1, "hello, this is a test")
testing = True
if testing:
    for led_id in range(1, 7):
        print("trying {0}".format(led_id))
        send(led_id, "Testing, this is led #{0}".format(led_id))
        time.sleep(10) # dirty workaround, fix later
input("Press enter to continue...")

'''
for led_id in range(1, 7):
    send(led_id, stats())
print("Connecting back to the internet...")
'''
connect("SJIHQ")
print("fin")
