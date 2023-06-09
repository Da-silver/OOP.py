from polygon import Shape

class Rectangle(Shape):
    def area(self):
        return self.get_height() * self.get_width()
