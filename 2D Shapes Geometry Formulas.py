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
    Area_of_a_Sqruare = area **2
    print("The area of a square is",Area_of_a_Sqruare)
elif 



