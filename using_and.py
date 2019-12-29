#A student makes honour roll if their avarage is >=85
# and their lowest grade is not below 70

gpa = float(input('What was your Grade Point Avarage? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85:
    if lowest_grade >= .70:
        print('You made the honour roll')