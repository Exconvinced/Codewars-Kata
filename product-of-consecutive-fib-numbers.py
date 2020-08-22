def productFib(prod):
    m, n = 0, 1
    while True:
        if m * n < prod: k = n; n += m; m = k
        elif m * n > prod: return [m, n, False]
        else: return [m, n, True]


print(productFib(5895))