import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))

# "255.255.255.255"


# "255"
# sub_patt = "[1-2]?[0-5]?[0-5]"
# sub_patt = '([0-1]?[0-9]?[0-9])|(2[0-5]?[0-5])'

sub_patt = '(0|[1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])'




def validate(ip: str)-> bool:
    # pattern ="^((([0-2])?(([0-5])?){2})|0\.){3}(([0-2])?(([0-5])?){2})|0$"
    pattern = fr"^{sub_patt}\.{sub_patt}\.{sub_patt}\.{sub_patt}$"

    if re.search(pattern, ip):
        return True
    return False


if __name__ == "__main__":
    main()