import argparse


def tsv_file(file_name, column, delimiter="\t"):
    try:
        try:
            if int(column) == 0:
                print("cut: fields are numbered from 1")
                return
        except ValueError:
            print("please give integer only")
            return
        
        with open(file_name, "r") as f:
            if str(file_name).endswith(".tsv"): 
                if delimiter == "\t":  
                    for line in f:
                        columns = line.strip().split(delimiter)
                        print(columns[int(column) - 1])
                else:
                    for line in f:
                        print(line.strip())
            elif str(file_name).endswith(".csv"):
                if delimiter == ",":
                    for line in f:
                        columns = line.strip().split(delimiter)
                        print(columns[int(column) - 1])
                else:
                    for line in f:
                        print(line.strip())

    except IndexError:
        print()


if __name__ == "__main__":
    msg = "A copy of cut tool of Unix."
    parser = argparse.ArgumentParser(
        prog="cut",
        description=msg,
        epilog="Thanks for using %(prog)s! :)",
    )
    parser.add_argument("filename", help="Provide a filename")
    parser.add_argument("-f", "--fields", help="select  only  these fields")
    parser.add_argument("-d", "--delimiter", help="select  only  these fields")
    args = parser.parse_args()

    delimiter = args.delimiter if args.delimiter else "\t"

    if args.fields:
        tsv_file(args.filename, args.fields, delimiter)
