import re

# url = input("URL: ").strip()

# if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#     print(matches.groups())
#     print(f"Username:", matches.group(1))

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(matches.groups())
    print(f"Username:", matches.group(2))


# name = input("What's your name? ").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last, first = matches.groups()
#     print(matches.groups())
    # name = first + " " + last
# print(f"hello, {last}")
