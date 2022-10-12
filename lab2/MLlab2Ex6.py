# Exercise 6
# (binomial distribution, applied)

# A sailor is trying to walk on a slippery deck, but because of the movements of the ship, he can make exactly one step every second, 
# either forward (with probability $p=0.5$) or backward (with probability $1-p=0.5$). 
# Using the `scipy.stats.binom` package, determine the probability that the sailor is in position +8 after 16 seconds.


# If the sailor is in position +8 after 16s, that means he must have made 12 steps forward and 4 backwards 
# Example: What is the probability of getting +8(k) steps forward when walking n=16 times consecutively knowing that the probability of getting (k) is 0.5.

import matplotlib.pyplot as plt
from scipy.stats import binom


n = 16
p = 0.5
k=range(n+1)

pmf_X = binom.pmf(k, n, p)

fig, ax = plt.subplots(1, 1)
ax.bar(k, pmf_X)
plt.ylabel("pmf")
plt.xlabel("k")
plt.title("Probability mass function")
plt.show()


