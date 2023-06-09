from polygon import Shape

class Triangle(Shape):
    def area(self):
        return self.get_height() * self.get_width()/2
    