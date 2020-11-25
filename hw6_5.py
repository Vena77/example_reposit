class Stationery:
    def __init__(self,title):
        self.title = title

    @staticmethod
    def draw():
        return "Запуск отрисовки"

class Pen(Stationery):
    def draw(self):
        return f"Draw {self.title}"

class Pencil(Stationery):
    def draw(self):
        return f"Draw {self.title}"

class Handle(Stationery):
    def draw(self):
        return f"Draw {self.title}"

sta = Stationery("common")
print(sta.draw())
pen = Pen("pen")
print(pen.draw())
pencil = Pencil("pencil")
print(pencil.draw())
handle = Handle("handle")
print((handle.draw()))