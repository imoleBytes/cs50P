import re
import sys


def main():
    print(convert(input("Hours: ")))


def conv(hr, min, meridian):
    hr = int(hr)

    if meridian == 'AM':
        if hr == 12:
            hr = 0
    else:
        hr += 12
        if hr == 24:
            hr = 12
    if not min:
        min = '00'
    if hr < 10:
        return f"0{hr}:{min}"
    return f"{hr}:{min}"


def convert(s: str) -> str:
    pattrn = r"^([1-9]|1[012]):?([0-5][0-9])? ([AP]M) to ([1-9]|1[012]):?([0-5][0-9])? ([AP]M)$"

    matches = re.search(pattrn, s)
    if not matches:
        raise (ValueError)
    fro = conv(matches.group(1), matches.group(2), matches.group(3))
    to = conv(matches.group(4), matches.group(5), matches.group(6))

    return (f"{fro} to {to}")


if __name__ == "__main__":
    main()
