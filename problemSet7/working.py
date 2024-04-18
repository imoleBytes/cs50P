import re
import sys



# '9:00 AM to 5:00 PM'
# '9 AM to 5 PM'


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    # 
    # print(f)
    pattrn = r"^([1-9]|1[012]) [AP]M to ([1-9]|1[012]) [AP]M$"

    if not (re.search(pattrn, s)):
        return 'invalid'
        ...
    
    first, sec = s.split(' to ')
    hr_first, meri_first = first.split()
    hr_sec, meri_sec = sec.split()
    if meri_first == 'PM':
        hr_first = int(hr_first) + 12
    if meri_sec == 'PM':
        hr_sec = int(hr_sec) + 12
    return (f"{hr_first}:00 to {hr_sec}:00")


if __name__ == "__main__":
    main()
