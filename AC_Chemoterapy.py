# Расчет доз введения препаратов по схеме химиотерапии AC

def square_body_chemotherapy(weight_float, height_float):
    square_body = 0.0167 * weight_float ** 0.5 * height_float ** 0.5
    square_body_result = round(square_body, 2)
    return square_body_result


height = float(input("Введите рост в сантиметрах: "))
weight = float(input("Введите вес в килограммах: "))
schema_therapy = input("Введите название схемы (AC): ")
reduction_doze = int(input("Если нужна редукция дозы, введите цифру процентов, иначе введите \"0\": "))

res = square_body_chemotherapy(height, weight)

if schema_therapy.upper() == "AC" or schema_therapy.upper() == "АС" and reduction_doze == 0:
    doksorubicin = 60
    ciklophosphamid = 600
    doksorubicin_doza = doksorubicin * res
    ciklophosphamid_doza = ciklophosphamid * res
    print(f"Площадь поверхности тела = {str(res)} квадратных метров")
    print(f"Необходимая доза Доксорубицина = {str(round(doksorubicin_doza))} мг")
    print(f"Необходимая доза Циклофосфамида = {str(round(ciklophosphamid_doza))} мг")
elif schema_therapy.upper() == "AC" or schema_therapy.upper() == "АС" and reduction_doze != 0:
    doksorubicin = 60
    ciklophosphamid = 600
    doksorubicin_doza = (doksorubicin * res) - ((doksorubicin * res) * (reduction_doze / 100))
    ciklophosphamid_doza = (ciklophosphamid * res) - ((ciklophosphamid * res) * (reduction_doze / 100))
    print(f"Площадь поверхности тела = {str(res)} квадратных метров")
    print(
        f"Необходимая доза Доксорубицина (редуцированная на {reduction_doze}%) = {str(round(doksorubicin_doza))} мг")
    print(
        f"Необходимая доза Циклофосфамида (редуцированная на {reduction_doze}%) = {str(round(ciklophosphamid_doza))}"
        f" мг")
else:
    print("Вы ввели не ту схему!")

k = input("Нажмите Enter для выхода! ")
