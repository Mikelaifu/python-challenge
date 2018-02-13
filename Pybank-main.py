import pandas as pd

csvfile = input("csv file you want to get analyzed : ")
# budget_data_1.csv

data = pd.read_csv(csvfile)
countmonth = data["Date"].count()-1
total_rev = data["Revenue"].sum()
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(countmonth) )
print("Total Revenue: $" + str(total_rev) )
#--------------------------get change, total, min, max------------------------
revchange = []
dictt = {}
count = 0

date = []
Date = data["Date"]
rev = data["Revenue"]
for i in range(0 , len(rev)-1):
    revchange.append(rev[i+1] - rev[i])
# get number of change
for j in revchange:
    count = count + 1
# get total change
total_change = sum(revchange)
# avg change
avgRev_change = total_change / count
print("Average Revenue Change: $" + str(avgRev_change))
for a in range(0, len(revchange) -1):
    date.append(Date[a])

for b in range(0, len(date) -1):
    dictt[date[b]] = revchange[b]
    
max_incr = max(dictt.values())
min_incr = min(dictt.values())  ## get the max and min value 
# get month according to the value
MaxMin_date = []
for key, value in dictt.items():
    if value == max_incr:
        MaxMin_date.append(key)
    if value == min_incr:
        MaxMin_date.append(key)
print("Greatest Increase in Revenue: " + str(MaxMin_date[0]) + " ($" + str(max_incr) + ")")
print("Greatest Decrease in Revenue: " + str(MaxMin_date[1]) + " ($" + str(min_incr) + ")")

f = open("Output_analysis.txt" , "w")
f.write("Financial Analysis"+ "\n")
f.write("----------------------------"+ "\n")
f.write("Total Months: " + str(countmonth) + "\n")
f.write("Total Revenue: $" + str(total_rev)+ "\n")
f.write("Average Revenue Change: $" + str(avgRev_change)+ "\n")
f.write("Greatest Increase in Revenue: " + str(MaxMin_date[0]) + " ($" + str(max_incr) + ")"+ "\n")
f.write("Greatest Decrease in Revenue: " + str(MaxMin_date[1]) + " ($" + str(min_incr) + ")"+"\n")
f.close()


