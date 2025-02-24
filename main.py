import sys
from stats import printCountWords

def printHeader(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

def printFooter():
    print("============= END ===============")

def printSortedAlphabet(sorted):
    for dict in sorted:
        value = list(dict.values())[0]
        key = list(dict.keys())[0]

        print(f"{key}: {value}")


def countCharacters(text):
    unique_chars = {}
    for char in text:
        char = char.lower()

        if char not in unique_chars:
            unique_chars[char] = 1
        else:
            unique_chars[char] += 1

    alphabet = []
    for char in unique_chars:
        if char.isalpha():
            alphabet.append({char: unique_chars[char]})
    
    print("--------- Character Count -------")
    return sorted(alphabet, key=lambda x: list(x.values())[0], reverse=True)


def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        return 1

    text = ""
    with open(sys.argv[1]) as f:
        for line in f:
            text += line

    printHeader(sys.argv[1])
    printCountWords(text)
    printSortedAlphabet(countCharacters(text))
    printFooter()

main()