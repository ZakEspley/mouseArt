import random

from numpy import average

start = 400
overCounter = 0
overValues = []
exactCounter = 0
underCounter = 0
underValues = []
totalGames = 1000
totalRolls = 11
for _ in range(totalGames):
    tracker = start
    for __ in range(totalRolls):
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        
        if random.randint(0,1)==1:
            stringValue = str(d1) + str(d2)
        else:
            stringValue = str(d2) + str(d1)
        tracker = tracker - int(stringValue)
    
    if tracker<0:
        overCounter += 1
        overValues.append(tracker)
    elif tracker == 0:
        exactCounter += 1
    else:
        underCounter += 1
        underValues.append(tracker)

if len(overValues) > 0:
    avgover = average(overValues, axis=0)
else:
    avgover = "NA"

if len(underValues) > 0:
    avgunder = average(underValues, axis=0)
else:
    avgunder = "NA"

print(f"Went over {overCounter} times with average over being {avgover}")
print(f"Went under {underCounter} times with average under being {avgunder}")
print(f"Hit the mark exactly {exactCounter}")