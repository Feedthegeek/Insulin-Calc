# Nicholas Herrick
# 2019
from datetime import date


today = date.today()


print('Hello, today is ' + str(today))
#blood sugar input
bs = int(input('Blood Sugar: '))
bst = int(input('Blood Sugar Target: '))
crcf = int(input('Correction Factor: '))

#assign insulin value and carbohydrate input
insamt = float((bs - bst) / (crcf))
carbs = int(input('Carbohydrates: '))
carb_ratio = int(input('Isulin to carbohydrate ratio is 1: '))
carb_crct = float((carbs / carb_ratio))

#insulin delivery check and print
for n in insamt:
    n = float(round(insamt, 2))
    print('No insulin will be delivered')
    exit


print('Delivering ' + str(round(insamt + carb_crct, 2)) + ' units.')
