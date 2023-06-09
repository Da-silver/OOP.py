'''INHERITANCE IN PYTHON'''

# class Polygon:
#     __width = None
#     __height = None

#     def set_value(self, height, width):
#         self.__height = height
#         self.__width = width

# class Rectangle(Polygon):
#     def area(self):
#         return self.__width * self.__height

# class Triangle(Polygon):
#     def area(self):
#         return self.__width * self.__height/2
    
# rec1 = Rectangle()
# tri1 = Rectangle()

# rec1.set_value(50, 40)
# tri1.set_value(100, 2)

# print(rec1.area())
# print(tri1.area())


# class Shape:
#     __height = None
#     __width = None

#     def set_value(self, height, width):
#         self.__height = height
#         self.__width = width

#     def get_height(self):
#         return self.__height
    
#     def get_width(self):
#         return self.__width
    
# class Rectangle(Shape):
#     def area(self):
#         return self.get_height() * self.get_width()
    
# class Triangle(Shape):
#     def area(self):
#         return self.get_height() * self.get_width()/2
    
# rectangle1 = Rectangle()
# triangle1 = Triangle()

# rectangle1.set_value(50, 30)
# triangle1.set_value(60, 40)

# print(rectangle1.area())
# print(triangle1.area())
