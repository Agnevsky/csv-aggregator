import argparse
from work_with_file import start_func


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help="Input name file")
    parser.add_argument("--where", type=str)
    parser.add_argument("--aggregate", type=str)
    return parser.parse_args()

def parse_args():
    args = get_args()
    file_name = args.file
    where_arg = []
    aggregate_arg = []

    if args.where:
        for op in ["<=", ">=", ">", "<", "="]:
            if op in args.where:
                column, value = args.where.split(op, 1)
                where_arg = [column.strip(), op, value.strip()]
                print(where_arg)
                break

    if args.aggregate:
        column, func = args.aggregate.split("=")
        if func in ["min", "max", "avg"]:
            aggregate_arg = [column, func]
            
    start_func(file_name, where_arg, aggregate_arg)
