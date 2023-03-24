import csv #import csv
import os #import operating system

#bring in the election data csv. Again use pyPoll instead of ..
file1=os.path.join("pyPoll","Resources","election_data.csv")

#open election data and read the first row which is header row
with open(file1, newline="") as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csvheader=next(csvreader)
    candidate_roster=[candidate[2] for candidate in csvreader]
#print(candidate_roster)
#list comprehension. basically addd candidates into a list of the row of candidate in the file, [2] starts at row 2

#calculate the number of votes. We can use len to count the votes by counting the rows of candidate_roster
vote_total=len(candidate_roster)
#print(vote_total) !
##1 solved

#List comprehension. Give me the candidate and the amount of votes they have from the dataset that we created earlier (candidate roster)
#how many ballots have the candidates names on it
candidate_votes=[[candidate,candidate_roster.count(candidate)] for candidate in set(candidate_roster)]
#print(candidate_votes) !
candidates_sorted=sorted(candidate_votes, key=lambda x:x[1], reverse=True)
#print(candidates_sorted) !
# #2 and #4 solved on module 3 challenges. Able to list Candidates that recieved votes as well as how much each got 

#get all the candidates in the index and divide them by vote total. Then multiply by 100 to get percentage
for candidate in candidates_sorted:
    percentage=(candidate[1]/vote_total)*100
    print(f'{candidate[0]}:{percentage:6.3f}%({candidate[1]})') #! 
#3

#print the final winner
#We use the function on candidates sorted because it has the candidates ordered from Descending order. With that, the index [0][0] will always have the winner of the poll.
#ripnt(f'{candidates_sorted[0][0]}') !

print("--------------------------------------------")
print("The total of votes are "+ str(vote_total))
print(candidates_sorted)
print("Above are the candidates who recieved votes")
for candidate in candidates_sorted:
    percentage=(candidate[1]/vote_total)*100
    print(f'{candidate[0]}: {percentage:6.3f}% ({candidate[1]}) Candidate info')
print(f'{candidates_sorted[0][0]} is the winner')

analysis_file=os.path.join("pyPoll","Resources","pyPoll_analysis.txt")

with open(analysis_file, "w") as txtfile:
    print("--------------------------------------------", file=txtfile)
    print("The total of votes are "+ str(vote_total), file=txtfile)
    print(candidates_sorted, file=txtfile)
    print("Above are the candidates who recieved votes", file=txtfile)
    for candidate in candidates_sorted:
        percentage=(candidate[1]/vote_total)*100
        print(f'{candidate[0]}: {percentage:6.3f}% ({candidate[1]}) Candidate info', file=txtfile)
    print(f'{candidates_sorted[0][0]} is the winner', file=txtfile)