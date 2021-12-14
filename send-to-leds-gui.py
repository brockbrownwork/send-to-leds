import tkinter as tk
from tkinter import messagebox, INSERT
import json

old_output = {}
try:
    with open("gui-info.json", "r") as infile:
        old_output = json.load(infile)
except FileNotFoundError:
    print("Couldn't find gui-info.json, moving on...")

def on_closing():
    save()
    window.destroy()

def save():
    output = {}
    for location in all_locations:
        output[location] = {}
        for message in all_messages:
            output[location][message] = check_buttons[location][message].get()
            if message == "Custom message":
                text_in_box = custom_text[location].get("1.0", "end")[:-1]
                if len(text_in_box) > 0:
                    output[location]["text"] = text_in_box
                else:
                    output[location][message] = check_buttons[location][message].get()
    with open("gui-info.json", "w") as outfile:
        json.dump(output, outfile)
    return output

def send_button():
    output = save()
    messagebox.showinfo("hello", "{0}".format(output))

all_messages = ['PPH', 'eComm', 'Good morning', 'Good job everybody', "Custom message"]
all_locations = ['All Cells', 'C1 + C2', 'C4 / Cutting', 'C5', 'C8', 'C9', 'C13 + C14'] # TODO: fix networking to take these as well as LED IDs

window = tk.Tk()
window.protocol("WM_DELETE_WINDOW", on_closing)
window.title("Send to LEDs")
check_buttons = {}
custom_text = {}

# Loads up the GUI
for i, location in enumerate(all_locations):
    led_id = i + 1
    location_label = tk.Label(text = location)
    location_label.grid(column = i, row = 0, sticky = 'w')
    check_buttons[location] = {}
    for j, message in enumerate(all_messages):
        check_buttons[location][message] = tk.IntVar()
        check_button = tk.Checkbutton(text="{0}".format(message),
                                      variable = check_buttons[location][message])
        # check the old buttons that were checked previously
        if old_output != {} and location in old_output and message in old_output[location]:
            if old_output[location][message] == 1:
                check_button.select()
        check_button.grid(column = i, row = j + 1, sticky = 'w')
    custom_text[location] = tk.Text(width = 20, height = 3)
    if old_output != {} and 'text' in old_output[location]:
        text = old_output[location]['text']
        custom_text[location].insert(INSERT, text) # TODO: get the old custom text into the box
    custom_text[location].grid(column = i, row = j + 2)

button = tk.Button(text = 'Send', command = send_button)
button.grid(column = 0, sticky = 'w')



window.mainloop()


