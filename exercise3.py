student_name = (input('Enter your name:'))
gpa = float(input("Enter GPA (0.0-4.0): "))
credit = int(input('Enter the total credit hours:')) 
is_eligible = gpa >= 3.5 and credit >= 12







print(f'Name: {student_name}')
print(f'GPA: {gpa}')
print(f'Total credit hours: {credit}')
print(f'Student status: {"YES" if is_eligible else "NO"}')

