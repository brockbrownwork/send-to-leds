from openpyxl import load_workbook
import pyperclip
import datetime

def stats():
    # grab the cell counts sheet
    workbook = load_workbook("PPH Calc.xlsx", data_only = True)
    sheet = workbook.active
    # this bit defines the number of spaces you put before each line of the output (to compensate for wonkyness)
    number_of_spaces = 0
    spaces = ' ' * number_of_spaces
    current_row = 3
    # grabs the time
    now = datetime.datetime.now()
    hour = now.hour
    if hour >= 13:
        hour = hour % 12
    minute = now.minute
    if len(str(minute)) == 1:
        minute = "0" + str(minute)
    output = "Since {0}:{1}:\n".format(hour, minute)
    current_row = 5
    # grabs each of the cell stats
    while str(sheet["A{0}".format(current_row)].value).lower() != "total pc":
        current_cell = sheet["A{0}".format(current_row)].value
        total_pc = sheet["B{0}".format(current_row)].value
        ind_pph_so_far = sheet["F{0}".format(current_row)].value
        ind_pph_so_far = round(ind_pph_so_far, 2)
        cell_pieces_left = round(sheet["H{0}".format(current_row)].value)
        cell_pieces_done = round(sheet["B{0}".format(current_row)].value)
        output =  output + "{2}C{0}: PPH {1}\n".format(current_cell, ind_pph_so_far, spaces)
        if cell_pieces_left <= 0:
            # output = output + "{1}C{0} is done!\n".format(current_cell, spaces)
            pass
        else:
            # output = output + "{2}C{0} {1} to go\n".format(current_cell, cell_pieces_left, spaces)
            output = output + "{2}C{0}: {1} pcs\n".format(current_cell, cell_pieces_done, spaces)
        current_row += 1

    # grabs SMA avg
    sma_avg = round(sheet["F{0}".format(current_row)].value, 2)
    sma_avg = str(sma_avg)
    output = output + spaces + "SMA: " + sma_avg + " PPH\n"
    sma_total_done = sheet["B15".format(current_row)].value
    # grabs the total pieces left to go
    total_to_go = round(sheet["H{0}".format(current_row)].value)
    if total_to_go <= 0:
        output = output + spaces + "Good job, everyone!"
    else:
        pass
        # output = output + spaces + str(total_to_go) + " to go"
        output = output + "SMA: " + spaces + str(sma_total_done) + " pcs"
    return output

