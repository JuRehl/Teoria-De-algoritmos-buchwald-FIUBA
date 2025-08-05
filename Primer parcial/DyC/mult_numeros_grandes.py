def multiplicar(a, b):
    if a < 10 or b < 10:
        return a * b

    n = max(len(str(a)), len(str(b)))
    m = n // 2

    a1 = a // (10**m)
    a2 = a % (10**m)
    b1 = b // (10**m)
    b2 = b % (10**m)

    A = multiplicar(a1, b1)
    B = multiplicar(a2, b2)
    C = multiplicar(a1 + a2, b1 + b2) - A - B

    return A * (10**(2*m)) + C * (10**m) + B