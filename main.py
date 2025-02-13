def printCountWords(text):
    word_count = len(text.split())

    print(f"{word_count} words found in the document\n")


def printSortedAlphabet(sorted):
    for dict in sorted:
        value = list(dict.values())[0]
        key = list(dict.keys())[0]

        print(f"The '{key}' character was found {value} times")


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
        
    return sorted(alphabet, key=lambda x: list(x.values())[0], reverse=True)


def main():
    text = ""
    with open("books/frankenstein.txt") as f:
        for line in f:
            text += line

    printCountWords(text)
    printSortedAlphabet(countCharacters(text))

main()