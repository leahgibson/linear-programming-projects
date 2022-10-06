# import numpy
import numpy as np

# import optimization and root-finding library
from scipy.optimize import linprog

# define input values

# objective function
obj = [2.5, 5, 7, 1]  # coefficents

# lhs inequalities
lhs_inequality = [[-3, 0, 0, -1],
                  [0, -1, -1, -3],
                  [1, 1, 1, 1],
                  [0, -1, -1, 0]]

# rhs inequality
rhs_inequality = [-1,
                  -1.4,
                  1.5,
                  -0.3]

# lhs equality
lhs_equality = [[1, 0, 0.5, 0]]

# rhs equality
rhs_equality = [0.7]

# bounds
bnds = [(0, np.inf),
        (0, np.inf),
        (0,1),
        (0,np.inf)]

# do the optimization
optimization = linprog(c=obj,
                       A_ub=lhs_inequality,
                       b_ub=rhs_inequality,
                       A_eq=lhs_equality,
                       b_eq=rhs_equality,
                       bounds=bnds,
                       method="highs")

print(optimization)
