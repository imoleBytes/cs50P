import sys

def main():
    num_of_args = len(sys.argv)

    if num_of_args < 2:
        sys.exit("Too few command-line arguments")
    elif num_of_args > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.py'):
        sys.exit("Not a Python file")
    else:
        py_file = sys.argv[1]
        count = 0

        try:

            with open(py_file) as file:
                for line in file:
                    if line.strip() == '' or line.strip().startswith('#'):
                        continue
                    count += 1
            print(count)
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
