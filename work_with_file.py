import csv
from formatter import output_format


def read_with_where(file_name: str, where_arg: list[str]):
    file_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        header = file.readline().lstrip("\n").rstrip("\n").split(",")
        file_list.append(header)
        index = header.index(where_arg[0])
        for s in table_from_file:
            if where_arg[1] == "=":
                if (
                    where_arg[2].lower() in [i.lower() for i in s]
                    and where_arg[0] not in s
                ):
                    file_list.append(s)
            elif where_arg[1] == "<":
                if s[index].isdigit and float(s[index]) < float(where_arg[2]):
                    file_list.append(s)
            elif where_arg[1] == ">":
                if s[index].isdigit and float(s[index]) > float(where_arg[2]):
                    file_list.append(s)

    print(output_format(file_list))


def read_with_aggregate(file_name: str, aggregate_op: list[str]):
    file_list = []
    options = {"min": min, "max": max, "avg": lambda x: sum(x) / len(x)}
    option = aggregate_op[1]
    list_for_math = []
    index = 0

    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        for s in table_from_file:
            if aggregate_op[0] in s:
                index = s.index(aggregate_op[0])
            else:
                list_for_math.append(float(s[index]))

    if option in options:
        file_list.append([option])
        file_list.append([options[option](list_for_math)])

    print(output_format(file_list))


def read_file(file_name: str):
    file_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        for s in table_from_file:
            file_list.append(s)

    print(output_format(file_list))
