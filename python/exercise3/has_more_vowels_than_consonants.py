def is_vowel(char):
    return char.lower() in "aeiou"


def count_vowels(s):
    if not s:
        return 0
    return (1 if is_vowel(s[0]) else 0) + count_vowels(s[1:])


def count_consonants(s):
    if not s:
        return 0
    return (1 if s[0].isalpha() and not is_vowel(s[0]) else 0) + count_consonants(s[1:])


def has_more_vowels_than_consonants(s):
    num_vowels = count_vowels(s)
    num_consonants = count_consonants(s)
    return num_vowels > num_consonants


def main():
    user_input = input("Enter a string: ")
    print(has_more_vowels_than_consonants(user_input))


if __name__ == "__main__":
    main()
