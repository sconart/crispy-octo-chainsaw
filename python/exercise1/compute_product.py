def compute_product(m, n):
    if n < 0:
        return -compute_product(m, -n)

    if n == 0:
        return 0
    return m + compute_product(m, n - 1)


def main():
    m = 5
    n = 3
    result = compute_product(m, n)
    print(result)


if __name__ == "__main__":
    main()
