from collections import defaultdict
# rod price based on its length
p = {1: 1,
     2: 5,
     3: 8,
     4: 9,
     5: 10,
     6: 17,
     7: 17,
     8: 20,
     9: 24,
     10: 30}


def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i]+cut_rod(p, n-i))
    return q


def cut_rod_memo(p, n, price={}):
    try:
        return price[n]
    except KeyError:
        if n == 0:
            price[0] = 0
            return 0
        q = float('-inf')
        for i in range(1, n+1):
            q = max(q, p[i]+cut_rod_memo(p, n-i, price))
            price[n] = q
        return q


def cut_rod_bottom_up(p, n):
    price = defaultdict(int)
    if n == 0:
        return 0
    q = float('-inf')
    for j in range(1, n+1):
        for i in range(1, j+1):
            q = max(q, p[i]+price[j-i])
        price[i] = q
    return price[n]


if __name__ == '__main__':
    revenue = cut_rod_memo(p, 9)
    print(revenue)
