import re
import sys


def main():
    print(parse(input("HTML: ").strip()))
    # parse(input("HTML: ").strip())


def parse(s):
    pt = r'^.+?src="https?://(www\.)?youtube\.com/embed/(.+?)"'

    matches = re.search(pt,s)
    if matches:
        user_id = matches.group(2)
        shorter_url = f"https://youtu.be/{user_id}"
        return shorter_url
    return None


if __name__ == "__main__":
    main()
