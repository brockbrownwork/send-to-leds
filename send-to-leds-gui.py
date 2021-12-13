import tkinter as tk
from tkinter import messagebox
import json


def send_button():
    output = {}
    for location in all_locations:
        output[location] = {}
        for message in all_messages:
            output[location][message] = check_buttons[location][message].get()
    messagebox.showinfo("hello", "{0}".format(output))
    with open("info.json", "w") as outfile:
        json.dump(output, outfile)

all_messages = ['PPH', 'eComm', 'Good morning', 'Good job everybody', "Custom message"]
all_locations = ['All Cells', 'C4 / Cutting', 'C1 + C2', 'C8'] # these are in order of their led IDs

window = tk.Tk()
window.title("Send to LEDS")
check_buttons = {}
custom_text = {}

for i, location in enumerate(all_locations):
    led_id = i + 1
    location_label = tk.Label(text = location)
    location_label.grid(column = i, row = 0, sticky = 'w')
    check_buttons[location] = {}
    for j, message in enumerate(all_messages):
        check_buttons[location][message] = tk.IntVar()
        check_button = tk.Checkbutton(text="{0}".format(message),
                                      variable = check_buttons[location][message])
        check_button.grid(column = i, row = j + 1, sticky = 'w')

button = tk.Button(text = 'Send', command = send_button)
button.grid(column = 0, sticky = 'w')



window.mainloop()


