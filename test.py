import argparse


def parse_args():
    file_name = ""
    where_arg = []

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help="Input name file")
    parser.add_argument("--where", type=str)
    # parser.add_argument('--aggregate', type=str)
    args = parser.parse_args()
    file_name = args.file

    if args.where is None:
        pass
    else:
        for i in args.where:
            if i in [">", "<", "="]:
                where_arg.append(args.where.split(i)[0])
                where_arg.append(i)
                where_arg.append(args.where.split(i)[1])

    print(file_name, where_arg)


parse_args()
