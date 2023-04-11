def goldbach():
    check = [True] * 10000

    for i in range(2, 101):
        if check[i] == True:
            for j in range(2*i, 10000, i):
                check[j] = False

    T = int(input())
    for _ in range(T):
        n = int(input())

        a = n //2
        b = a
        for _ in range(10000):
            if check[a] and check[b]:
                print(a, b)
                break
            a -= 1
            b += 1

goldbach()
