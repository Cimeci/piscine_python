import sys


def count_character(text: str):
    """Print the total number of characters in the string"""
    print("The text contains", len(text), "characters:")


def count_upper_letters(text: str):
    """Print the total number of uppers characters in the string"""
    count = sum([1 if c.isupper() else 0 for c in text])
    print(count, "upper letters")


def count_lower_letters(text: str):
    """Print the total number of lowers characters in the string"""
    count = sum([1 if c.islower() else 0 for c in text])
    print(count, "lower letters")


def count_ponctuation_marks(text: str):
    """Print the total number of ponctuations marks in the string"""
    punct = "'.,;:?!"
    count = sum([1 if c in punct else 0 for c in text])
    print(count, "punctuation marks")


def count_space(text: str):
    """Print the total number of spaces characters in the string"""
    count = sum([1 if c.isspace() else 0 for c in text])
    print(count, "spaces")


def count_digits(text: str):
    """Print the total number of digits characters in the string"""
    count = sum([1 if c.isdigit() else 0 for c in text])
    print(count, "digits")


def process(text: str):
    """Call all the function"""
    count_character(text)
    count_upper_letters(text)
    count_lower_letters(text)
    count_ponctuation_marks(text)
    count_space(text)
    count_digits(text)


def readline() -> str:
    """Read standard input if not argv[1]"""
    print("What is the text to count?")
    line = sys.stdin.readline()
    if line == "":
        return ""
    return line


def main():
    """Main building.py"""
    if len(sys.argv) < 2:
        text = readline()
        process(text)
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    else:
        process(sys.argv[1])


if __name__ == "__main__":
    main()
