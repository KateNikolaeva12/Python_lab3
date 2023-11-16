import json

INPUT = 'input.json'


def task() -> float:
    with open(INPUT) as file:
        slovar = json.load(file)
        s = [num['score'] * num['weight'] for num in slovar]
    return round(sum(s), 3)


print(task())
