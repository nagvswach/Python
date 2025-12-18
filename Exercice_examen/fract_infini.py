#récursive 


def frac_rec(lst, i = None):
    if i == None:
        i = 0
    if i == len(lst) - 1:
        return lst[i]
    return lst[i] + 1 / frac_rec(lst, i + 1)

#itérative

def frac_it(lst):
    res = lst[-1]
    for elem in reversed(lst[:-1]):
        res = elem + 1 / res
    return res


liste = [5, 1, 4, 1, 10]
print(frac_rec(liste))
print(frac_it(liste))


    
