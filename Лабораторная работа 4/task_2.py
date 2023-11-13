import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as inp:
        reader = csv.DictReader(inp)
        csv_data = [i for i in reader]

    with open(OUTPUT_FILENAME, 'w') as out:
        json.dump(csv_data, out, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
