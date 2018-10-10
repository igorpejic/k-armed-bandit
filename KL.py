import numpy as np
import math

def normpdf(x, mean, sd, steps):
    pi = 3.1415926
    res =  (1 / math.sqrt(2 * pi * sd * sd)) * math.exp(-((x - mean) * (x - mean)) / (2 * sd * sd))
    return res
    return num /denom

def kl(p, q):
    sum = 0
    for i in range(len(p)):
        if p[i] == 0:
            continue
        if q[i] == 0:
            continue
        sum += (p[i] * math.log(p[i] / q[i]))
    return sum

def kl_extracted_forumla(mu, sigma, ni, tau, steps):
    return math.log(tau/sigma) + (sigma*sigma + (mu - ni)**2) / (2 * tau * tau) - 0.5

def kl_extracted_forumla_1(mu, sigma, ni, tau, steps):
    return 0.5 * (math.log((tau*tau)/(sigma*sigma)) -1 + (sigma*sigma + (mu - ni)**2) / (tau * tau))

mu = 0.3
sigma =  0.3

steps = 400
p = np.array([normpdf(x, mu, sigma, steps) for x in np.linspace(-100, 100, steps)])
p = p / sum(p)

ni = 0.1
tau = 0.2
q = np.array([normpdf(x, ni, tau, steps) for x in np.linspace(-100, 100, steps)])
q = q / sum(q)

print(kl(p, q))
print(kl_extracted_forumla_1(mu, sigma, ni, tau, steps))
print(kl_extracted_forumla(mu, sigma, ni, tau, steps))
