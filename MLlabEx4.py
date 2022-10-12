# Exercise 4
# (Random variable, implementation)

# Let $S$ be the outcome of a random variable describing the sum of two dice thrown independently.

# 1. Print the probability distribution of $S$ graphically.
# 1. Determine $E[S]$ and $Var(S)$.


#Let  Ω:={1,2,3,4,5,6}2 .

# Let  A:=P(Ω) .

# Let  P(A)=|A|36  for  A∈A .

# Then  (Ω,A,P)  is a probability space.

# E[S] = 
# Variance of S is : var(s) = E[(X-E[X])^2]

# Nu am reusit sa fac exercitiul

import matplotlib.pyplot as plt
from scipy.stats import binom
from tools import probability_weighted, WeightedOutcome
from dataclasses import dataclass


@dataclass(frozen=True)
class Outcome(WeightedOutcome):
    die_face : int


omega = set([Outcome(sum = 2, weight = 1),
             Outcome(sum = 3, weight = 1),
             Outcome(sum = 4, weight = 1),
             Outcome(sum = 5, weight = 1),
             Outcome(sum = 6, weight = 1),
             Outcome(sum = 7, weight = 1),
             Outcome(sum = 8, weight = 1),
             Outcome(sum = 9, weight = 1),
             Outcome(sum = 10, weight = 1),
             Outcome(sum = 11, weight = 1),
             Outcome(sum = 12, weight = 1)
             ])

X = {2 : 1, 3 : 2, 4 : 3, 5 : 4, 6 : 5, 7 : 6, 8 : 7, 9 : 8, 10 : 9, 11 : 10, 12 : 11}

def pmf(X, a, omega):
    A = set(o for o in omega if X[o.die_face] is a)
    return probability_weighted(A, omega)
    
import matplotlib.pyplot as plt


k = sorted(set(X.values()))
pmf_X = [pmf(X, x, omega) for x in k]

fig, ax = plt.subplots(1, 1)
ax.bar(k, pmf_X)
plt.ylabel("pmf")
plt.xlabel("k")
plt.title("Probability mass function")
plt.show()



