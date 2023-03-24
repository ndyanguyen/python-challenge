import csv #Import csv module
import os  #importing operating system


#must use pybank in os.path.join. Since I need to do a clean up on my system
file1=os.path.join("pyBank","Resources","budgetdata.csv")

#create list to store data
budget_data=[]

with open(file1) as csvfile:
    reader=csv.DictReader(csvfile)

    #looping through data to store in dictionary. We are all adding the definitions into a list (budget_data)
    for row in reader:
        budget_data.append({"month": row["Date"], "amount": int(row["Profit/Losses"]),"change": 0})

#calculate the total months. Using the len function to count objects in data set
total_months=len(budget_data)

#print(total_months)
#looping the dictionary so we can calculate the changes between the months
prev_amount=budget_data[0]["amount"]
for i in range(total_months):
    budget_data[i]["change"]=budget_data[i]["amount"] - prev_amount
    prev_amount=budget_data[i]["amount"]
#print(budget_data) Checking work

#calculate total amount
total_amount=sum(row["amount"] for row in budget_data)
#print(total_amount)

#average change
#sum all of rows of change/total months
total_row_change=sum(row["change"] for row in budget_data)
average=round(total_row_change/(total_months-1),2)
#print(average)
#print(total_row_change)

great_increase=max(budget_data, key=lambda x:x["change"])
#print(great_increase)
great_decrease=min(budget_data,key=lambda x:x["change"])
#print(great_decrease)
#we use lambda to sort information we need. In this case we need the change and amount. Using the lambda function gives us what we're looking for

#Print all the info we have gathered
Final_Report=[("PyBank Analysis"),
(f'Total Months: {total_months}'),
(f'Total: {total_amount}'),
(f'Average Change: {average}'),
(f'Greatest Increase in Profits: {great_increase["month"]} ${great_increase["change"]}'),
(f'Greatest Decrease in Profits: {great_decrease["month"]} ${great_decrease["change"]}')]
print(Final_Report)



#transfer everything to a text file
#print must include file=*conversion*
#"w" must be included to write
#formatting became a little janky when trying to print (final_report) onto textfile. Wrote it out for clear understanding
file2=os.path.join("pyBank","Resources","pyBank_analysis.txt")

with open(file2,"w") as textfile:
    print("PyBank Analysis",file=textfile)
    print("----------------------", file=textfile)
    print(f'Total Months: {total_months}',file=textfile)
    print(f'Total: {total_amount}',file=textfile)
    print(f'Average Change: {average}',file=textfile)
    print(f'Greatest Increase in Profits: {great_increase["month"]} ${great_increase["change"]}', file=textfile)
    print(f'Greatest Decrease in Profits: {great_decrease["month"]} ${great_decrease["change"]}', file=textfile)


