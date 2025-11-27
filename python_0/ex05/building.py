import sys

def countCharacter(str: str):
	print("The text contains", len(str), "characters:");

def countUpperLetters(str: str):
	count = sum([1 if c.upper() else 0 for c in str])
	print(count, "upper letters")

def countLowerLetters(str: str):
	count = 0
	count = sum([1 if c.lower() else 0 for c in str])
	print(count, "lower letters")

def countPonctuationMarks(str: str):
	punct = ".,;?!"
	count = sum([1 if c in punct else 0 for c in str])
	print(count, "punctuation marks")

def countSpace(str: str):
	count = sum([1 if c == " " else 0 for c in str])
	print(count, "spaces")

def countDigits(str: str):
	count = sum([1 if c.isdigit() else 0 for c in str])
	print(count, "digits")

def main():
	if len(sys.argv) < 2 :
		return
	elif len(sys.argv) > 2 :
		print("AssertionError: more than one argument is provided")
	else:
		countCharacter(sys.argv[1])
		countUpperLetters(sys.argv[1])
		countLowerLetters(sys.argv[1])
		countPonctuationMarks(sys.argv[1])
		countSpace(sys.argv[1])
		countDigits(sys.argv[1])

if __name__ == "__main__":
	main()