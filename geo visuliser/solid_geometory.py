import matplotlib.pyplot as plt
import numpy as np

def draw_sphere():
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Create angles
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)

    # Sphere formula
    x = 10 * np.outer(np.cos(u), np.sin(v))
    y = 10 * np.outer(np.sin(u), np.sin(v))
    z = 10 * np.outer(np.ones(len(u)), np.cos(v))

    # Draw sphere
    ax.plot_surface(x, y, z)

    plt.show()
