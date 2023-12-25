greet = input("Greeting: ").strip().lower()

balance = 0

if greet.startswith("hello"):
    balance = 0
elif greet.startswith("h") and not greet.startswith("hello"):
    balance = 20
else:
    balance = 100

print(f"${balance}")
