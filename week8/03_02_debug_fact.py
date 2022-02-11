## DEBUG THIS CODE


def h_fact(n):
    if n == 1:
        return 0
    else:
        return n - 2 * h_fact(n - 1)


h_fact(10)
