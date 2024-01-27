### Library Files ###
import json
import random
import customtkinter

### File Stuff ###
mmStat       = {}
mmStatBall   = {}
pbStat       = {}
pbStatBall   = {}
nyStat       = {}
c4lStat      = {}
c4lStatBall  = {}
tenStat      = {}

### Single function to call others with 1 command ###
def on_submit():
    currentSelect = combobox.get()
    records = load_file(currentSelect)
    pick_best_ticket(currentSelect, records, output_label)

### Choose Data File ###
def load_file(selection):
    records = None
    if selection == "PICK 10":
        try:
            file = open("pick10.json")
            records = json.load(file)
            file.close()
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
    elif selection == "NY LOTTO":
        try:
            file = open("nylotto.json")
            records = json.load(file)
            file.close()
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
    elif selection == "CASH 4 LIFE":
        try:
            file = open("cash4life.json")
            records = json.load(file)
            file.close()
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
    elif selection == "POWERBALL":
        try:
            file = open("powerball.json")
            records = json.load(file)
            file.close()
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
    elif selection == "MEGAMILLIONS":
        try:
            file = open("megamillions.json")
            records = json.load(file)
            file.close()
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
    else:
        print("Selection not found.")
    return records

### Ticket Picking Functions ###
def pick_best_ticket(selected_option, records, output_label):
    if selected_option == "PICK 10":
        for tenRecord in records["data"]:
            tenNumbers = tenRecord[9]
            tenArray = tenNumbers.split(" ")
            for tenResults in tenArray:
                if tenResults in tenStat:
                    occurences = tenStat[tenResults]
                    occurences += 1
                    tenStat[tenResults] = occurences
                else:
                    tenStat[tenResults] = 1
        topTenStatSorted = sorted(tenStat.items(), key=lambda x:x[1], reverse=True)
        topTenStatSortedOccur = list(map(lambda x: x[0], topTenStatSorted))
        top21TenStatOccur = topTenStatSortedOccur[:25]
        realTicket = " ".join(sorted(random.sample(top21TenStatOccur, 10)))
        response = "High Pick Ticket\n {}".format(realTicket)

    elif selected_option == "NY LOTTO":
        for nyRecord in records["data"]:
            nyNumbers = nyRecord[9]
            nyArray = nyNumbers.split(" ")
            for nyResults in nyArray:
                if nyResults in nyStat:
                    occurences = nyStat[nyResults]
                    occurences += 1
                    nyStat[nyResults] = occurences
                else:
                    nyStat[nyResults] = 1
        topNYStatSorted = sorted(nyStat.items(), key=lambda x:x[1], reverse=True)
        topNYStatSortedOccur = list(map(lambda x: x[0], topNYStatSorted))
        top21NYStatOccur = topNYStatSortedOccur[:25]
        realTicket = " ".join(sorted(random.sample(top21NYStatOccur, 6)))
        response = "High Pick Ticket\n {}".format(realTicket)

    elif selected_option == "CASH 4 LIFE":
        for c4lRecord in records["data"]:
            c4lNumbers = c4lRecord[9]
            c4lArray = c4lNumbers.split(" ")
            c4lBall = c4lRecord[10]

            for c4lResults in c4lArray:
                if c4lResults in c4lStat:
                    c4lStat[c4lResults] += 1
                else:
                    c4lStat[c4lResults] = 1

            if c4lBall in c4lStatBall:
                c4lStatBall[c4lBall] += 1
            else:
                c4lStatBall[c4lBall] = 1
            
        topC4LStatSorted = sorted(c4lStat.items(), key=lambda x:x[1], reverse=True)
        C4LBallStatSorted = sorted(c4lStatBall.items(), key=lambda x:x[1], reverse=True)

        topC4LStatSortedOccur = list(map(lambda x: x[0], topC4LStatSorted))
        C4LBallStatSortedOccur = list(map(lambda x: x[0], C4LBallStatSorted))

        top21C4LStatOccur = topC4LStatSortedOccur[:25]
        top3C4LBALLStatOccur = C4LBallStatSortedOccur[:5]

        primary = " ".join(sorted(random.sample(top21C4LStatOccur, 5)))
        secondary = "".join(sorted(random.sample(top3C4LBALLStatOccur, 1)))

        primaryFMT = "High Pick Ticket\n{}".format(primary)
        secondaryFMT = "\n\nPowerball\n{}".format(secondary)

        realTicket = primaryFMT + secondaryFMT
        response = realTicket

    elif selected_option == "POWERBALL":
        for pbRecord in records["data"]:
            pbNumbers = pbRecord[9]
            pbArray = pbNumbers.split(" ")
            pbBall = pbArray.pop()

            for pbResults in pbArray:
                if pbResults in pbStat:
                    pbStat[pbResults] += 1
                else:
                    pbStat[pbResults] = 1

            if pbBall in pbStatBall:
                pbStatBall[pbBall] += 1
            else:
                pbStatBall[pbBall] = 1
    
        topPBStatSorted = sorted(pbStat.items(), key=lambda x:x[1], reverse=True)
        pbBallStatSorted = sorted(pbStatBall.items(), key=lambda x:x[1], reverse=True)

        topPBStatSortedOccur = list(map(lambda x: x[0], topPBStatSorted))
        pbBallStatSortedOccur = list(map(lambda x: x[0], pbBallStatSorted))

        top21PBStatOccur = topPBStatSortedOccur[:25]
        top3PBBALLStatOccur = pbBallStatSortedOccur[:6]

        primary = " ".join(sorted(random.sample(top21PBStatOccur, 5)))
        secondary = "".join(sorted(random.sample(top3PBBALLStatOccur, 1)))

        primaryFMT = "High Pick Ticket\n{}".format(primary)
        secondaryFMT = "\n\nPowerball\n{}".format(secondary)

        realTicket = primaryFMT + secondaryFMT
        response = realTicket

    elif selected_option == "MEGAMILLIONS":
        for mmRecord in records["data"]:
            mmNumbers = mmRecord[9]
            mmArray = mmNumbers.split(" ")
            mmBall = mmRecord[10]

            for mmResults in mmArray:
                if mmResults in mmStat:
                    mmStat[mmResults] += 1
                else:
                    mmStat[mmResults] = 1

            if mmBall in mmStatBall:
                mmStatBall[mmBall] += 1
            else:
                mmStatBall[mmBall] = 1
            
        topMMStatSorted = sorted(mmStat.items(), key=lambda x:x[1], reverse=True)
        mmBallStatSorted = sorted(mmStatBall.items(), key=lambda x:x[1], reverse=True)

        topMMStatSortedOccur = list(map(lambda x: x[0], topMMStatSorted))
        mmBallStatSortedOccur = list(map(lambda x: x[0], mmBallStatSorted))

        top21MMStatOccur = topMMStatSortedOccur[:25]
        top3MMBALLStatOccur = mmBallStatSortedOccur[:5]
        
        primary = " ".join(sorted(random.sample(top21MMStatOccur, 5)))
        secondary = "".join(sorted(random.sample(top3MMBALLStatOccur, 1)))

        primaryFMT = "High Pick Ticket\n{}".format(primary)
        secondaryFMT = "\n\nPowerball\n{}".format(secondary)

        realTicket = primaryFMT + secondaryFMT
        response = realTicket

    else:
        print("Not a valid submission.")

    output_label.configure(text=response)

### Graphical User Interface ###
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

### Variables to store GUI dimensions ###
root = customtkinter.CTk()
root.geometry("500x350")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

### GIU Title ###
label = customtkinter.CTkLabel(master=frame, text="Gamble Time", font=("Arial", 24))
label.pack(pady=12, padx=10)

### Dropdown Menu ###
comboOptions = ["MEGAMILLIONS", "POWERBALL", "CASH 4 LIFE", "NY LOTTO", "PICK 10"]
combobox = customtkinter.CTkComboBox(master=frame, values=comboOptions)
combobox.pack(padx=20, pady=10)
combobox.set(comboOptions[-1])

### Select button for Combobox ###
# select = combobox.get()
submit = customtkinter.CTkButton(master=frame, text="Select", command=(on_submit))
submit.pack(padx=20, pady=10)

### File Loading ###
gameSelect = customtkinter.StringVar(root)
gameSelect.set(comboOptions[-1])

### Output Ticket ###
output_label = customtkinter.CTkLabel(master=frame, text="", font=("Arial", 18))
output_label.pack(pady=10)

### Game run loop ###
root.mainloop()