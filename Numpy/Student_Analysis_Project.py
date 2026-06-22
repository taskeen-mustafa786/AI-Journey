# Student Marks Analysis

import numpy as np

marks = np.array([
    [90,85,88],
    [70,75,80],
    [95,92,97],
    [50,45,60],
    [78,82,85]
])

# Assuming Column 0,1,2 as MAth, Physics, Chemistry in order.

## Finding total numbers of students:

marks_shape = marks.shape
total_num_of_students = marks_shape[0]

print(" Total number of students : ",total_num_of_students)

## Average marks of each student
print("Average marks of each student are : ",np.mean(marks,axis=1))

## Average marks of each subject
subject_avg_marks = np.mean(marks,axis=0)
print("Average marks of each subject are : ",subject_avg_marks)

## Highest marks in entire dataset 
print("Highest marks in entire dataset : ",np.max(marks))

## Lowest marks in entire dataset 
print("Lowest marks in entire dataset : ",np.min(marks))

## Student average marks greater than 80

### _Average marks of students
avg_marks = np.mean(marks,axis=1)

### _Greater than 80
toppers = np.where(avg_marks>80)[0]
print("Student with average marks greater than 80 are Toppers")
print("Toppers are : ")
for i in toppers:
    print("Student ",i+1)

## Topper Student
print(" Topper student is Student ",np.argmax(avg_marks)+1)

## Number of Pass Students
pass_students = np.size(avg_marks[avg_marks>=50])
print("Pass = ",pass_students)

## Number of fail students
fail_students = total_num_of_students - pass_students
print("Fail = ",fail_students)

## Printing each subject average marks without hardcoding:
subjects = ["Math", "Physics", "Chemistry"]

for i in range(len(subjects)):
    print(f"{subjects[i]} average = ",subject_avg_marks[i])