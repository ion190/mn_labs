import numpy as np
import matplotlib.pyplot as plt

Vmax = 120  # max velocity (km/h)
rho_max = 100  # max traffic density (vehicles/km)
L = 10  # length of road segment (km)
dx = 0.1  # distance step (km)
dt = 0.01  # time step (s)
T = 100  # simulation time (s)

# discretize space and time
x = np.arange(0, L, dx)
t = np.arange(0, T, dt)
nx = len(x)
nt = len(t)

# initial conditions
rho = np.zeros(nx)
rho[int(0.3 * nx):int(0.5 * nx)] = 50  # initial density

def velocity(rho):
    return Vmax * (1 - rho / rho_max)

def flux(rho):
    return rho * velocity(rho)

# time-stepping loop
for n in range(nt):
    q = flux(rho)
    
    # update traffic density with conservation law
    rho[1:-1] = rho[1:-1] - dt/dx * (q[1:-1] - q[:-2])
    
    # boundary conditions
    rho[0] = rho[1]
    rho[-1] = rho[-2]
    
    if n % 100 == 0:
        plt.plot(x, rho, label=f't={n*dt:.1f}s')

plt.xlabel('Position (km)')
plt.ylabel('Traffic Density (vehicles/km)')
plt.legend()
plt.title('Traffic Density Over Time')
plt.show()