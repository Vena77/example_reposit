from random import choice
spisok_print = []
spisok_scan = []
spisok_xcerox = []
dict_teh = {"printer":spisok_print, "scaner":spisok_scan, "xcerox":spisok_xcerox}

class Sclad:
    list_teh = []
    kolteh_in_sclad = {"printer":0, "scaner":0, "xcerox":0}
    @classmethod
    def get_tehnica_on_sclad(cls, cnt1, what):
        if cnt1<=len(dict_teh[what]):
          for x in range(cnt1):
            dict_teh[what][x].depart = "sclad"
            cls.list_teh.append(dict_teh[what][x])
            cls.kolteh_in_sclad[what] = cls.kolteh_in_sclad[what]+1
          return [cls.list_teh[x].name for x in range(0,len(cls.list_teh))]
        else:
          return f"Enter another number. You have only {len(dict_teh[what])} printer"

    @classmethod
    def give_tehnica_from_sclad(cls, d, cnt1, what):
        if cnt1 <= cls.kolteh_in_sclad[what]:
            cls.kolteh_in_sclad[what] = cls.kolteh_in_sclad[what] - cnt1
            for x in range (cnt1):
                dict_teh[what][x].depart = d
                cls.list_teh.remove(dict_teh[what][x])
            return f"Оставшаяся техника на складе: {[cls.list_teh[x].name for x in range(0,len(cls.list_teh))]}"
        else:
            return f"Enter another number. You have only {cls.kolteh_in_sclad[what]} printer"

class Orgteh:
    def __init__(self, name, ser_num, depart):
        self.name = name
        self.ser_num = ser_num
        self.depart = depart

class Printer(Orgteh):
    cnt = 0

    def __init__(self, name, ser_num, depart):
        super().__init__(name, ser_num, depart)
        Printer.cnt+=1
        #Printer.spisok.append({"name":name, "ser_num":ser_num, "depart":depart})
        spisok_print.append(self)

    def __str__(self):
       return f"Принтер наименование {self.name}, серийный номер: {self.ser_num}"

    def input_new_printer(self, count):
        for x in range(count):
          print("Новый принтер добавлен")
          yield Printer(name=choice(["SamsungMP22", "HpRR11","CanonST556 "]),
                        ser_num=f"Num556{self.cnt}",
                        depart="None")

class Scaner(Orgteh):
    cnt = 0
    def __init__(self, name, ser_num, depart):
        super().__init__(name, ser_num, depart)
        Scaner.cnt += 1
        spisok_scan.append(self)

    def __str__(self):
        return f"Сканер наименование {self.name}, серийный номер: {self.ser_num}"

    def input_new_scaner(self, count):
        for x in range (count):
            print ("Новый сканер добавлен")
            yield Scaner (name=choice (["ScanerMP22", "ScanerRR11", "ScanerST556 "]),
                           ser_num=f"Num777{self.cnt}",
                           depart="None")

class Xcerox(Orgteh):
    cnt = 0

    def __init__(self, name, ser_num, depart):
        super().__init__(name, ser_num, depart)
        Xcerox.cnt+=1
        spisok_xcerox.append(self)

    def __str__(self):
        return f"Ксерокс наименование {self.name}, серийный номер: {self.ser_num}"

    def input_new_xcerox(self, count):
        for x in range(count):
          print("Новый ксерокс добавлен")
          yield Xcerox(name=choice(["XceroxMP22", "XceroxRR11","XceroxST556 "]),
                        ser_num=f"Num126{self.cnt}",
                        depart="None")

class NewException(Exception):
    def __init__(self,text):
        self.text = text


a = input("Enter number(количество) new printer, scaner and xcerox: ")
a = a.split()
spisok_print[0] = Printer("printer1", "prn1234g", "None")
spisok_scan[0] = Scaner("Scan222", "rscab54", "None")
spisok_xcerox[0] = Xcerox("Xcerox1","rt543","None")
for prin in spisok_print[0].input_new_printer(int(a[0])-1):
  pass

for prin in spisok_scan[0].input_new_scaner(int(a[1])-1):
  pass

for prin in spisok_xcerox[0].input_new_xcerox(int(a[2])-1):
  pass

kol = input("You have "+ str(Printer.cnt) +" new printer. Enter how mach printer do you want to put sclad: ")
print(Sclad.get_tehnica_on_sclad(int(kol), "printer"))

print(Sclad.get_tehnica_on_sclad(int(a[1]),"scaner"))
print(Sclad.get_tehnica_on_sclad(int(a[2]),"xcerox"))

flag = True
while flag:
 kol = input ("You have " + str (len (Sclad.list_teh)) + " technics on sclad. Enter how mach printer do you want to take?: ")
 a = input ("Enter where department?: ")
 try:
    if kol.isdigit():
       print (Sclad.give_tehnica_from_sclad (a, int (kol), "printer"))
       flag = False
       ll = []
       for i in range (0, len (spisok_print)):
           ll.append ((spisok_print[i].name, spisok_print[i].depart))
       print (f"Где теперь принтеры: {ll}")
       print (f"Количество техники на складе: {Sclad.kolteh_in_sclad}")
    else:
       raise NewException("Enter number!!!")
 except Exception as err:
      print (err)

# То же самое для сканеров и ксероксов
