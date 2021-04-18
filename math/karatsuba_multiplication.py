def karatsuba_multiplication(x, y):
    """Implementation of Karatsuba Multiplication.
    Returns the product of two numbers.
    """
    n = max(len(str(x)), len(str(y)))

    if n == 1:
        return x * y
    else:
        m = round(n / 2)

        a = x // (10 ** m)
        b = x % (10 ** m)
        c = y // (10 ** m)
        d = y % (10 ** m)

        ac = karatsuba_multiplication(a, c)
        bd = karatsuba_multiplication(b, d)
        ad_plus_bc = karatsuba_multiplication((a + b), (c + d)) - ac - bd

        return ((10 ** (m * 2)) * ac) + ((10 ** m) * ad_plus_bc) + bd