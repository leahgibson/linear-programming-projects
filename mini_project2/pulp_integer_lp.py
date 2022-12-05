from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# create the model
model = LpProblem(name="integer linear program", sense=LpMaximize)

# variables
x = LpVariable(name="x", lowBound = 0, cat="Integer")
y = LpVariable(name="y", lowBound = 0, cat="Integer")

# constraints
model += (x - y <= 0, "first constraint")
model += ((5/2 )* x - (1/3) * y <= 7, "second constraint")
model += (-1 * x + 2 * y <= 8, "third constraint")

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


