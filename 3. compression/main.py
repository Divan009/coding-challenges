from collections import defaultdict


def frequency_counter(file):
    char_count = defaultdict(int)
    with open(file) as f:
        while True:
            char = f.read(1)

            if not char:
                break

            if char == " ":
                continue

            else:
                char_count[char] += 1

        return char_count


if __name__ == "__main__":
    import argparse
    from pathlib import Path
    import sys

    msg = "This is a compressor"
    parser = argparse.ArgumentParser(description=msg)

    parser.add_argument("file_name")

    args = parser.parse_args()

    file = Path(args.file_name)

    if not file.exists():
        print(f"File: {file} doesn't exist.")
        sys.exit()

    print(frequency_counter(file))
