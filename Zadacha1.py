import math

def triangle_area(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def right_triangle(x1, y1, x2, y2, x3, y3):
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    if c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == b**2 + c**2:
        return True
    else:
        return False

x1 = float(input("Введите координат x1: "))
y1 = float(input("Введите координат y1: "))
x2 = float(input("Введите координат x2: "))
y2 = float(input("Введите координат y2: "))
x3 = float(input("Введите координат x3: "))
y3 = float(input("Введите координат y3: "))

area = triangle_area(x1, y1, x2, y2, x3, y3)
right = right_triangle(x1, y1, x2, y2, x3, y3)

with open("area.txt", "w") as f:
    f.write(str(area))

with open("truefalse.txt", "w") as f:
    f.write(str(right))