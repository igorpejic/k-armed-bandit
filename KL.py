import numpy as np
import math

def normpdf(x, mean, sd, steps):
    var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    # num = math.exp(-(float(x)-float(mean))**2/(2*var))
    res =  (1 / math.sqrt(2 * pi * sd * sd)) * math.exp(-((x - mean) * (x - mean)) / (2 * sd * sd))
    return res / steps

def kl(p, q):
    sum = 0
    for i in range(len(p)):
        sum += p[i] * math.log(p[i] / q[i])
    return sum

def kl_extracted_forumla(mu, sigma, ni, tau, steps):
    return math.log(tau/sigma) + (sigma*sigma + (mu - ni)**2) / (2 * tau * tau) - 0.5

def kl_extracted_forumla_1(mu, sigma, ni, tau, steps):
    return 0.5 * (math.log((tau*tau)/(sigma*sigma)) -1 + (sigma*sigma + (mu - ni)**2) / (tau * tau))

mu = 0.1
sigma =  0.3

steps = 100
p = [normpdf(x, mu, sigma, steps) for x in np.linspace(-3 * sigma + mu, 3 * sigma + mu, steps)]
print(p)

ni = 0.1
tau = 0.4
q = [normpdf(x, ni, tau, steps) for x in np.linspace(-3 * tau + ni, 3 * tau + ni, steps)]

print(kl(p, q))
print(kl_extracted_forumla_1(mu, sigma, ni, tau, steps))
print(kl_extracted_forumla(mu, sigma, ni, tau, steps))

