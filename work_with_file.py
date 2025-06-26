import csv
from formatter import output_format


def read_with_where(file_name: str, where_arg: list[str]):
    file_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        header = file.readline().lstrip('\n').rstrip('\n').split(',')
        file_list.append(header)
        index = header.index(where_arg[0])
        for s in table_from_file:
            if where_arg[1] == "=":
                if where_arg[2].lower() in [i.lower() for i in s] and where_arg[0] not in s:
                    print([i.lower() for i in s])
                    file_list.append(s)
            elif where_arg[1] == "<":
                if s[index].isdigit and float(s[index]) < float(where_arg[2]):
                    file_list.append(s)
            elif where_arg[1] == ">":
                if s[index].isdigit and float(s[index]) > float(where_arg[2]):
                    file_list.append(s)

    print(output_format(file_list))



def read_with_aggregate():
    pass

def read_file(file_name: str):
    file_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        for s in table_from_file:
            file_list.append(s)
    
    print(output_format(file_list))

