class Shape:
    __width = None
    __height = None

    def set_value(self, height, width):
        self.__height = height
        self.__width = width

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width
