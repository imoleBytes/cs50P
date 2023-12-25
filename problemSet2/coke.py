due = 50

while True:
    print(f"Amount Due: {due}")

    accepts = input("Insert Coin: ")
    if accepts in ["25", "10", "5"]:
        due = due - eval(accepts)
        if due <= 0:
            print(f"Change Owed: {due * (-1)}")
            break
        else:
            continue
