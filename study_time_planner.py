print("Welcome to the study Time Planner!")
question = int(input("How many courses this term?"))
question_2 = int(input("How many hours per week can you study"))
required_hours = question * 12

if question_2 >= required_hours:
    print("You are on track!")
else:
    print("You may fall behind. \n Consider reducing courses.")