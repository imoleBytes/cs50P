def main():
    t = input("Enter time: ").strip().lower()
    final_time = convert(t)

    if final_time >= 7 and final_time <= 8:
        print("breakfast time")
    elif final_time >= 12 and final_time <= 13:
        print("lunch time")
    elif final_time >= 18 and final_time <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(":")
    h = eval(h)
    m = eval(m)
    h = h + m / 60
    return h


if __name__ == "__main__":
    main()
