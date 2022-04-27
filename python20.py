def putNumber(n):
    for i in range(n + 1):
        if i % 7 == 0:
            yield i


for i in putNumber(500):
    print(i)
