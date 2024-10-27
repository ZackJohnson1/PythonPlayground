# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")

while True:
    if name.strip() == "":                                          # Strips any whitespace
        print("You did not enter your name. Please try again.")     # If the line below isnt there the loop = infinite 
        name = input("Enter your name: ")                           # input is outside the while loop; add again
    else:
        print(f"Hello {name}")
        break