print("Welcome to WGU Graduation Checker")

credits_done = int(input("How many credits have you completed? "))
credits_needed = int(input("How many credits needed to graduate? "))
gpa = float(input("What is your GPA? "))
capstone = input("Did you pass your capstone Yes or No? ").lower()

if credits_done >= credits_needed and gpa >= 2.0 and (capstone == "yes"):
    print("You are eligible to graduate")
elif credits_done >= credits_needed and gpa < 2.0:
        print("You have enough credits but need a higher GPA.")
elif credits_done < credits_needed and (capstone == "yes"):
            print("You passed capstone but still need more credits.")
else:
    print("You still need more credits and must pass the capstone.")