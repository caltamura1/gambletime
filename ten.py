import json
import random

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
top21TenStatOccur = topTenStatSortedOccur[:25]

realTicket = " ".join(sorted(random.sample(top21TenStatOccur, 10)))
bestTicket = " ".join(sorted(topTenStatSortedOccur[:10]))

print("Winning Ticket: {}".format(bestTicket))
print("High Pick Ticket: {}".format(realTicket))