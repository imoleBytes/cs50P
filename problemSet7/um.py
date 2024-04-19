import re


def main():
    print(count(input("Text: ")))


# def count(s: str) -> int:
#     s = s.lower()
#     c = len([i for i in s.split() if i == 'um'])
#     return c
#     ...

def count(s: str) -> int:
    s = s.lower()
    pattern = r"\bum\b"
    matches = re.findall(pattern, s)
    return (len(matches))


if __name__ == "__main__":
    main()
