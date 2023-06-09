'''ENCAPSULATION IN PYTHON'''

class Car:
    def __int__(self, speed, color):
        self.speed = speed
        self.color = color

ford = Car(200, "white")
camry = Car(230, "blue")
honda = Car(240, "wine")


print(ford.speed)



class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color

    def setspeed(self, value):
        self.speed = value

    def getspeed(self):
        return self.speed

ford = Car(200, "white")
benz = Car(230, "wine")
honda = Car(250, "black")

ford.setspeed(300)
print(ford.getspeed())




class Car:
    def __init__(self, speed, color):
        self. __speed = speed
        self. __color = color

    def setspeed(self, value):
        self. __speed = value
    
    def getspeed(self):
        return self. __speed
    
ford = Car(200, "white")
benz = Car(230, "wine")
honda = Car(250, "black")

ford.setspeed(300)
print(ford.getspeed())




class person:
    def __init__(self, speed, color):
        self.__carspeed = speed
        self.__carcolor = color


    def setcar(self, value):
        self.__carspeed = value


    def getcar(self):
        return self.__carspeed


    def setcolor(self, value):
        self.__carcolor = value


    def getcolor(self):
        return self.__carcolor
    

ford = person(200, "white")
camry = person(210, "blue")
benz = person(250, "black")


print(ford.getcar())
print(camry.getcar())
print(benz.getcar())

# set the value of speed you want to change
ford.setcar(300)
camry.setcar(500)
benz.setcar(700)

print(ford.getcar())
print(camry.getcar())
print(benz.getcar())


# This will call out the colors one after the other
# Also it will get it from what you set above

ford.setcolor("wine")
camry.setcolor("violent")
benz.setcolor("green")

print(ford.getcolor())
print(camry.getcolor())
print(benz.getcolor())

# This will place both the speed and color side by side
print(ford.getcar(), ford.getcolor())
print(camry.getcar(), camry.getcolor())
print(benz.getcar(), benz.getcolor())






class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def setheight1(self, value):
        self.__height1 = value

    def getheight1(self):
        return self.__height1
    
    def setwidth1(self, value):
        self.__width1 = value

    def getwidth1(self):
        return self.__width1
    
    def setheight2(self, value):
        self.__height2 = value

    def getheight2(self):
        return self.__height2
    
    def setwidth2(self, value):
        self.__width2 = value

    def getwidth2(self):
        return self.__width2
    
    def area(self):
        return self.__height * self.__width


rectangle1 = Rectangle(100, 5)
rectangle2 = Rectangle(10, 5)

print(0.5 * rectangle1.area())
print(0.5 * rectangle2.area()) 



class Car:
    def __init__(self, speed, color):
        self.__carspeed = speed
        self.__carcolor = color

    def setspeed(self, value):
        self.__carspeed = value

    def getspeed(self):
        return self.__carspeed
    
ford = Car(300, "white")
honda = Car(310, "wine")
benz = Car(350, "black")


ford.getspeed()
print(ford.getspeed())


ford.setspeed(500)
print(ford.getspeed())



class Car:
    def __init__(self, speed, color):
        self.carspeed = speed
        self.color = color

ford = Car(300, "white")
honda = Car(320, "wine")
audi = Car(330, "blue")

# print(ford.carspeed)

ford.carspeed = 349
print(ford.carspeed)



class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public_method(self):
        print("public")
        
        return self.__c

hello = Hello("name")
print(hello.a)
print(hello._b)
print(hello.public_method())

