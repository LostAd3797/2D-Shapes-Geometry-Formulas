import math
print("1.Perimeter of a Square")
print("2.Perimeter of a Rectangle")
print("3.Area of a Square")
print("4.Area of a Rectangle")
print("5.Area of a Triangle")
print("6.Area of a Trapezoid")
print("7.Area of a Circle")
print("8.Circumference of a Circle")

user= input("Select a choice from 1 through 8:")

if user == "1":
    side_length = float(input("Enter the sides of the length of the square:"))
    Perimeter_of_a_Square = 4*side_length
    print("The Perimeter of a Square is",Perimeter_of_a_Square)
elif user == "2":
    length = float(input("Enter the length of the Rectangle:"))
    width = float(input("Enter the width of the Rectangle:"))
    Perimeter_of_a_Rectangle = 2*(length + width)
    print("The Perimeter of a Rectangle is",Perimeter_of_a_Rectangle)
elif user == "3":
    area = float(input("Enter a number for area of a square:"))
    Area_of_a_Square = area **2
    print("The area of a square is",Area_of_a_Square)
elif user == "4":
    length= float(input("Enter the length of rectangle:"))
    width= float(input("Enter the width of a rectangle:"))
    Area_of_a_Rectangle= length * width
    print("The area of the rectangle is",Area_of_a_Rectangle)
elif user == "5":
    base= float(input("Enter the base of the triangle:"))
    height = float(input("Enter the height of the triangle:"))
    Area_of_a_Triangle = 1/2 *(base)*(height)
    print("The area of the triangle is",Area_of_a_Triangle)
elif user == "6":
    base1= float(input("Enter the first base for the trapezoid:"))
    base2= float(input("Enter the second base for the trapezoid:"))
    heigth3= float(input("Enter the height of the trapezoid:"))
    Area_of_a_Trapezoid = 1/2 *(base1+base2)*heigth3
    print("The area of the trapezoid is",Area_of_a_Trapezoid)
elif user == "7":
    radius= float(input("Enter the radius of the circle:"))
    Area_of_a_circle = math.pi*(radius**2)
    print("The area of the circle is",round(Area_of_a_circle,2))
elif user == "8":
    radius2 = float(input("Enter the radius for the circumference of the circle:"))
    cicumference_of_the_circle= 2*math.pi*(radius2)
    print("The circumference of the circle is",round(cicumference_of_the_circle,2))
else:
    print("Invalid choice")

          

    



