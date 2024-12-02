# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ['Arnold', 'Francois', 'Elliot', 'Chase', 'Sandra']
    first_student = students[1]
    last_student = students[(len(students) - 1)]
    return(first_student, last_student)

# Call the function and print the result
print('Exercise 1:', manage_students())