import sys


def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    result = []
    for element in iterable:
        if function is not None and function(element):
            result.append(element)
        elif function is None and element:
            result.append(element)

    return result


def main():
    """Main ft_filter.py"""
    ages = [5, 12, 17, 18, 24, 32]

    def myFunc(x):
        if x < 18:
            return False
        else:
            return True

    if len(sys.argv) == 2 and sys.argv[1] == "--doc":
        print("__DOC__:")
        print(filter.__doc__)
        print("\n----\n")
        print(ft_filter.__doc__)
    else:

        print("REAL FILTER FUNCTION: ")

        adults = filter(myFunc, ages)
        for x in adults:
            print(x)

        print("\n----\n")

        print("MY FILTER FUNCTION: ")

        adults = ft_filter(myFunc, ages)
        for x in adults:
            print(x)


if __name__ == "__main__":
    main()
