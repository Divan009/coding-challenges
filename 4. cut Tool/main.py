import argparse


def tsv_file(file_name, column, delimiter="\t"):
    # try:
    nums_list = column.split(',')
    len_nums_list = len(nums_list)
    # try:

    check_0 = any(int(num)==0 for num in nums_list)

    if check_0:
        print("cut: fields are numbered from 1")
        return
    
    
    with open(file_name, "r") as f:
        for line in f:
            stripped_columns = line.strip()
            columns = stripped_columns.split(delimiter)
            
            if str(file_name).endswith(".tsv"): 
                if delimiter == "\t":  
                    if len_nums_list == 1:
                        print(columns[int(column) - 1])
                    else:
                        for i in range(len_nums_list):
                            print(columns[int(nums_list[i])-1], end=', ')
                        print(end='\n')
                else:
                    print(stripped_columns)

            
            elif str(file_name).endswith(".csv"):
                # if this delimiter == ,
                if delimiter == ",":
                    if len_nums_list == 1:
                        print(columns[int(column) - 1])
                    else:
                        for i in range(len_nums_list):
                            print(columns[int(nums_list[i])-1], end=', ')
                        print(end='\n')
                else:
                    print(stripped_columns)
            else:
                print(stripped_columns)

    # except (IndexError, BrokenPipeError):
    #     print()


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
