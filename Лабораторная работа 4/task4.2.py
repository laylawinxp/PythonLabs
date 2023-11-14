import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as fin:
        dict_reader = [line_ for line_ in csv.DictReader(fin, delimiter=",", quotechar="\n")]
    with open(OUTPUT_FILENAME, "w") as fout:
        json.dump(dict_reader, fout, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
