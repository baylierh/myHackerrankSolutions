# The provided code stub will read in a dictionary 
#  containing key/value pairs of name:[marks] for 
#  a list of students. Print the average of the marks 
#  array for the student name provided, with 2 decimal places.

# average() function is from py-introduction-to-sets.py
def average(arr):
    set_arr = set(arr)
    avg = sum(set_arr) / len(set_arr)
    rounded = round(avg, 2)
    return rounded

# Ask how many students will be entered
n = int(input("Enter n: "))

# Create a dictionary
student_marks = {}

# Ask for input and save it to a dictionary
for i in range(n):
    line = input("Name and marks of the student: ").split()
    name, scores = line[0], line[1:]
    scores = list(map(float, scores))
    student_marks[name] = scores
    #print(name, scores)

# Ask for a specific student's name
query_name = input("Enter a name: ")

# Find the average of that student's marks by 'searching'
#  their name in the student_marks dictionary
student_avg = average(student_marks[query_name])

# Print it out
print(query_name, "'s average: ", student_avg, sep ='')
#print("{:.2f}".format(student_avg)) 
# ^Format answer so that it passes on hackerrank