import os
import csv
from types import ModuleType
import sys


budget_data = os.path.join('..', 'Python-Homework', 'budget_data.csv')




with open(budget_data, newline='') as budget_data: 
    data = csv.reader(budget_data, delimiter=',')
    header = next(data)
    data= [(row[0], int(row[1])) for row in data]



row_count = 0
pnl_total = 0 
great_curr = 0
monthly_diff = []
#monthly_sum = 0 
month_curr = tuple()
month_prev = tuple()
top_inc_month = ""
top_inc = 0
top_dec_month = ""
top_dec = sys.maxsize


for row in data:
  
    if (row_count == 0):
        month_prev = row
    else:
        month_curr = row
        great_curr = month_curr[1] - month_prev[1]
        least_curr = month_curr[1] - month_prev[1]
        if great_curr > top_inc:
            top_inc_month = row[0]
            top_inc = great_curr
        if least_curr < top_dec:
            top_dec_month = row[0]
            top_dec = least_curr

        month_prev = row
        monthly_diff.append(great_curr)
        # monthly_sum +=  great_curr

    
 
    row_count += 1
    profit = int(row[1])
    pnl_total += profit

monthly_sum = 0 
for val in monthly_diff: 
    monthly_sum = monthly_sum + val

avg_change = monthly_sum / len(monthly_diff)
#avg_change = monthly_sum / (row_count - 1)
avg_change = round(avg_change, 2)

print(row_count, len(monthly_diff))


        


#ref https://www.tutorialspoint.com/get-first-element-with-maximum-value-in-list-of-tuples-in-python
# from operator import itemgetter   
# max_monthly = max(data, key=itemgetter(1))
# min_monthly = min(data, key=itemgetter(1))

# max_monthly = max(data, key = lambda i : i(1))
# min_monthly = min(data, key = lambda i : i(1))

print('Finacial Analysis')
print("--------------------------------")
print(f"Total Months: {row_count}")
print(f"Total: ${pnl_total}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {top_inc_month}, (${top_inc})")
print(f"Greatest Decrease in Profits: {top_dec_month}, (${top_dec})")


#     Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

