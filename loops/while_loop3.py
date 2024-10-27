# while loop = execute some code WHILE some condition remains true

age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be a negative number")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")