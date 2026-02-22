import matplotlib.pyplot as plt

# Plot a point
def plot_point(x, y):
    plt.scatter(x, y)
    plt.show()


# Draw a line
def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2])
    plt.show()


# Draw a triangle
def draw_triangle(x1, y1, x2, y2, x3, y3):
    plt.plot([x1, x2], [y1, y2])
    plt.plot([x2, x3], [y2, y3])
    plt.plot([x3, x1], [y3, y1])
    plt.show()