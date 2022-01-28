# Modules
import os
import csv
from typing import Dict

# Set path to file
csvpath = os.path.join("budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    # Read the header row
    header = next(csvreader)
    num_months = 0
    profit_loss = 0
    current_month = [] # month tracker
    current_profit_list = [] # profit for current month tracker
    max_profit = []
    min_profit = []
    net_total = [] 
    months_total = []
   


    #loop through counting the number of months
    for row in csvreader:

        num_months = num_months + 1
        profit_loss = float(profit_loss) + float (row[1])
        net_total.append(profit_loss)   
        months_total.append(num_months)
        greatest_increase = max(net_total)
        month_increase = months_total[net_total.index(greatest_increase)]
        greatest_decrease = min(net_total)
        month_decrease = months_total[net_total.index(greatest_decrease)]



print("Total Months: " + str(num_months))
print("Total: $" + str(profit_loss))
avg_chg = float(profit_loss) / float(num_months)
print("Average Change: $" + str(avg_chg))

#find min and max values in column 2

# for row in csvreader:
#     lastmonth_profit = int(row[1]) # determines whether this month is higher or lower
#     current_profit = int(row[1]) - lastmonth_profit #this resets the profit/loss to current
#     current_profit_list = current_profit_list + current_profit
#     current_month = current_month + (row[0])
#     if current_profit > max_profit[1]:
#         max_profit[0] = row[0]    
#         max_profit[1] = current_profit
#     if current_profit < min_profit[1]:
#         min_profit[0] = row[0]
#         min_profit[1] = current_profit




# print(max_profit)[0] + max_profit[1]
# print(min_profit)[0] + min_profit[1]

# print("The greatest increase in profits " + {str[month_increase + greatest_increase]})
# print("The greatest increase in profit: " + str(month_increase) + str(greatest_increase)

# print("The decrease increase in profits " + {month_decrease} + {greatest_decrease})    



