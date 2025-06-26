from tabulate import tabulate


def output_format(list: list[str]):
    table = tabulate(list[1:], headers=list[0], tablefmt="grid")
    print(table)
