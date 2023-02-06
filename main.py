tikets = int(input("Больше 4 билетов - скидка 10% \n"
                   "Введите количество билетов: "))
age = list(map(int, input("Укажите возраст посетителей: ").split()))

while tikets != len(age):
    age = list(map(int, input("Количество поситетелей не совпадает с количеством билетов. \n"
                              "Укажите возраст поситетелей: ").split()))
price = []
for i in age:
    if i in range (0, 18):
        price.append(0)
    elif i in range (18, 25):
        price.append(990)
    else:
        price.append(1390)
if tikets > 3:
    print("Сумма со скидкой: ", sum(price) - ((sum(price) / 100)* 10),"рублей")
else:
    print("Сумма: ", sum(price), "рублей")