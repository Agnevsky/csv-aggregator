import csv
from formatter import output_format as of
from parsargs import parse_args as pa



def read_file():
    file_name = pa()
    file_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        table_from_file = csv.reader(file)
        for s in table_from_file:
            file_list.append(s)
    
    print(of(file_list))

