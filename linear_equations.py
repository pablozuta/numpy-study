import numpy as np 

# Define the coefficients of the linear equations  
coefficients = np.array([[22, 11],[33, 66]])
  
# Define the constants of the linear equations  
constants =   np.array([2, 1])
  
# Solve the linear equations  
solution =   np.linalg.solve(coefficients, constants)
  
# Print the solution  
print("Solution:")  
print(solution)  