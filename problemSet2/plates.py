from string import digits, ascii_uppercase, punctuation



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def no_middle_number(s):
    index = -1
    for i in s:

        index += 1
        if i in digits:
            if i == "0":
                return False
            break
    for l in s[index:]:
        if l in ascii_uppercase:
            return False
    return True



def is_valid(s):
    lenght = len(s)
    if lenght < 2 or lenght > 6:
        return False

    if not (s[0] in ascii_uppercase and s[1] in ascii_uppercase):
        return False
    for i in s:
        if i in f" {punctuation}":
            return False
    if s.isalpha():
        return True
    return no_middle_number(s)


main()
