# solve linear program using PuLP

# minimize -z = -x - y
# subject to: -x + y <= 1
# x + 6y <= 15
# 4x - y <= 10
# x >= 0
# y >= 0

from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# create the model
model = LpProblem(name="m510example", sense=LpMaximize)

# variables
x = LpVariable(name="x", lowBound = 0)
y = LpVariable(name="y", lowBound = 0)

# constraints
model += (-1 * x + y <= 1, "first constraint")
model += (x + 6 * y <= 15, "second constraint")
model += (4 * x - y <= 10, "third constraint")

# objective function
objective_function = x + y

# add objective function to model
model += objective_function

print(model)

# solve the problem
status = model.solve()

# see the solution
print(f"status: {model.status}, {LpStatus[model.status]}")  # tells you if solver was sucessful

print(f"objective: {model.objective.value()}") # output using optimal variables

for var in model.variables(): print(f"{var.name}: {var.value()}")  # print variables

for name, constraint in model.constraints.items(): print(f"{name}: {constraint.value()}") # value of constraints
