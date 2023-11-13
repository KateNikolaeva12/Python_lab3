import json

INPUT = 'input.json'


def task() -> float:
    with open(INPUT) as file:
        s = 0
        slovar = json.load(file)
        for i in slovar:
            s += i['score'] * i['weight']
    return round(s, 3)


print(task())
