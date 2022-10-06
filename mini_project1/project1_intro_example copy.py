# this code solves the following linear optimization problem using SciPY

# minimize -z = -x - y
# subject to: -x + y <= 1
# x + 6y <= 15
# 4x - y <= 10
# x >= 0
# y >= 0

# import numpy
import numpy as np

# import optimization and root-finding library
from scipy.optimize import linprog

# define input values

# objective function
obj = [-1, -1]  # coefficents for -z = -x - y

# lhs inequalities
lhs_inequality = [[-1, 1],  # first inequality
            [1, 6],  # second inequality
            [4, -1]]  # third inequality

# rhs inequalities
rhs_inequality = [1,  # first inequality
            15,  # second inequality
            10]  # third inequality


# define bounds for each variable
# note this is redundant because linprog takes bounds to be (0, inf) by default
bound = [(0, np.inf),  # bound for x
         (0, np.inf)]  # bound for y

# do the optimization
# c:= coefficents from objective function
# A_ub = coefficents for lhs inequalities
# b_ub := coefficents for rhs inequalities
# A_eq := coefficents for lhs equalities
# b_eq := coefficents for rhs equalities
optimization = linprog(c=obj,
                       A_ub=lhs_inequality,
                       b_ub=rhs_inequality,
                       bounds=bound,
                       method="highs")


print(optimization)



