user_input = input("Enter: ")

newStr = "".join([i for i in user_input if i not in "AEIOUaeiou"])
print(newStr)
