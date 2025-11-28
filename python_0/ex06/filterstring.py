import sys


def filterstring(s: str, n: int) -> list:
    """filterstring(s: str, n: int) -> filter list

Returns a list containing only the words in str whose
lengths are greater than n."""

    result = []
    split = s.split(" ")
    for word in split:
        if len(word) > n:
            result.append(word)
    return (result)


def check_error(s: str, n: str) -> bool:
    """check_error(s: str, n: str) -> bool

Returns true if s and n are valid, false otherwise."""

    return True if not s or not n.isdigit() else False


def main():
    """Main filterstring.py"""

    if len(sys.argv) == 2 and sys.argv[1] == "--doc":
        print("__DOC__:")
        print(filterstring.__doc__)
        print("\n----\n")
        print(check_error.__doc__)

    elif len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")

    elif check_error(sys.argv[1], sys.argv[2]):
        print("AssertionError: the arguments are bad")

    else:
        ret = filterstring(sys.argv[1], int(sys.argv[2]))
        print(ret)


if __name__ == "__main__":
    main()
