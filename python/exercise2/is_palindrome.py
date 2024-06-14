def is_palindrome(s):
    if len(s) <= 1:
        return True

    s = "".join(char for char in s if char.isalnum()).lower()

    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def main():
    s = input("Provide string entries to be checked: ").strip()
    print(is_palindrome(s))


if __name__ == "__main__":
    main()
