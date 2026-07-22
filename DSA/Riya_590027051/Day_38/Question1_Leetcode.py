# Number of students
n = int(input("Enter number of students: "))

# Student preferences
students = list(map(int, input("Enter student preferences: ").split()))

# Sandwiches in stack order
sandwiches = list(map(int, input("Enter sandwiches: ").split()))

# Count students who prefer each type of sandwich
count = [0, 0]

for student in students:
    count[student] += 1

# Process sandwiches from top to bottom
for sandwich in sandwiches:
    if count[sandwich] == 0:
        break

    count[sandwich] -= 1

# Students who are unable to eat
unable_to_eat = count[0] + count[1]

print("Number of students unable to eat:", unable_to_eat)