def solve(a):
    even = 0
    odd = 0
    for num in a:
        try:
            testNum = int(num)
            print(num)
        except:
            continue
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    total = even - odd
    print(total)

solve([13, 6, 8, 15, 4, 8, 13])
