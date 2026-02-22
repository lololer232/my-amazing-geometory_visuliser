from plane_geometory import plot_point, draw_line, draw_triangle
from mesurment import distance, triangle_area, angle_between

while True:
    print("\nGEOMETRY VISUALISER")
    print("1. Plot Point")
    print("2. Draw Line")
    print("3. Draw Triangle")
    print("4. Distance Between Two Points")
    print("5. Area of Triangle")
    print("6. Angle Between Two Lines")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = float(input("Enter x: "))
        y = float(input("Enter y: "))
        plot_point(x, y)

    elif choice == 2:
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        draw_line(x1, y1, x2, y2)

    elif choice == 3:
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        x3 = float(input("x3: "))
        y3 = float(input("y3: "))
        draw_triangle(x1, y1, x2, y2, x3, y3)

    elif choice == 4:
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        print("Distance =", distance((x1, y1), (x2, y2)))

    elif choice == 5:
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        x3 = float(input("x3: "))
        y3 = float(input("y3: "))
        print("Area =", triangle_area((x1, y1), (x2, y2), (x3, y3)))

    elif choice == 6:
        m1 = float(input("Slope of line 1: "))
        m2 = float(input("Slope of line 2: "))
        print("Angle =", angle_between(m1, m2), "degrees")

    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")