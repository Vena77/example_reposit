class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, go):
        if go == "go":
            return f"{self.name} {self.color} car go"
        else:
            return "Car don't go"

    @staticmethod
    def stop(stop):
        if stop == "stop":
            return "Car stop"
        else:
            return "Car don't stop"

    @staticmethod
    def turn(direction):
        if direction == "right":
            dir1 = "Car turn right"
        elif direction == "left":
            dir1 = "Car turn left"
        elif direction == "back":
            dir1 = "Car go back"
        else:
            dir1 = "Car go forward"
        return dir1

    def show_speed(self) -> object:
        return  f"Скорость машины {self.speed} км/ч."

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"{super().show_speed()} Превышение скорости больше 60 км/ч."
        else:
            return super(TownCar, self).show_speed()

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"{super().show_speed()} Превышение скорости больше 40 км/ч."
        else:
            return super().show_speed()

class SportCar(Car):
    pass
class PoliceCar(Car):
    pass

townCar = TownCar(90,"red","Volvo",True)
print(townCar.show_speed())
workCar = WorkCar(30,"black","Kia",False)
print(workCar.show_speed())
sportCar = SportCar(40,"white","Tayota",True)
print(sportCar.turn("left"))
policeCar = PoliceCar(80,"blue","Ford",True)
print(sportCar.turn("hi"))
print(sportCar.go("go"))
print(policeCar.stop("stop"))
print((policeCar.stop("ghh")))
print(workCar.go("jjj"))