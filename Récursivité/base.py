unites = "0123456789ABCDEF"


def convert(n, base):
    if n < base:
        return (unites[n])
    else:
        return convert(n // base, base) + unites [n % base]



def convert2(base, n):
    pile = stack()
    while n >= base:
        pile.push(n)
        n = n // base
    res = unites[n]
    while not pile.isEmpty():
        n = pile.pop()
        res = res + unite[n % base]
    return res
