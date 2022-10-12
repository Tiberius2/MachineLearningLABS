# Exercise 5
# (Random variable, conceptual)

# The probability distribution of a discrete random variable $X$ is given by

# $P(X=-1)=1/5, P(X=0)=2/5, P(X=1)=2/5$.

# 1. Compute $E[X]$.
# 2. Give the probability distribution of $Y=X^2$ and compute $E[Y]$ using the distribution of $Y$.
# 3. Determine $E[X^2]$ using the change-of-variable formula. Check your answer against the answer in 2.
# 4. Determine $Var(X)$.




 # 1+4 :  E[x] And Var(X)

import matplotlib.pyplot as plt

"""
X = {'-1': 0.2, '0': 0.4, '1': 0.4}
k = [-1, 0, 1]
pmf_X=[0.2, 0.4, 0.4]


e_x = sum([k[i]*pmf_X[i] for i in range(len(k))])
var_x = sum([(ki-e_x)**2*pmf_X[i] for i, ki in enumerate(k)])
print(f"E[X] = {e_x}")
print(f"Var[X] = {var_x}")

"""


# 2. Y[i] * pmf, unde y = x ^2


X = {'-1': 0.2, '0': 0.4, '1': 0.4}
k = [-1, 0, 1]
pmf_X=[0.2, 0.4, 0.4]


e_x = sum([k[i]**2*pmf_X[i] for i in range(len(k))])

print(f"E[X] = {e_x}")


# 3. $E[g(X)] = \sum_ig(a_i)P(X=a_i)$ where X is a discrete variable taking the values $a_1, a_2,...$ and $g$ is a function $g:\mathbb{R} \to \mathbb{R}$ ("change of variable" formula)
