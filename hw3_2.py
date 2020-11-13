def myf(name, surname, ye, city, email, tel):
    print(name, surname, ye, city, email, tel)

dict1 = {}
d = input("Enter name:")
dict1["name"] = d
d = input("Enter surname:")
dict1["surname"] = d
d = input("Enter born year:")
dict1["ye"] = d
d = input("Enter email:")
dict1["email"] = d
d = input("Enter telephon:")
dict1["tel"] = d
d = input("Enter city:")
dict1["city"] = d

myf(name="Elena", surname="Danilova", city="Kazan", ye=1991, email="eledan@gmail.com", tel="+7(915)565-67-22")
myf(name=dict1["name"], surname=dict1["surname"], city=dict1["city"], ye=dict1["ye"], email=dict1["email"], tel=dict1["tel"])