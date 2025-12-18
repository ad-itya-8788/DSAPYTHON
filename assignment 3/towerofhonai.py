def toh(n, first, helper, last):
    if n == 1:
        print("Move disk 1 from", first, "to", last)
        return

    toh(n - 1, first, last, helper)
    print("Move disk", n, "from", first, "to", last)
    toh(n - 1, helper, first, last)


n = 4
toh(n, 'A', 'B', 'C')
