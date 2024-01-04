import json

file = open("data.json")
pbRecords = json.load(file)
file.close()

pbStat = {}
numStat = {}

for pbRecord in pbRecords["data"]:
    pbNumbers = pbRecord[9]
    numArr = pbNumbers.split(" ")
    pbNums = numArr.pop()

    for numRegular in numArr:
        if numRegular in numStat:
            occurences = numStat[numRegular]
            occurences += 1
            numStat[numRegular] = occurences
        else:
            numStat[numRegular] = 1

    if pbNums in pbStat:
        occurences = pbStat[pbNums]
        occurences += 1
        pbStat[pbNums] = occurences
    else:
        pbStat[pbNums] = 1
    


numStatSorted = sorted(numStat.items(), key=lambda x:x[1], reverse=True)
pbStatSorted = sorted(pbStat.items(), key=lambda x:x[1], reverse=True)
numStatSortedOccur = list(map(lambda x: x[0], numStatSorted))
pbStatSortedOccur = list(map(lambda x: x[0], pbStatSorted))

WinningTicket = " ".join(numStatSortedOccur[:10] + pbStatSortedOccur[:3])
print("Winning Ticket: {}".format(WinningTicket))