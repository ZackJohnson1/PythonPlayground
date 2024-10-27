# while loop = execute some code WHILE some condition remains true
x
food = input("Enter a food you like (press Q to quit): ")

while not (food == "q" or food == "Q"):
    print(f"You like {food}")
    food = input("Enter a food you like (press Q to quit): ")

print("Bye!")
