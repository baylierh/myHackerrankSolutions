# The provided code stub will read in a dictionary 
#  containing key/value pairs of name:[marks] for 
#  a list of students. Print the average of the marks 
#  array for the student name provided, with 2 decimal places.

n = int(input("Enter n: "))
student_marks = {}

for i in range(n):
    line = input("Name and marks of the student: ").split()
    name, scores = line[0], line[1:]
    scores = list(map(float, scores))
    student_marks[name] = scores
    print(name, scores)


print(student_marks)

#query_name = input("Enter a name: ")