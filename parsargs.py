import argparse
from work_with_file import read_file, read_with_where, read_with_aggregate


def parse_args():
    file_name = ""
    where_arg = []
    aggregate_arg = []

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help="Input name file")
    parser.add_argument("--where", type=str)
    parser.add_argument("--aggregate", type=str)
    args = parser.parse_args()
    file_name = args.file

    if args.where:
        for op in [">", "<", "="]:
            if op in args.where:
                column, value = args.where.split(op)
                where_arg = [column.strip(), op, value.strip()]
                read_with_where(file_name, where_arg)
                break

    if args.aggregate:
        column, func = args.aggregate.split("=")
        if func.strip() in ["min", "max", "avg"]:
            aggregate_arg = [column.strip(), func.strip()]
            read_with_aggregate(file_name, aggregate_arg)

    if len(where_arg) == 0 and len(aggregate_arg) == 0:
        read_file(file_name)
