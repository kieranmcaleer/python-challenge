import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#set month count equal to zero so we can count them later
month_count = 0 

#set profit loss equal to zero so we can total it later
profit_loss = 0

#start with setting previous profit to zero
previous_profit=0

#start with setting current profit equal to zero
current_profit =0

#create an empty list so that we can calculate the average change
profit_loss_list=[]

#create a variable that will hold the final average after going through the list
final_average_profit=0

#greatest profit variable
greatest_profit=0

#greatest month variable
greatest_month=""

#least profit variable
least_profit=0
#least month variable
least_month=""

#open the csv path that we created earlier
with open(csvpath) as csvfile:

    #read the file in
    csvreader = csv.reader(csvfile, delimiter=',')

    # make the header so that it is seperate
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    #go through each row in the csv
    for row in csvreader:
        #add 1 to the month count because each row is a month
        month_count +=1

        #add the the second column to the profit loss so that we can total it
        profit_loss += int(row[1])

        #set the current profit to equal the second row that we are currently on
        current_profit = int(row[1])

        #calculate the average profit between this row and the previous row
        average_profit = current_profit - previous_profit
    
        #now set the previous row to the current one so that we can use it next time we loop
        previous_profit = int(row[1])

        #add the average profit to a list for later use
        profit_loss_list.append(average_profit)


        #compare weather the average profit is greater than the current greatest profit
        if average_profit > greatest_profit:
            greatest_profit=average_profit
            greatest_month= row[0]

        #compare weather the average profit is less than the least profit
        if average_profit < least_profit:
            least_profit=average_profit
            least_month= row[0]
    #calculate the final average profit by taking the sum of all in the list and dividing it by the length of that list
    final_average_profit=sum(profit_loss_list)/len(profit_loss_list)
    
s

  
        
#print Everything out
output = (
"Financial Analysis \n" 
"------------------------------\n"

f'Total Months: {month_count}\n'

f'Total: ${profit_loss}\n'
f'Average Change: ${round(final_average_profit,2)}\n'
f'Greatest Increse in Profits: {greatest_month} (${greatest_profit})\n'
f'Greatest Decrese in Profits: {least_month} (${least_profit})\n'
)
print(output)

#create and write output to the file
financial_analysis= open("financial_analysis.txt","w+")
financial_analysis.write(output)

    


