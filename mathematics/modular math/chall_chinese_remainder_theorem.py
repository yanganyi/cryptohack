from functools import reduce
from math import gcd

# 定义同余方程组和模数
eqns = [(2, 5), (3, 11), (5, 17)]
moduli = [5, 11, 17]

# 计算总模数
N = reduce(lambda x, y: x*y, moduli)

# 计算每个模数的逆元
m = [N // m for m in moduli]
mi = [pow(m[i], -1, moduli[i]) for i in range(len(moduli))]

# 计算唯一解
x = sum(a * mi[i] * m[i] for i, (a, _) in enumerate(eqns))

# 输出结果
print("Solution: x = {} (mod {})".format(x % N, N))