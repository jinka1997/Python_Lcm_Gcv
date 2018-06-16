## 素因数分解
def prime_factorize(num):
    prime_dic = {}
    tmp = num
    n = 2
    while tmp > 1:
        i = 0
        while tmp % n == 0:
            i += 1
            tmp = tmp / n
        if i > 0 :
            prime_dic[n] = i
        n += 1
    return prime_dic

def lineup_power_index(pfs):
    dic = {}
    lst = []
    for pf in pfs:
        lst.extend(list(pf.keys()))
    primes = list(set(lst))

    for p in primes:
        dic[p] = [0] * len(pfs)

    idx = 0
    for pf in pfs:
        for key,value in pf.items():
            dic[key][idx] = value
        idx += 1

    return dic

def calc(dic):
    gcd = lcm = 1

    for key, value in dic.items():
        max_index = max(value)
        min_index = min(value)

        lcm = lcm * (key ** max_index)
        gcd = gcd * (key ** min_index)

    return lcm, gcd

nums = [12,16,18]

pfs = [prime_factorize(n) for n in nums]
dic = lineup_power_index(pfs)
lcm, gcd = calc(dic)

print('最小公倍数 = {}, 最大公約数 = {}'.format(lcm, gcd))
