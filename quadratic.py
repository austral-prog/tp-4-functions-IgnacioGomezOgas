# Replace the "ANSWER HERE" for your answer
def roots(a, b, c):
    if (b**2 -4*a*c)<0:
        return "( )"
    elif (b**2 -4*a*c)==0:
        return f"({(-b/(2*a))})"
    else:
        return f"({((-b+(b**2-4*a*c)**0.5)/2*a)}, {((-b-(b**2-4*a*c)**0.5)/2*a)})"
def value_y(a, b, c, x):
    return a*(x**2) + b*x + c

def to_string(a, b, c):
    if a!=0 and b!=0:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
    elif a==0 and b!=0:
        return f"f(x) = {b} * X + {c}"
    elif a==0 and b==0:
        return f"f(x) = {c}"
    elif a!=0 and b==0:
        return f"f(x) = {a} * X^2 + {c}"
def derivation(a, b, c):
    if a==0:
        return f"f'(x) = {b}"
    elif b==0:
        return f"f'(x) = {2*a} * X"
    else:
        return f"f'(x) = {2*a} * X + {b}"
