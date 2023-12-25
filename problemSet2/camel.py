name = input("Enter name: ")

snake_case = ""
for i in name:
    if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        snake_case += "_" + i.lower()
    else:
        snake_case += i
print(snake_case)
