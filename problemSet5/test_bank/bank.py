def main():
    greet = input("Greeting: ").strip().lower()

    bal = value(greet)

    print(f"${bal}")


def value(greeting):
    balance = 0

    if greeting.startswith("hello"):
        balance = 0
    elif greeting.startswith("h") and not greeting.startswith("hello"):
        balance = 20
    else:
        balance = 100
    return balance

if __name__ == "__main__":
    main()
