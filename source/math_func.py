import math

def calcQadratic(a, b, c):
    d = b*b - 4 * a * c

    if d < 0:
        return 'd = {} < 0'.format(d)
    elif d == 0:
        r = -b / (2 * a)
        return r
    else:
        d = math.sqrt(d)
        r1 = (-b + d) / (2 * a)
        r2 = (-b - d) / (2 * a)
        return '{} {}'.format(r1, r2)

a, b, c = [int(x) for x in input().split()]
r = calcQadratic(a, b, c)
print(r)