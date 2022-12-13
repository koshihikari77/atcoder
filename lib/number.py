def isprime(N):
    if N < 2:
        return False
    i = 2
    while i * i <= N:
        if N % i == 0:
            return False
        i += 1
    return True

# 1 以上 N 以下の整数が素数かどうかを返す
def Eratosthenes(N):
    isprime = [True] * (N+1)
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        if not isprime[p]:
            continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    return isprime

# 素因数分解
# 460 = 2^2 x 5 x 23 の場合
# 返り値は [(2, 2), (5, 1), (23, 1)]
def prime_factorize(N):
    res = []

    for p in range(2, N):
        if p * p > N:
            break

        if N % p != 0:
            continue

        e = 0
        while N % p == 0:
            e += 1
            N //= p

        res.append((p, e))

    if N != 1:
        res.append((N, 1))

    return res


def calc_divisors(N):
    res = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i != 0:
            continue
        res.append(i)
        if N // i != i:
            res.append(N // i)
    res.sort()
    return res

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    g = gcd(a,b)
    return a*b // g