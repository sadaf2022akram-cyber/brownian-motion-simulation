import numpy as np
import matplotlib.pyplot as plt

steps = 5000
dt = 0.1
simulations = 5
diffusion_coefficient = 0.5
scale = np.sqrt(2 * diffusion_coefficient * dt)

plt.figure(figsize=(8, 8))

for s in range(simulations):
    x_shocks = np.random.normal(0, 1, steps)
    y_shocks = np.random.normal(0, 1, steps)
    
    x_path = np.cumsum(scale * x_shocks)
    y_path = np.cumsum(scale * y_shocks)
    
    plt.plot(x_path, y_path, alpha=0.8, label=f'Particle {s+1}')
    plt.plot(x_path[0], y_path[0], 'go') 
    plt.plot(x_path[-1], y_path[-1], 'ro') 

plt.title(f"2D Random Walk: Brownian Motion of {simulations} Particles")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.legend()
plt.show()