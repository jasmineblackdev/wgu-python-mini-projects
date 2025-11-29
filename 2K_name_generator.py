import random
print("Welcome to MyPlayer name generator")

f_name = ["Liam", "Noah", "Mateo", "Elijah", "Lucas", "William", "Benjamin", "Levi", "Ezra", "Sebastian", "Jack", "Daniel",
"Samuel", "Michael", "Ethan", "Asher", "John", "Hudson", "Luca", "Leo", "Elias", "Owen", "Alexander", "Dylan", "Santiago",
"Julian", "David", "Joseph", "Matthew", "Luke", "Jackson", "Maverick", "Miles", "Wyatt", "Thomas" ]
l_name = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Lee",
"Gonzalez", "Hernandez", "Black", "Evans", "Anderson" , "Thomas", "Moore", "King", "White", "Thompson" ]

question1 = int(input("How many random names do you want? \n"))


for i in range(question1):
    first = random.choice(f_name)
    last = random.choice(l_name)
    print("Your 2K Player name is: " ,first, last)