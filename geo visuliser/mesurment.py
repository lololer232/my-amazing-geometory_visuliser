import math

# Distance between two points
def distance(p1, p2):
    return math.sqrt(
        (p2[0] - p1[0]) * (p2[0] - p1[0]) +
        (p2[1] - p1[1]) * (p2[1] - p1[1])
    )


# Area of triangle
def triangle_area(p1, p2, p3):
    return abs(
        p1[0] * (p2[1] - p3[1]) +
        p2[0] * (p3[1] - p1[1]) +
        p3[0] * (p1[1] - p2[1])
    ) / 2


# Angle between two lines (using slopes)
def angle_between(m1, m2):
    return math.degrees(
        math.atan((m2 - m1) / (1 + m1 * m2)))