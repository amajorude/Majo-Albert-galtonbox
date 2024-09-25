# IMPORTS
import random 
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import math

N = 10000
n = 15

#  EXPERIMENT RESULTS
board = [0 for x in range(n + 1)] 
for i in range(N):
    x = 0
    for j in range(n):
       x += random.randint(0, 1)
    board[x] += 1

# EXPERIMENT MEAN
exp_mean = 0
for x in range(n+1):
    exp_mean += x*board[x]
exp_mean = exp_mean/N

# EXPERIMENT STANDARD DEVIATION
exp_std_dev = 0
for x in range(n +1):
    exp_std_dev += board[x] * (x - exp_mean)**2
exp_std_dev = math.sqrt(exp_std_dev/N)

print('experiment mean: ', exp_mean)
print('experiment standard deviation: ', exp_std_dev)

# Scale the results
scaled_board =[board[x]/N for x in range(n + 1)]

# NORMAL DISTRIBUTION

mean = n/2
std_dev = math.sqrt(n)/2

print('gaussian mean: ', mean)
print('gaussian standard deviation: ', std_dev)
 
x = np.linspace(0, n, 100)
normal_dist = norm.pdf(x, mean, std_dev)

# MEAN QUADRATIC ERROR
mean_quadratic_error = 0
for i in range(n):
    mean_quadratic_error = (scaled_board[i] - normal_dist[i])**2
print('mean quadratic error: ', mean_quadratic_error)


# PLOT THE RESULTS

# Plot the experiment results
plt.bar(range(len(scaled_board)), scaled_board)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Bar Plot of Array') 

# Plot the normal distribution
plt.plot(x, normal_dist, color='red', label='Normal Distribution')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Bar Plot with Normal Distribution')

plt.legend()
plt.show()