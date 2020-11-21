#imports
import os
import csv

#create path to csv
csvpath = os.path.join('Resources', 'election_data.csv')

#create variables to be used later
vote_count=0
canidate_dict={}
total_votes=0
voter_string=""
current_winner=0
winner=""

#open the csv
with open(csvpath) as csvfile:

    #read the file in
    csvreader = csv.reader(csvfile, delimiter=',')

    # make the header so that it is seperate
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    #go through each row in the csv
    for row in csvreader:
        #add one to the vote count because each of these is a vote
        vote_count+=1
        #check if the canidate is in the canidate list and if not set the value of the dictionary equal to 1 
        if row[2] not in canidate_dict:
            canidate_dict[row[2]] =1

        #if not add one to the value of the dictionary
        else:
            canidate_dict[row[2]] += 1

    #go through each person in the dictionary and format so that all values are sent to a string
    for person in canidate_dict:
        voter_string+= "{}: ({}%) {}\n".format(person, round(((canidate_dict[person]/vote_count)*100),3),canidate_dict[person])
        #if the number of votes for a canidate is greater than the current winners votes then make that person the winner
        if canidate_dict[person] > current_winner:
            current_winner = canidate_dict[person]
            winner = person
    

    
    
  #print the output  
output = (
"Election Results \n" 
"------------------------------\n"
f'Total Votes: {vote_count}\n'
"------------------------------\n"
f'{voter_string}'
"------------------------------\n"
f'Winner: {winner}'




)
print(output)

#create and write output to the file
polling_analysis= open("polling_analysis.txt","w+")
polling_analysis.write(output)