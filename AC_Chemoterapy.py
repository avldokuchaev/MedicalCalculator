# Расчет доз введения препаратов по схеме химиотерапии AC

def square_body_chemotherapy(weight_float, height_float):
    square_body = 0.0167 * weight_float ** 0.5 * height_float ** 0.5
    square_body_result = round(square_body, 2)
    return square_body_result


height = float(input("Введите рост в сантиметрах: "))
weight = float(input("Введите вес в килограммах: "))
reduction_doze_doksorubicin = int(input("Если нужна редукция дозы Доксорубицина, введите цифру процентов, \
иначе введите \"0\": "))
reduction_doze_ciklophosphamid = int(input("Если нужна редукция дозы Циклофосфамида, введите цифру процентов, \
иначе введите \"0\": "))

res = square_body_chemotherapy(height, weight)

if reduction_doze_doksorubicin == 0 and reduction_doze_ciklophosphamid == 0:
    doksorubicin = 60
    ciklophosphamid = 600
    doksorubicin_doza = doksorubicin * res
    ciklophosphamid_doza = ciklophosphamid * res
    print(f"Площадь поверхности тела = {str(res)} квадратных метров")
    print(f"Необходимая доза Доксорубицина = {str(round(doksorubicin_doza))} мг")
    print(f"Необходимая доза Циклофосфамида = {str(round(ciklophosphamid_doza))} мг")
elif reduction_doze_doksorubicin == 0 and reduction_doze_ciklophosphamid != 0:
    doksorubicin = 60
    ciklophosphamid = 600
    doksorubicin_doza = doksorubicin * res
    ciklophosphamid_doza = (ciklophosphamid * res) - ((ciklophosphamid * res) * (reduction_doze_ciklophosphamid / 100))
    print(f"Площадь поверхности тела = {str(res)} квадратных метров")
    print(
        f"Необходимая доза Доксорубицина = {str(round(doksorubicin_doza))} мг")
    print(
        f"Необходимая доза Циклофосфамида (редуцированная на {reduction_doze_ciklophosphamid}%)  "
        f"= {str(round(ciklophosphamid_doza))} мг")
elif reduction_doze_doksorubicin != 0 and reduction_doze_ciklophosphamid == 0:
    doksorubicin = 60
    ciklophosphamid = 600
    doksorubicin_doza = (doksorubicin * res) - ((doksorubicin * res) * (reduction_doze_doksorubicin / 100))
    ciklophosphamid_doza = ciklophosphamid * res
    print(f"Площадь поверхности тела = {str(res)} квадратных метров")
    print(
        f"Необходимая доза Доксорубицина (редуцированная на {reduction_doze_doksorubicin}%) = "
        f"{str(round(doksorubicin_doza))} мг")
    print(f"Необходимая доза Циклофосфамида = {str(round(ciklophosphamid_doza))} мг")
else:
    doksorubicin = 60
    ciklophosphamid = 600
    doksorubicin_doza = (doksorubicin * res) - ((doksorubicin * res) * (reduction_doze_doksorubicin / 100))
    ciklophosphamid_doza = (ciklophosphamid * res) - ((ciklophosphamid * res) * (reduction_doze_ciklophosphamid / 100))
    print(f"Площадь поверхности тела = {str(res)} квадратных метров")
    print(
        f"Необходимая доза Доксорубицина (редуцированная на {reduction_doze_doksorubicin}%) = "
        f"{str(round(doksorubicin_doza))} мг")
    print(
        f"Необходимая доза Циклофосфамида (редуцированная на {reduction_doze_ciklophosphamid}%) = "
        f"{str(round(ciklophosphamid_doza))} мг")

k = input("Нажмите Enter для выхода! ")
