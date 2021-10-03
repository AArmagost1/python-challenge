# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.


import os
import csv
import operator

poll_data = os.path.join('..', 'Python-Homework', 'election_data.csv')

with open(poll_data, newline='') as poll_data: 
    data = csv.reader(poll_data, delimiter=',')
    next(data)
    
    row= 0
    vote_count = [0, 0, 0, 0] 
    vote_total = 0
    candidate_list = []
    
    
    for row in data: 
        cadidnates = row[2]
        
        if(cadidnates not in candidate_list):
            candidate_list.append(cadidnates)
        if(cadidnates == candidate_list[0]):
            vote_count[0] += 1
        if(len(candidate_list) > 1 and cadidnates == candidate_list[1]):
            vote_count[1] += 1
        if(len(candidate_list) > 2 and cadidnates == candidate_list[2]):
            vote_count[2] += 1
        if(len(candidate_list) > 3 and cadidnates == candidate_list[3]):
            vote_count[3] += 1
        if(len(candidate_list) > 4 and cadidnates == candidate_list[4]):
            vote_count[4] += 1
        
        vote_total += 1
    
    
    can_0 = round((vote_count[0]/vote_total)*100, 2)
    can_1 = round((vote_count[1]/vote_total)*100, 2)
    can_2 = round((vote_count[2]/vote_total)*100, 2)
    can_3 = round((vote_count[3]/vote_total)*100, 2)



    cand_outcomes = {candidate_list[0]:can_0, 
                    candidate_list[1]:can_1, 
                    candidate_list[2]:can_2,
                    candidate_list[3]:can_3
    }
    
    
    highest_outcome = max(zip(cand_outcomes.values(), cand_outcomes.keys()))[1]
   
    

    # print(vote_total)
    # print(vote_count[0])
    # print(candidate_list)
    # print(can_0)

print('Election Results')
print('------------------------')
print(f'Total Votes: {vote_total}')
print('------------------------')
print(f'Khan: {can_0}% ({vote_count[0]})')
print(f'Correy: {can_1}% ({vote_count[1]})')
print(f'Li: {can_2}% ({vote_count[2]})')
print(f"O'Tooley: {can_3}% ({vote_count[3]})")
print('------------------------')
print(f'Winner: {highest_outcome}')

with open('pypoll_report.txt', 'w') as results:
    print('Election Results', file=results)
    print('------------------------', file=results)
    print(f'Total Votes: {vote_total}', file=results)
    print('------------------------', file=results)
    print(f'Khan: {can_0}% ({vote_count[0]})', file=results)
    print(f'Correy: {can_1}% ({vote_count[1]})', file=results)
    print(f'Li: {can_2}% ({vote_count[2]})', file=results)
    print(f"O'Tooley: {can_3}% ({vote_count[3]})", file=results)
    print('------------------------', file=results)
    print(f'Winner: {highest_outcome}', file=results)

        

    #     Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------