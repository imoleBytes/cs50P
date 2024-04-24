from datetime import date
import re, sys
from inflect import engine

def main():
    """ Main program starts here"""

    user_input = input("Date of Birth: ")
    is_date_valid = validate_date(user_input)
    if not is_date_valid:
        print('Invalid date')
        sys.exit(1)
    
    yy, mm, dd = user_input.split('-')

    day = date(int(yy), int(mm), int(dd))
    minutes = int((date.today() - day).total_seconds() / 60)
    # minutes = int((date(2000,1,1) - day).total_seconds() / 60)

    word_engine = engine()
    words = word_engine.number_to_words(minutes, andword='')
    
    print(words.capitalize(), 'minutes')

    
    # d1 = date(2000,1,1)
    # d2 = date(1999,1,1)
    # mn = int((d1-d2).total_seconds() / 60)
    # wrds = word_engine.number_to_words(mn, andword='')
    # print(wrds, 'minutes')
    # wrds = word_engine.number_to_words(mn)
    # print(wrds, 'minutes')
    

def validate_date(dt):
    # "YYYY-MM-DD"
    # pattern = r"^([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    yyyy = "(0{3}[1-9]|0{2}[1-9][0-9]|0[1-9][0-9]{2}|[1-9][0-9]{3})"
    mm = "(0[1-9]|1[0-2])"
    dd = "(0[1-9]|[12][0-9]|3[01])"
    pattern = fr"^{yyyy}-{mm}-{dd}$"

    matches = re.match(pattern, dt)
    if matches:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
