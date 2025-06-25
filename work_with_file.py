import csv
from formatter import output_format


def read_with_where(file_name: str, where_arg: list[str]):
    file_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        for s in table_from_file:
            if where_arg[1] == "=":
                for i in s:
                    if i == where_arg[2] or i == where_arg[0]:
                        file_list.append(s)
            if where_arg[1] == "<":
                pass
        
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

