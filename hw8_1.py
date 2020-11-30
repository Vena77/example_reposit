class Date:

    def __init__(self, data):
        self.data = data

    def get_num(self):
        dict1 = {"число":self.data[0:2],"месяц":self.data[3:5],"год":self.data[6:10]}
        return dict1

    @staticmethod
    def get_check_month(st):
        a = st[3:5]
        if int(a[0:1]) != 0:
            if int(a) < 13:
                return "Валидация пройдена"
            else:
                return "Нет такого месяца"
        else:
            if int(a[1:2]) != 0:
                return "Валидация пройдена"
            return "Нет такого месяца"

date = Date("12.01.2007")
print(date.get_num())
print(date.get_check_month("12.14.2007"))