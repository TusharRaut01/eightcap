#list of subjects
subjects = []

#No of subject
num_subject=int(input('Enter the no. of subject: '))
#Names of subject form user
for i in range(num_subject):
    subject_name = input(f"Enter the name of subject {i + 1}: ")
    subjects.append({'Name': subject_name})


#list of student 
students = []

#No of student
num_students = int(input("Enter the number of students: "))
#for loop for each student
for i in range(num_students):
    #Dictionary for each student
    student_info = {}
    
    #Name of each student
    student_name = input(f"Enter the name of student {i + 1}: ")
    student_info['Name'] = student_name
    
    #marks for each subject
    for subject in subjects:
        marks = float(input(f"Enter {subject['Name']} marks for {student_name}: "))
        student_info[subject['Name']] = marks
    
    # Calculate total marks for each student
    total_marks = sum(student_info[subject['Name']] for subject in subjects)
    student_info['Total Marks'] = total_marks
    
    #Calculate percentage for each student
    percentage_marks = (total_marks / (num_subject * 100))*100
    student_info['Percentage '] = percentage_marks
    

    #grade for each student
    if percentage_marks==100:
        Grade = 'O'
    elif percentage_marks>=90:
        Grade = 'A'
    elif percentage_marks>=80:
        Grade = 'B'
    elif percentage_marks>=70:
        Grade = 'C'
    elif percentage_marks>=60:
        Grade = 'D'
    else:
        Grade = 'PASS'
    
    student_info['Grade'] = Grade
    
    # Append the student information to the list of students
    students.append(student_info)

# Print the information for each student
for student in students:
    print("\nStudent Information:")
    for key, value in student.items():
        print(f"{key}: {value}")
