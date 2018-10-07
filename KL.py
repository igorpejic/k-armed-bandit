import numpy as np
import math

def normpdf(x, mean, sd):
    var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

def kl(p, q):
    sum = 0
    for i in range(len(p)):
        sum += p[i] * math.log(p[i] / q[i])
    return sum

mu = 0.2
sigma =  0.3

p = [normpdf(x, mu, sigma) for x in np.linspace(0, 1, 1000)]

ni = 0.4
tau = 0.1
q = [normpdf(x, ni, tau) for x in np.linspace(0, 1, 1000)]

print(kl(p, q))
