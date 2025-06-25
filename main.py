import csv
import argparse


def parse_args():
    file_name = ""
    where_arg = []

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, help="Input name file")
    # parser.add_argument('--where', type=str)
    # parser.add_argument('--aggregate', type=str)
    args = parser.parse_args()
    file_name = args.file

    return file_name


def read_file(file_name: str):
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        for s in table_from_file:
            print('|'.join(s))

read_file(parse_args())

if __name__ == "__main__":
    parse_args()