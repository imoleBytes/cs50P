def main():
    user_input = input("Enter: ")

    newStr = shorten(user_input)
    print(newStr)

def shorten(word):
    new_word = "".join([i for i in word if i not in "AEIOUaeiou"])
    return new_word


if __name__ == "__main__":
    main()