
while True:
    user = input("Fraction: ")
    ls = user.split("/")
    if len(ls) != 2:
        continue
    try:
        n = int(ls[0])
        d = int(ls[1])
        c = (n / d) * 100

    except:
        continue
    if c <= 1:
        print("E")
    elif c >= 99 and c <= 100:
        print("F")
    elif c > 100:
        continue
    else:
        print("{:.0f}%".format(c))
    break
