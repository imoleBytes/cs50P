from datetime import date
import re


def main():
    """ Main program starts here"""

    user_input = input("Enter D.O.B (YYYY-MM-DD): ")
    dt = validate_date(user_input)
    print(user_input, 'is', dt)

    ...


def validate_date(dt):
    "YYYY-MM-DD"
    pattern = r"^([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

    matches = re.match(pattern, dt)
    if matches:
        return 'valid'
    else:
        return 'invalid'
    ...
...


if __name__ == "__main__":
    main()
