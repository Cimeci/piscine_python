import sys


def convert_str_to_morse(text: str) -> str:
    """convert_str_to_morse(text: str) -> str

Function convert text to morse code"""

    supported_characters = "abcdefghijklmnopqrstuvwxyzABC" \
        "DEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    for c in text:
        if c not in supported_characters:
            return "AssertionError: the arguments are bad"

    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }

    morse_text = ""

    for c in text.upper():
        if c in NESTED_MORSE:
            morse_text += NESTED_MORSE[c]
        else:
            morse_text += "? "
    return morse_text


def main():
    """Main sos.py"""
    if len(sys.argv) != 2:
        print("AssertionError: the number of arguments are bad")

    elif sys.argv[1] == "--doc":
        print("__DOC__:")
        print(convert_str_to_morse.__doc__)

    else:
        ret = convert_str_to_morse(sys.argv[1])
        print(ret)


if __name__ == "__main__":
    main()
