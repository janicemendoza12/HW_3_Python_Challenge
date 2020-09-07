import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")
os.getcwd()
#lists
current_change = []
current_profit = []
dates = []
#open file
with open (csvpath) as Financial_Data:
    csvreader = csv.reader(Financial_Data, delimiter=",")
    #define variables
    count = 0
    total_profit = 0
    previous_profit = 0
    average_change = 0
    is_first_row = True
   
   
#deal with header
    header = next(csvreader)
   

    for current_row in csvreader: 
        count = count + 1
        current_profit.append(int(current_row[1]))
        dates.append(current_row[0])

    for i in range(len(current_profit)-1):
        current_change.append(current_profit[i+1] - current_profit[i])
      
        total_profit = sum(current_profit)
        average_change = round(sum(current_change) / len(current_change))
        greatest_increase = max(current_change)
        

        least_increase = min(current_change)


    greatest_increase_index = current_change.index(greatest_increase)
    greatest_increase_date = dates[greatest_increase_index + 1]
    
    least_increase_index = current_change.index(least_increase)
    least_increase_date = dates[least_increase_index + 1]
#     print(least_increase_date)


print("Financial Analysis:")
print("\n")
print("Total Months: " + str(count))
print("Total: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(average_change))
print(f"Greatest Increase in Profits: " +(greatest_increase_date)+ "$" + str(greatest_increase))
print(f"Greatest Decrease in Profits: " +(least_increase_date)+ "$" + str(least_increase))
    
   
    


