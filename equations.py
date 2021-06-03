from matplotlib import pyplot as plt
import numpy as np
import math

plt.style.use("seaborn-pastel")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Custom plot')

print(u"""Select type of equation:
1. Linear:
y = mx+b
2. Exponential:
y = b^x
3. Parabola Quadratic:
y = ax^2 + bx + c
4. Reciprocal:
y = a/(x-b) + c
5. Sine wave:
y = a sin((x - b) * c) + d
6. Circle:
y = \u00B1sqrt(r^2 - (x - Ox)^2) + Oy
""")
t = input("Enter here: ")

def reDec(num): # Reduce decimals .0 to int
    if ".0" in str(num):
        return int(num)
    else:
        return num

def pos_neg(num): # Positive or negative:
    if num > 0:
        return "+ %i" % num
    else:
        noMin = str(num)[1:]
        return "- %i" % reDec(float(noMin))

def reciprocal(a, b, c, x):
    # a / (x+b) + c
    try:
        return a / (x+b) + c
    except ZeroDivisionError:
        return np.nan

def circle(r, Ox, Oy, x, negative=False):
    try:
        if negative:
            return math.sqrt(r ** 2 - (x + Ox) ** 2) * -1 + Oy
        else:
            return math.sqrt(r ** 2 - (x + Ox) ** 2) + Oy
    except ValueError:
        return np.nan

if t == '1':
    plt.title("Linear Equation")
    print("Enter a y=mx+b format equation:")
    print("""Example - y = 3x + 4
    y: 1
    m: 3
    b: 4
    """)
    y = float(input("y: "))
    m = float(input("m: "))
    b = float(input("b: "))

    y = reDec(y)
    m = reDec(m)
    b = reDec(b)
    
    
    slope = m / y
    x_values = [i for i in range(-20, 20)]
    y_values = [i * slope + b for i in range(-20, 20)]

    y = "" if y == 1 else str(y)
    m = "" if m == 1 else str(m)
    b = "" if b == 0 else pos_neg(b)
    lab = "%sy = %sx %s"%(y,m,b)
elif t == '2':
    plt.title("Exponential Equation")
    print("Enter a y=b^x format equation:")
    print("""Example - y=2^x
    b: 2
    """)
    b = float(input("b: "))
    x_values = [i / 10.0 for i in range(-200,200)]
    y_values = [b ** x for x in x_values]
    
    b = reDec(b)
    b = str(b)
    lab = "y = %s^x" % b
elif t == '3':
    plt.title("Quadratic Equation")
    print("Enter a y = ax^2 + bx + c format equation:")
    print("""Example: y = 2x^2 -5x + 8
    a: 2
    b: -5
    c: 8
    """)

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    x_values = [i / 10.0 for i in range(-200,200)]
    y_values = [a * x * x + b * x + c for x in x_values]

    a = "%g" % a
    b = "x" if b == 1 else "" if b == 0 else " %+gx" % b
    c = "" if c == 0 else " %+g" % c

    lab = "y = %sx^2%s%s" %(a, b, c)
elif t == '4':
    plt.title("Reciprocal Equation")
    print("Enter y = a/(x-b) + c format equation:")
    print("""Example - y = 5/(x - 2) + 10
    a: 5
    b: 2
    c: 10
    """)
    x_values = [i / 10.0 for i in range(-200,200)]

    a = float(input("a: "))
    b = float(input("b: ")) * -1
    c = float(input("c: "))

    y_values = [reciprocal(a, b, c, x) for x in x_values]
    x_values.insert(math.ceil(-10 * b) + 200, -b)
    y_values.insert(math.ceil(-10 * b) + 200, np.nan)

    a = "%g" % a
    b = "" if b == 0 else " %+g" % b
    c = "" if c == 0 else " %+g" % c

    
    lab = "y = %s/(x%s) %s" % (a, b, c)
elif t == '5':
    plt.title("Sine graph")
    print("Enter a y = a sin((x-b) * c) + d equation:")
    print("""Example - y = 5 sin((x - 3) * 2) + 9:
    a: 5
    b: 3
    c: 2
    d: 9
""")
    a = float(input("a: "))
    b = float(input("b: ")) * -1
    c = float(input("c: "))
    d = float(input("d: "))
    x_values = [i / 10.0 for i in range(-200,200)]
    y_values = [a * math.sin((x - b) * c) + d for x in x_values]

    a = "" if a == 1 else "%g" % a
    b = "" if b == 0 else " %+g" % b
    c = "" if c == 0 else " %g" % c
    d = "" if d == 0 else " %+g" % d

    lab = "y = %s sin((x%s) * %s) %s" %(a, b, c, d)
elif t == '6':
    plt.title("Circle")
    print("Enter a y = sqrt(r^2 - (x - Ox)^2) + Oy equation:")
    print("""Example: y = sqrt(3^2 - (x - 4)^2) + 5
    r: 3
    Ox: 4
    Oy: 5
""")
    r = float(input("r: "))
    Ox = float(input("Ox: ")) * -1
    Oy = float(input("Oy: "))

    x_values = [i / 10.0 for i in range(-200,200)]
    y_values = [circle(r, Ox, Oy, x) for x in x_values]
    y_bottom = [circle(r, Ox, Oy, x, True) for x in x_values]

    lab2 = "Origin: (%g, %g)" % (-Ox, Oy)
    plt.annotate(lab2, xy=(-Ox -3, Oy + 0.25))
    
    r = "%g" % r
    Ox = "" if Ox == 0 else " %+g" % Ox
    Oy = "" if Oy == 0 else " %+g" % Oy
    
    lab = u"y = \u00B1sqrt(%s^2 - (x%s)^2%s)" %(r, Ox, Oy)
    plt.plot(x_values, y_bottom, color='red', linewidth=5)

# x and y lines
x_lines1 = [i for i in range(-16, 18)]
x_lines2 = [0 for i in range(-16, 18)]

y_lines1 = [0 for i in range(-16, 18)]
y_lines2 = [i for i in range(-16, 18)]

plt.plot(x_lines1, x_lines2, color="black", linewidth=2)
plt.plot(y_lines1, y_lines2, color="black", linewidth=2)

plt.ylim(-16, 16)
plt.xlim(-16, 16)
plt.xticks(range(-16, 18, 2))
plt.yticks(range(-16, 18, 2))

plt.plot(x_values, y_values, label=lab, color='red', linewidth=5)
plt.legend()
plt.grid()
plt.gca().set_aspect('equal')
plt.show()
