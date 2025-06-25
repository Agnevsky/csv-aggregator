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