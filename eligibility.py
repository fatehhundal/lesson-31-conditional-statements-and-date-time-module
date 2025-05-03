print("Welcome. This is a program that calculates your eligibility to take your exams, basing it off your attendance in school.")

student_name = input("What is your name? ")
working_days = int(input("How many days do you have of school? "))
student_absent_days = int(input("How many days have you been absent for? "))

student_present_days = working_days - student_absent_days

if (student_present_days/working_days)*100 < 75:
    print("Your attendance rate (in %) is", (student_present_days/working_days)*100)
    print("Your aren't able to take your exams.")
else:
    print("Your attendance rate (in %) is", (student_present_days/working_days)*100)
    print("You are able to take your exams.")