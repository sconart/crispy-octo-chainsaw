def print_asterisks(n, current=1):
    if current > n:
        return
    print("*" * current)
    print_asterisks(n, current + 1)
    if current != n:
        print("*" * current)


def main():
    max_stars = int(input("Enter the number of asterisks of the maximum line: "))
    print_asterisks(max_stars)


if __name__ == "__main__":
    main()
