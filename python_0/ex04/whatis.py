import sys


def ScriptCheckNb(nb: str) -> str:
    i = 0
    while nb[i] == '-' or nb[i] == '+':
        i += 1
    if not nb[i:].isnumeric():
        return "AssertionError: argument is not an integer"
    return "I'm Even." if int(nb) % 2 == 0 else "I'm Odd."


def main():
    if len(sys.argv) < 2:
        return
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        print(ScriptCheckNb(sys.argv[1]))


if __name__ == "__main__":
    main()
