import math
p = 0.171**1.163 * math.log(5, 2) + 2.526 * math.log(7, 3) 
n = math.tan(6) * math.e**abs(math.sqrt(2/3) - (math.sqrt(6) + 1) / 2*math.sqrt(3))
if p <= n:
    u = math.log10(abs(p) + abs(n))
if p > n:
    u = math.log10(abs(p - n))
print(u)
