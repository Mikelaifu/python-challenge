

import pandas as pd
filecsvname = input("name of first file: ")
    
# "election_data_1.csv", "election_data_2.csv"
data = pd.read_csv(filecsvname) 

Total = int(data.index.size)
print("Election Results")
print("Total Votes : ", str(Total))
print("-----------------------------------")


candi_name = data["Candidate"].unique()
candi_name # get candidate name 
candi_count = data.groupby("Candidate")
candidate_count = candi_count.agg({'Voter ID':"count"})["Voter ID"].tolist()

percentage = []
for i in range(len(candidate_count)):
    percentage.append((candidate_count[i]/Total))
lst = []
for i in range(len(candidate_count)):
    x= candi_name[i] + ": " + str("{:.2%}".format(percentage[i])) + " (" + str(candidate_count[i]) + ")"
    print(x)
    lst.append(x)


candidate_winner = candi_count.agg({'Voter ID':"count"}).sort_values(by = "Voter ID", ascending=False )

print("-------------------------------------")
print("Winner : ", candidate_winner.index[0])

f = open("Output_analysis.txt" , "w")
f.write("Election Results"+ "\n")
f.write("Total Votes : "+ str(Total) + "\n")
f.write("-------------------------------------"+ "\n")
f.write(lst[0] + "\n")
f.write(lst[1] + "\n")
f.write(lst[2] + "\n")
f.write(lst[3] + "\n")
f.write("-------------------------------------" + "\n")
f.write("Winner : "+ candidate_winner.index[0] + "\n")
f.close()
    



