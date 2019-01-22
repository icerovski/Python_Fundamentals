student_grades = {
    'ivan': [3, 4],
    'petar': [5, 2, 5],
    'maria': [6, 6, 5, 6],
    'gosho': [5, 6]
}

sorted_grades = \
    sorted(student_grades.items(), \
           key=lambda kvp: kvp[0], \
           reverse= True) #sort by first letter of keys

print(sorted_grades)