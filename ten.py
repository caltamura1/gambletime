import json

file = open("tendata.json")
tenRecords = json.load(file)
file.close()

tenStat = {}

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

topTenStatSorted = sorted(tenStat.items(), key=lambda x:x[1], reverse=True)
topTenStatSortedOccur = list(map(lambda x: x[0], topTenStatSorted))

WinningTicket = " ".join(topTenStatSortedOccur[:20])
print("Winning Ticket: {}".format(WinningTicket))