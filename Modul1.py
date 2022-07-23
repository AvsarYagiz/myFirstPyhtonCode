people = []
bmi: float


def bmi_calculator(number, number2):
    global bmi
    bmi = round(number / (number2 ** 2), 2)
    return bmi


while True:
    try:
        count = int(input('For how many people BWI will be calculated?: '))
        break
    except ValueError:
        print('Please enter only integer value!')

for i in range(count):
    name = str(input('Please enter your name: '))
    weight = float(input('Please enter your weight(kg): '))
    height = int(input('Please enter your height(cm): ')) / 100
    bmi_calculator(weight, height)
    record = {name: bmi}
    people.append(record)
i = 0
for i in range(count):
    print(list(people[i].keys())[0], list(people[i].values())[0])

