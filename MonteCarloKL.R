f = function(x, mu, sigma) dnorm(x,mu, sigma)
g = function(x, nu, tau) dnorm(x,nu, tau)
KL = function(mu,sigma,nu,tau) log(tau/sigma) + (sigma^2 + (mu-nu)^2)/(2*tau^2) - 1/2

num_sims=1000
mu=1
sigma=2
nu=3
tau=4

results=numeric(num_sims)
x = rnorm(1,mu,sigma)
results[1] = log(f(x, mu, sigma)/g(x, nu, tau))

for (i in 2:num_sims){
  x = rnorm(1,mu,sigma)
  results[i] = results[i-1] + (log(f(x, mu, sigma)/g(x, nu, tau)) - results[i-1])/i
}

results[num_sims]
KL(mu,sigma,nu,tau)
plot(results/KL(mu,sigma,nu,tau),type="l")

iterations=1:num_sims
approximated_and_exact_KL_value=cbind(results,rep(KL(mu,sigma,nu,tau),n_sims))
matplot(iterations,approximated_and_exact_KL_value,type="l")
