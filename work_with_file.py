import csv
from formatter import output_format

def start_func(file_name: str, where_arg: list[str], aggregate_arg: list[str]):
    if len(where_arg) == 0 and len(aggregate_arg) == 0:
        output_format(read_file(file_name))
    elif len(aggregate_arg) == 0:
        output_format(read_with_where(read_file(file_name), where_arg))
    elif len(where_arg) == 0:
        output_format(read_with_aggregate(read_file(file_name), aggregate_arg))
    else:
        output_format(read_with_aggregate(read_with_where(read_file(file_name), where_arg), aggregate_arg))

def read_file(file_name: str):
    file_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        for s in table_from_file:
            file_list.append(s)

    return file_list

def read_with_where(file_list: list[str], where_arg: list[str]):
    result_list = []
    for ls in file_list:
        if where_arg[1] == '=':
            if where_arg[0] in ls or where_arg[2].title() in ls:
                result_list.append(ls)

    return result_list


def read_with_aggregate(file_list: str, aggregate_op: list[str]):
    result_list = []
    options = {"min": min, "max": max, "avg": lambda x: sum(x) / len(x)}
    option = aggregate_op[1]
    list_for_math = []
    index = 0 
    for ls in file_list:
        if aggregate_op[0] in ls:
            index = ls.index(aggregate_op[0])
        else:
            list_for_math.append(float(ls[index]))

    if option in options:
        result_list.append([option])
        result_list.append([options[option](list_for_math)])

    return result_list


