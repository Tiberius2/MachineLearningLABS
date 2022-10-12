# ## Exercise 1
# (Random variables, implementation)

# Give an example of a a real phenomenon modelled by the following discrete distributions and plot an illustrative pmf for that phenomenon using `matplotlib` and `scipy.stats` functions:

# 1. binomial;
# -------

# For example: Out of 30 people that eat fast food , only 10 of them are obese. So there's a probability of 0.33 that a person who eats fast food is obese
# We want to find out whats the probability that a person who eats fast food is obese by picking 5 people that eat fast food
# We have n=5 , p=0.33, k=range(n+1)


import matplotlib.pyplot as plt
from scipy.stats import binom 
n = 5
p = 0.33
k=range(n+1)

pmf_X = binom.pmf(k, n, p)

fig, ax = plt.subplots(1, 1)
ax.bar(k, pmf_X)
plt.ylabel("pmf")
plt.xlabel("k")
plt.title("Probability mass function")
plt.show()







