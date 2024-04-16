import sys
from tabulate import tabulate


def main():
    num_of_args = len(sys.argv)

    if num_of_args < 2:
        sys.exit("Too few command-line arguments")
    elif num_of_args > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith('.csv'):
        sys.exit("Not a CSV file")
    else:
        csv_file = sys.argv[1]
        try:
            with open(csv_file) as file:
                headers = file.readline().strip().split(',')
                table = []
                for row in file.readlines():
                    row_data = row.strip().split(',')
                    table.append(row_data)
            print(tabulate(table, headers, 'grid'))
        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
