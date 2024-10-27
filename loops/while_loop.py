# while loop = execute some code WHILE some condition remains true

while True:
    name = input("Enter your name: ")
    if name.strip() == "":
        print("You did not enter your name. Please try again.")
    else:
        print(f"Hello {name}")
        break