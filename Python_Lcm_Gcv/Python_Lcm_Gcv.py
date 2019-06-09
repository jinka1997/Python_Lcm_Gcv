## 素因数分解
def prime_factorize(num):
    
    ## 辞書初期化
    prime_dic = {}
    
    ## 変数の初期値は素因数分解したい値
    tmp = num

    ## 2(最小の素数)で除算するところから
    n = 2

    ## 除算の結果が1になるまで繰り返し
    ## 判定1回目：12は1より大きいのでループに入る
    ## 判定2回目：3は1より大きいのでループに入る
    ## 判定3回目：1は1より大きいのは偽なので、ループに入らない
    while tmp > 1:

        ## 【n = 2】 自然数が変わったら、指数はゼロで初期化
        i = 0

        ## nで割りきれる(nで割った余りがゼロ)の間、繰り返し
        ## 【n = 2】
        ##   判定1回目：12は2で割り切れるのでループに入る
        ##   判定2回目：6は2で割り切れるのでループに入る
        ##   判定3回目：3は2で割り切れないので、ループに入らない
        ## 【n = 3】
        ##   判定1回目：3は3で割り切れるのでループに入る
        ##   判定2回目：1は3で割り切れるので、ループに入らない
        while tmp % n == 0:

            ## 指数+1
            ## 【n = 2】
            ##   1周目：12は2で割りきれるので指数を0→1に
            ##   2周目：6は2で割りきれるので指数を1→2に
            ## 【n = 3】
            ##   1周目：3は3で割りきれるので指数を0→1に
            i += 1

            ## 除算して、商を変数に入れる
            ## 【n = 2】
            ##   1周目：12÷2の結果、6をtmpに入れる
            ##   2周目：6÷2の結果、3をtmpに入れる
            ## 【n = 3】
            ##   1周目：3÷3の結果、1をtmpに入れる
            tmp = tmp / n

        ## 1回でも除算ができたか？
        ##  【n = 2】指数は2
        ##  【n = 3】指数は1
        if i > 0 :

            ## 素数と指数を辞書にセット
            ##  【n = 2】素数2に対しての、指数2をセット
            ##  【n = 3】素数3に対しての、指数1をセット
            ## {2:2,3:1}
            prime_dic[n] = i

        ## 次の自然数へ
        ##  【n = 2→3】
        ##  【n = 3→4】
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
