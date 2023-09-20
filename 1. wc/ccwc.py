import argparse
from pathlib import Path
import sys


def count_bytes(file):
    try:
        file = Path(file)
        if file.exists():
            file_size = file.stat().st_size
            return f"{file_size} {file}"
        else:
            return f"{file}: No such file or directory"
    except Exception as e:
        return f"Failed because of {e}"


def count_lines(file):
    try:
        file = Path(file)
        if file.exists:
            # maybe can make it better using generator
            with open(file) as f:
                return f"{len(f.readlines())} {file}"
        else:
            return f"{file}: No such file or directory"
    except Exception as e:
        return f"Failed because of {e}"


def count_words(file):
    try:
        file = Path(file)
        if file.exists:
            # maybe can make it better using generator
            with open(file) as f:
                word_list = f.read().split()
                return f"{len(word_list)} {file}"
        else:
            return f"{file}: No such file or directory"
    except Exception as e:
        return f"Failed because of {e}"


def count_chars(file):
    try:
        file = Path(file)
        if file.exists:
            # maybe can make it better using generator
            with open(file) as f:
                word_list = f.read().split()
                total_characters = sum(len(word) for word in word_list)
                return f"{total_characters} {file}"
        else:
            return f"{file}: No such file or directory"
    except Exception as e:
        return f"Failed because of {e}"


def main():
    msg = "This is a copy of wc"
    parser = argparse.ArgumentParser(description=msg)

    # Adding optional arguments
    parser.add_argument(
        "-c", "--bytes", action="store_true", help="print the byte counts"
    )
    parser.add_argument(
        "-l",
        "--lines",
        action="store_true",
        default=None,
        help="print the number of lines",
    )
    parser.add_argument(
        "-w", "--words", action="store_true", help="print the number of words"
    )
    parser.add_argument(
        "-m", "--chars", action="store_true", help="print the character counts"
    )
    parser.add_argument("filename", nargs="?", default=None, help="the file to analyze")
    # Read arg from command lineon
    args = parser.parse_args()

    print(args)

    if args.filename:
        # python3 ccwc.py -c test.txt
        if args.bytes:
            print(count_bytes(args.filename))

        if args.lines:
            print(count_lines(args.filename))

        if args.words:
            print(count_words(args.filename))

        if args.chars:
            print(count_chars(args.filename))

        # python3 ccwc.py test.txt
        if not (args.bytes or args.lines or args.words or args.chars):
            file_size = count_bytes(args.filename)
            file_line = count_lines(args.filename)
            file_word = count_words(args.filename)
            print("^^^^^^^^")
            print(file_size, file_line, file_word)

    elif args.filename is None:
        # print(sys.stdin.name)
        if args.lines:
            line_count = sum(1 for _ in sys.stdin)
            print(line_count)
        elif args.words:
            word_count = sum(len(line.split()) for line in sys.stdin)
            print(word_count)
        elif args.bytes:
            byte_count = len(sys.stdin.read())
            print(byte_count)
        elif args.chars:
            char_count = len(sys.stdin.read().encode("utf-8"))
            print(char_count)
        elif not (args.bytes or args.lines or args.words or args.chars):
            line_count = sum(1 for _ in sys.stdin)
            word_count = sum(len(line.split()) for line in sys.stdin)
            byte_count = len(sys.stdin.read())

            print(f"{byte_count} {line_count} {word_count} ")


if __name__ == "__main__":
    main()
