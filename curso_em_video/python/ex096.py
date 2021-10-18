def area(a, b):
    ar = a * b
    print(f'The area of the quadrilateral {a}x{b} is {ar:.2f}m²')


l1 = float(input('base of the quadrilateral: '))
l2 = float(input('height of the quadrilateral: '))
area(l1, l2)
