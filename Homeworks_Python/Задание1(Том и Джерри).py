x = float(input("Введите скорость джерри в метрах в секунду: "))
y = float(input("Введите скорость тома в метрах в секунду: "))
s = float(input("Введите начальное расстояние между ними в метрах: "))
z = y - x
if z <= 0:
    print("том не сможет поймать Джерри")
else: t = s / z
print("том догонит джерри через", t, "секунд")
