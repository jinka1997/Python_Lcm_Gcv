## 素因数分解
def prime_factorize(num):
    prime_dic = {}
    
    ## 変数の初期値は素因数分解したい値
    tmp = num

    ## 2(最小の素数)で除算するところから
    n = 2

    ## 除算の結果が1になるまで繰り返し
    while tmp > 1:

        ## 自然数が変わったら、指数はゼロで初期化
        i = 0

        ## nで割りきれる(nで割った余りがゼロ)の間、繰り返し
        while tmp % n == 0:

            ## 指数+1
            i += 1

            ## 除算して、商を変数に入れる
            tmp = tmp / n

        ## 1回でも除算ができたか？
        if i > 0 :

            ## 素数と指数を辞書にセット
            prime_dic[n] = i

        ## 次の自然数へ
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

nums = [12,15]

pfs = [prime_factorize(n) for n in nums]
dic = lineup_power_index(pfs)
lcm, gcd = calc(dic)

print('最小公倍数 = {}, 最大公約数 = {}'.format(lcm, gcd))
