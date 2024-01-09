### Library Files ###
import json
import random
import customtkinter

### File Stuff ###
mmStat      = {}
mmStatBall  = {}
pbStat      = {}
pbStatBall  = {}
nyStat      = {}
c4Stat      = {}
c4StatBall  = {}
tenStat     = {}

### Choose Data File ###
def pick_game():
    return

file = open("tendata.json")
tenRecords = json.load(file)
file.close()

### Ticket Functions ###
def pick_best_ticket():
    selected_option=combobox.get()
    if selected_option == "PICK 10":
        for tenRecord in tenRecords["data"]:
            tenNumbers = tenRecord[9]
            tenArray = tenNumbers.split(" ")

            for tenResults in tenArray:
                if tenResults in tenStat:
                    occurences = tenStat[tenResults]
                    occurences += 1
                    tenStat[tenResults] = occurences
                else:
                    tenStat[tenResults] = 1
    else:
        print("Not a valid submission.")

    topTenStatSorted = sorted(tenStat.items(), key=lambda x:x[1], reverse=True)
    topTenStatSortedOccur = list(map(lambda x: x[0], topTenStatSorted))
    top21TenStatOccur = topTenStatSortedOccur[:25]
    realTicket = " ".join(sorted(random.sample(top21TenStatOccur, 10)))
    response = print("High Pick Ticket: {}".format(realTicket))
    return response


### Graphical User Interface ###
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Gamble Time", font=("Arial", 24))
label.pack(pady=12, padx=10)

combobox = customtkinter.CTkComboBox(master=frame, values=["MEGA MILLION", "POWERBALL", "CASH 4 LIFE", "NY LOTTO", "PICK 10"])
combobox.pack(padx=20, pady=10)
combobox.set("MEGA MILLION")

select = combobox.get()
submit = customtkinter.CTkButton(master=frame, text="Select", command=pick_best_ticket)
submit.pack(padx=20, pady=10)

result = customtkinter.CTkLabel(master=frame, text=submit.pack, font=("Arial", 24))
result.pack(pady=12, padx=10)

### Formatting Returns ###
# bestTicket = " ".join(sorted(topTenStatSortedOccur[:10]))
# print("Winning Ticket: {}".format(bestTicket))

root.mainloop()