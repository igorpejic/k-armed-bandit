from numpy import *
from math import *
from itertools import *

"""
Depending on the policy pi, this creates the matrix of transition probabilities.

The policy is of a matrix of size [5, 5, 4] which for every place [a, b] specifies the four probabilities of moving in certain directions. It is in the order [p(north), p(south), p(east), p(west)].
"""
def transition(pi, terminal=False):
  P = zeros([5, 5, 5, 5])
  if (terminal == False):
    P[0, 1, 4, 1] = 1
    P[0, 3, 2, 3] = 1
  if (terminal == True):
    P[0, 1, 0, 1] = 1
    P[0, 3, 0, 3] = 1
  for a in range(5):
    for b in range(5):
      if [a, b] != [0, 1] and [a, b] != [0, 3]:
        for c in range(5):
          for d in range(5):
            if (a == c and (d == b-1 or (d == 0 and b == 0))):
              P[a, b, c, d] += pi[a, b, 3]
            if (a == c and (d == b+1 or (d == 4 and b == 4))):
              P[a, b, c, d] += pi[a, b, 2]
            if (b == d and (c == a+1 or (c == 4 and a == 4))):
              P[a, b, c, d] += pi[a, b, 1]
            if (b == d and (c == a-1 or (c == 0 and a == 0))):
              P[a, b, c, d] += pi[a, b, 0]
  return P


"""
The reward for doing i in (a,b)
"""
def dreward(a, b, i, terminal=False):
  if (a == 0 and b == 1 and terminal==False):
    return 10
  elif (a == 0 and b == 3 and terminal==False):
    return 5
  elif ((a,b) == (0,1) or (a,b) == (0,3)) and terminal==True:
    return 0
  elif (succ(a,b,i, terminal)==(0,1) and terminal==True):
    return 10
  elif (succ(a,b,i, terminal)==(0,3) and terminal==True):
    return 5
  elif ((a == 0 and i == 0) or (a == 4 and i == 1) or (b == 0 and i == 3) or (b == 4 and i == 2)):
    return -1
  else:
    return 0

"""
The rewards vector in position (a, b), specifying the rewards for the different possible actions.
"""
def drewards(a, b,terminal=False):
  return [dreward(a, b, 0, terminal), dreward(a, b, 1, terminal), dreward(a, b, 2, terminal), dreward(a, b, 3,terminal)]

"""
Depending on the policy, this creates the matrix of expected rewards from each position.
"""
def rewards(pi, terminal=False):
  r = zeros([5, 5])
  for a in range(5):
    for b in range(5):
      r[a, b] = dot(pi[a, b], drewards(a, b, terminal))
  return r

"""
Here we define the multiplication of a 5*5x5*5 matrix with a 5*5 vector
"""
def wmultiply(P, V):
  result = zeros([5, 5])
  for a in range(5):
    for b in range(5):
      for c in range(5):
        for d in range(5):
          result[a, b] += P[a, b, c, d] * V[c, d]
  return result

"""
The function bellmann update does the dynamic programming in order to approximate the state value function of a policy
"""
def bellmann_update(y, pi, V, n, terminal=False):
  return bellmann_update_pr_re(y*transition(pi, terminal), rewards(pi, terminal), V, n)

def bellmann_update_pr_re(P, r, V, n):
  if (n == 0):
    return V
  else:
    return bellmann_update_pr_re(P, r, r + wmultiply(P, V), n-1)



"""
This is the successor-function, specifying where we land if we move deterministically in a certain direction
"""

def succ(a, b, i, terminal=False):
  if (a == 0 and b == 1):
    if (terminal == False):
      return (4,1)
    else:
      return (0,1)
  elif (a == 0 and b == 3):
    if (terminal == False):
      return (2, 3)
    else:
      return (0, 3)
  elif (i == 0):
    if (a == 0):
      return (a, b)
    else:
      return (a-1, b)
  elif (i == 1):
    if (a == 4):
      return (a, b)
    else:
      return (a+1, b)
  elif (i == 2):
    if (b == 4):
      return (a, b)
    else:
      return (a, b+1)
  elif (i == 3):
    if (b == 0):
      return (a, b)
    else:
      return (a, b-1)

    
  
"""
This function defines the epsilon-greedy policy depending on a state value matrix/vector V
"""
def greedy(y, V, terminal=False):
  result = zeros([5, 5, 4])
  for a in range(5):
    for b in range(5):
      index = 0
      comp = V[a, b]
      for i in range(4):
        if (dreward(a, b, i) + y*V[succ(a, b, i, terminal)[0], succ(a, b, i, terminal)[1]] >= comp):
          index = i
          comp = dreward(a, b, i) + y*V[succ(a, b, i, terminal)[0], succ(a, b, i, terminal)[1]]
      result[a, b, index] = 1
  return result

def print_policy(pi):
  directions=["N","S","E","W"]
  result = chararray((5, 5))
  result[:] = '-'
  for a in range(5):
    for b in range(5):
      for i in range(4):
        if (pi[a, b, i] == 1):
          result[a, b] = directions[i]
  return result
V = zeros([5, 5])


"""
Exercise 1
"""

"""The equiprobable policy"""
pi = zeros([5, 5, 4])
for a in range(5):
  for b in range(5):
    for c in range(4):
      pi[a, b, c] = 1/4

print("Exercise 1")
print("")
print("This verifies the state value function of the equiprobable policy in the discounted case:")
print(bellmann_update(0.9, pi, zeros([5, 5]), 200, False))


"""
Exercise 2
"""

for i in range(25):
  V = bellmann_update(0.9, pi, V, 25)
  pi = greedy(0.9, V)


print("")
print("Exercise 2")
print("")
print("This is the state value function of the optimal policy in the discounted case, developed through greedification:")
print(V)
print("")
print("This is the optimal policy in the discounted case:")
print(print_policy(pi))



"""
Exercise 3
"""

"""The equiprobable policy"""
pi = zeros([5, 5, 4])
for a in range(5):
  for b in range(5):
    for c in range(4):
      pi[a, b, c] = 1/4

print("")
print("Exercise 3")
print("")
print("This is the state value function of the equiprobable policy in the undiscounted episodic case:")
print(bellmann_update(1, pi, zeros([5, 5]), 200, True))


V = zeros([5, 5])
for i in range(25):
  V = bellmann_update(1, pi, V, 25, True)
  pi = greedy(1, V, True)

print("")
print("This is the state value function of the optimal policy in the undiscounted case, developed through greedification:")
print(V)
print("")
print("This is one of the optimal policies in the undiscounted case. Note that the agent does not even bother to reach the final state, since he does not lose anything by moving around (as long as he does not reach the border):")
print(print_policy(pi))


