import validators


def main():
    email = input("What's your email address? ")
    if bool(validators.email(email)):
        print('Valid')
    else:
        print('Invalid')


if __name__ == "__main__":
    main()