print("Welcome to WGU Term Load Advisor")

question = input("Work full-time Yes or No: ").lower()

if question == "yes" or question == "Yes":
    question_2 = int(input("How many course this term? "))
    if question_2 >= 4:
        print("To heavy")
    elif question_2 >= 2 and question_2 <= 3:
        print("Balanced")
    else:
        print("Very light")
if question == "no" or question == "No":
    question_3 = int(input("How many course this term? "))
    if question_3 >= 6:
        print("Too heavy")
    elif question_3 >= 3 and question_3 <=5:
        print("Balanced")
    else:
     print("Very light")
