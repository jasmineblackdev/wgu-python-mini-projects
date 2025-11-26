print("WGU Financial Aid Recommender")

gpa = float(input("What is your GPA? "))
income = int(input("What is your yearly income? $ "))
credits = int(input("How many credits are needed for this term? "))
student = input("Are you a First-gen student Yes or No? ").lower()

if gpa < 2.0:
    print("Not eligible. Improve GPA.")
elif gpa >= 3.5 and income < 40000:
    print("High priority grants + scholarships")
elif gpa >= 3.0 and 9 <= credits <= 12:
    print("Work-study or middle tier aid")
elif student == "yes" and income < 60000:
    print("First-gen scholarship resources available")

else:
    print("Standard aid options only - loans available.")

