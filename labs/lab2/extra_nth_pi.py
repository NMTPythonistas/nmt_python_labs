def expmod(base, power, mod_by):
    """This function calculates (base ^ power) % mod_by."""

    x = 1
    while(power > 0):
        if (power & 1 == 1):
            x = (x * base) % mod_by
        base = (base * base) % mod_by
        power >>= 1
    return x % mod_by


def decimal_to_hex(frac, ndigits):
    """Convert the float frac into a hexadecimal number of
    length ndigits."""

    frac = abs(frac)
    s = []
    for i in range(ndigits):
        frac = 16 * (frac - int(frac))
        s.append("0123456789ABCDEF"[int(frac)])
    return ''.join(s)


def digits(n):
    nth_digit = 0.141592653589
    return decimal_to_hex(nth_digit, 10)
