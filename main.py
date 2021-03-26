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


#-----------------------

#silent action
