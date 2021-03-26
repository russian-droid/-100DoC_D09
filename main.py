#following Udemy course: 100 days of code by Angela Yu

#-----------------------change score to grade in dict
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#create a new empty dict
student_grades = {}

#loops via list
for student in student_scores:
    #takes an element (key=student) and assigns it to a var
    score = student_scores[student]
    #checks and changes the value
    if score <= 70:
      student_grades[student] = 'Fail'
    elif score <+ 80:
      student_grades[student] = 'Acceptable'
    elif score <= 90:
      student_grades[student] = 'Exceeds Expectations'
    else:
      student_grades[student] = 'Outstanding'

print(student_grades)


#-----------------------travel log
#Nesting Dictionaries in Lists: a list of dict [ {},{},{} ]
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
    #create a new dict which we'll add to the list of dict later    
    new_country={}
    #add each element into the new dict
    new_country['country']=country
    new_country['visits']=visits
    new_country['cities']=cities
    #now we add the dict into the list of dict
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


#-----------------------silent action
bids={}

running = True
while running: #same as: while running == True
    print('\033c') #Use this to clear screen between users
    print('----------------SECRET AUCTION-----------------\n')
    user_name = input("Enter your name:\n")
    user_bid = int(input("Your bid:\n$"))

    #add each element into the new dict
    bids[user_name]=user_bid

    running_flag = input("Another bid?\n(enter 'y' for yes, or 'n' for no)\n")
    if running_flag == 'n':
        running = False
        print('\033c') #clear screen
    #else - don't need it here, because it'll pass this way anyways

#find the key that has highest value
max_key=max(bids, key=bids.get)
#find the highest value
max_value=max(bids.values())

'''
#or we can go simple way, without fancy functions:
#var to keep the heighest bidder
highest_bid = 0
#var to keep winners name
winner = ''
#loop through
for bidder in bids:
#assign to var
bid_amount = bids[bidder]
#if it's bigger, change it
if bid_amount > highest_bid: 
    highest_bid = bid_amount
    winner = bidder
print(f"The winner is {winner} with a bid of ${highest_bid}")
'''

print('----------------SECRET AUCTION-----------------\n')
print(f'\nThe winner is _{max_key}_ with the highest bid of _${max_value}_\n')
