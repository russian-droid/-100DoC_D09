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


#-----------------------
#silent action
