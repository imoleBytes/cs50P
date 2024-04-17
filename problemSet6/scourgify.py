import sys, csv

def main():


    num_args = len(sys.argv)

    if num_args < 3:
        sys.exit("Too few command-line arguments")
    elif num_args > 3:
        sys.exit("Too many command-line arguments")
    else:
        before = sys.argv[1]
        after = sys.argv[2]

        try:
            with open(before) as file:
                reader = csv.DictReader(file)
                f2 = open(after, "a")

                for row in reader:
                    first, last = row['name'].split(', ')
                    house = row['house']
                    writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
                    writer.writerow({'first': first, 'last': last, 'house': house})
                f2.close()
        except FileNotFoundError:
            sys.exit(f"Could not read {before}")


if __name__ == "__main__":
    main()