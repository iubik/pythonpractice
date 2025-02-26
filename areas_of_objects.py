#function to calculate the area of a triangle.
def area_of_triangle():
    base = int(input("Enter the measurement of base: "))
    height = int(input("Enter the measurement of height: "))
    area = 0.5 * base * height #formula for area of a triangle is a half base x height
    print("The area of this triangle is: ", area)
    return area
    

#area of rectangles and squares. 
def area_of_rectangle():
    length = int(input("Enter the length of your rectangle or square: "))
    width = int(input("Enter the measurement of width of rectangle or square: "))
    area = length * width
    print("The area of this object is: ", area)
    return area



#function to choose the area of the object I want calculated.
def function_chooser():
    chosen_area = int(input("Choose the object you want to calculate area of:\n 1. rectangle or square \n 2. Triangle \n Answer: ",))
    
    #Loop to allow the user to make a correct object choice.
    while True:
        if chosen_area == 1:
            area_of_rectangle()
            break
        elif chosen_area == 2:
            area_of_triangle()
            break
            

function_chooser()