from tabulate import tabulate


def output_format(list: list[str]):
    try:
        table = tabulate(list[1:], headers=list[0], tablefmt="grid")
        print(table)
    except IndexError:
        print("...Файл пуст. Обработка не требуется...")
