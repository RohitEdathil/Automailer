from csv import reader


def parse(file: str) -> tuple:
    """
    Opens csv file, reads the data.

    Returns (header,data)
    header: tuple of header strings
    data: list of tuples of data

    """
    with open(file, 'r') as csvfile:
        csvreader = reader(csvfile)
        header = next(csvreader)
        data = [row for row in csvreader]
    return (tuple(header), tuple(data))


