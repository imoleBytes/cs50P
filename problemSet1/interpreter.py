exp = input("Enter file: ").strip().lower()

x, y, z = exp.split(" ")
x = int(x)
z = int(z)
answer = 0

if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z

print(f"{answer:.1f}")
