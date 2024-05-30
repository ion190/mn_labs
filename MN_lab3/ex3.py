import numpy as np
import matplotlib.pyplot as plt

# parameters
dt = 0.01
T = 10  # total time
steps = int(T / dt)

# arrays to store values of U(t), R(t)
U = np.zeros(steps)
R = np.zeros(steps)
t = np.linspace(0, T, steps)

U[0] = 1  # initial utilization
R[0] = 1  # initial resources

# functions for A(t) and D(t)
def A(t):
    return 0.5  # example constant arrival rate

def D(t):
    return 0.3  # example constant departure rate

# solving ODEs using Euler's method
for i in range(1, steps):
    U[i] = U[i-1] + dt * (A(t[i-1]) - D(t[i-1]))
    R[i] = R[i-1] + dt * (A(t[i-1]) - D(t[i-1]))

plt.plot(t, U, label='U(t)')
plt.plot(t, R, label='R(t)')
plt.xlabel('Time')
plt.ylabel('Value')
plt.legend()
plt.show()
