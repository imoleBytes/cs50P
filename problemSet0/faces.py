def main():
    user = input()
    print(convert(user))


def convert(s):
    if ":)" in s:
        s = s.replace(":)", "🙂")
    if ":(" in s:
        s = s.replace(":(", "🙁")
    return s

main()
