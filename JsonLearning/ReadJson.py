import json
import math
import statistics

"""IMport Data directly"""
"""//
Student = '''
{
"S1": {
    "Name": "Rakesh",
    "Age": 14,
    "Sex": "Male",
    "class": 9, 
    "Section": "A", 
    "School Name": "Cheran Metric School",
    "Father Name": "Kumar", 
    "State" : "Tamil Nadu", 
    "Pincode" : 639001
    }
}
'''

//
"""
# JSON File Loaded from File
with open('Students.json', 'r') as file:
    student = json.load(file)

# Reterive the student details who has name starts with 'A'
students_with_a = {key: value for key, value in student.items() if value['Name'].startswith('A')}
print(students_with_a)
print()
# Print the filtered students whose name starts with A
for student_id, student_info in students_with_a.items():
    print("Student ID : ", student_id, " Student Name : ", student_info['Name'])

total_age = 0
no_of_students = 0

# TO find the average age of all students
for student_info in student.values():
    total_age += student_info['Age']
    no_of_students += 1

if (no_of_students > 0):
    avg_Student_age = math.ceil(total_age / no_of_students)
    print("Average Student Age : ", avg_Student_age, ". No. of Students : ", no_of_students)
else:
    print("No Students Found")

# TO Find the average age of Male Students

m_total_age = 0
no_of_m_students = 0

for student_info in student.values():
    if (student_info['Sex'] == 'Male'):
        m_total_age += student_info['Age']
        no_of_m_students += 1

if (no_of_m_students > 0):
    avg_m_Student_age = math.ceil(m_total_age / no_of_m_students)
    print("Average Male Student Age : ", avg_m_Student_age, ". Number of Male Students : ", no_of_m_students)
else:
    print("No Male Students Found")

# Calculate the Median of Age of Male Students
male_ages = [student_info['Age'] for student_info in student.values() if student_info['Sex'] == 'Male']

# Sort the ages
male_ages.sort()

# Calculate the median
if male_ages:
    median_age = statistics.median(male_ages)
    print("Median Age of Male Students:", median_age)
else:
    print("No male students found.")
