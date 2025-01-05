def perimeter (a, b):
    return 2*a + 2*b

def area (a, b):
    return a*b

def diagonal (a, b):
    return ((a ** 2) + (b ** 2)) ** 0.5

def show_results (a, b):
    print("Obwód prostokąta o bokach {} i {} to:".format(a,b), perimeter(a,b))
    print("Pole prostokąta o bokach {} i {} to:".format(a,b), area(a,b))
    print("Przeciwprostokątna w prostokącie o bokach {} i {} to:".format(a,b), diagonal(a,b))


show_results(4,5)
show_results(2678,5678)
show_results(344555,788998)