import os

import csv

months = []
profit = []
total_profit_difference = 0
average_change = 0
max_profit = 0
min_profit = 0

# location
pybank_csv = os.path.join('Resources', 'budget_data.csv')
# turn into an object
with open(pybank_csv) as csvfile:
    # that you can read
    pybankreader = csv.reader(csvfile, delimiter = ",")
    # don't count headers
    next(pybankreader)
    # turn the tables into lists because python likes those better
    for row in pybankreader:
        months.append(row[0])
        profit.append(int(row[1]))
        # length and sum describer, append method
    print(len(months))
    print(sum(profit))
        
    for n in range(0, len(profit) - 1):
    # -1 tere so then at the end of the list it doesn't try to subtract row 86 from 87 that doesn't exist
    # += incremements a for loop to get a running total. sequentially adds to value y += x b is the same as y = x + b
        profit_difference = int(profit[n + 1]) - int(profit[n])
        if profit_difference > max_profit:
            max_profit = profit_difference
            max_month = months[n+1]
        if profit_difference < min_profit:
            min_profit = profit_difference
            min_month = months[n+1]
        total_profit_difference += profit_difference
        average_change = total_profit_difference / 85

    # print(total_profit_difference)
    # print(average_change)
    # print(max_profit)
    # print(min_profit)

final_pybank = os.path.join("Analysis", "pybank_table")

with open(final_pybank, "w") as datafile:
    datafile.write(f"""
    Financial Analysis:
    -------------------------------------------------------
    Total Months: {len(months)}
    Total: {sum(profit)}
    Average Change: {average_change}
    Greatest Increase in Profits: {max_month}, {max_profit}
    Greatest Decrease in Profits: {min_month}, {min_profit}\n""")

    print(f"""
    Financial Analysis:
    -------------------------------------------------------
    Total Months: {len(months)}
    Total: {sum(profit)}
    Average Change: {average_change}
    Greatest Increase in Profits: {max_month}, {max_profit}
    Greatest Decrease in Profits: {min_month}, {min_profit}\n""")

