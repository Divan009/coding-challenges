import argparse
import sys


def field_converter(field):
    """
    converts "1 2" or "1,2" into [1, 2]
    """
    if "," in field:
        nums_list = field.split(",")
    else:
        nums_list = field.split(" ")

    int_list = [int(item) for item in nums_list]

    check_0 = any(num == 0 for num in int_list)
    if check_0:
        print("cut: fields are numbered from 1")
        sys.exit()

    return int_list


def file_read_from_content(content, filename, column, delimiter="\t"):

    nums_list = field_converter(column)
    len_nums_list = len(nums_list)

    for line in content:
        # print(line)
        stripped_columns = line.strip()
        columns = stripped_columns.split(delimiter)

        if not filename or filename.endswith(".csv"):
            # if this delimiter == ,
            if delimiter == ",":
                if len_nums_list == 1:
                    print(columns[int(column) - 1])
                else:
                    for i in range(len_nums_list):
                        print(columns[int(nums_list[i]) - 1], end=", ")
                    print(end="\n")
            else:
                print(stripped_columns)

        elif filename.endswith(".tsv"):
            if delimiter == "\t":
                if len_nums_list == 1:
                    print(columns[int(column) - 1])
                else:
                    for i in range(len_nums_list):
                        print(columns[int(nums_list[i]) - 1], end=", ")
                    print(end="\n")
            else:
                print(stripped_columns)

        else:
            print(stripped_columns)


if __name__ == "__main__":
    msg = "A copy of cut tool of Unix."
    parser = argparse.ArgumentParser(
        prog="cut",
        description=msg,
        epilog="Thanks for using %(prog)s! :)",
    )
    parser.add_argument("filename", nargs="?", default=None, help="the file to analyze")
    parser.add_argument("-f", "--fields", help="select  only  these fields")
    parser.add_argument("-d", "--delimiter", help="select  only  these fields")
    args = parser.parse_args()

    delimiter = args.delimiter if args.delimiter else "\t"

    # filename = sys.argv# Assuming filename is the first argument  # Assuming the field argument is the fourth argument

    # print("Filename:", filename)

    if not args.filename:
        content = sys.stdin.read()
        delimiter = ","
        filename = None
    else:
        filename = str(args.filename)
        with open(args.filename, "r") as f:
            content = f.readlines()

    if args.fields:

        file_read_from_content(content, filename, args.fields, delimiter)
