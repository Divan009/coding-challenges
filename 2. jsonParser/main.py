from pathlib import Path
import argparse
import sys
import json
import os


def step_1(char):
    try:
        if char[0] == "{" and char[-1] == "}":
            return 0
    except IndexError:
        return 1


def validates_json_obj(char):
    try:
        parsed_json = json.loads(char)

        if isinstance(parsed_json, dict):
            for key, val in parsed_json.items():
                if not (
                    isinstance(key, str)
                    and (
                        isinstance(val, str)
                        or isinstance(val, int)
                        or isinstance(val, bool)
                        or val is None
                        or isinstance(val, list)
                        or isinstance(val, dict)
                    )
                ):
                    return 1
            return 0
    except json.JSONDecodeError:
        return 1


def check_syntax_json(file):
    with open(file) as f:
        char = f.read()
        char = char.strip()

        value = 0
        while value == 0:
            value = step_1(char)
            if value != 0:
                return "Invalid JSON file"

            value = validates_json_obj(char)
            if value != 0:
                return "Invalid JSON file"

            return "Valid JSON file"


if __name__ == "__main__":
    msg = "This validates JSON file"
    parser = argparse.ArgumentParser(description=msg)

    # Adding optional arguments
    parser.add_argument(
        "file_name", nargs="?", default=None, help="the file to analyze"
    )
    # Read arg from command lineon
    args = parser.parse_args()

    file = Path(args.file_name)
    if not file.exists():
        print(f"File {str(file).split('/')[-1]} does not exist.")
        sys.exit()

    print(check_syntax_json(file))

    # TODO: if you want to test json_test_suites
    # for path, dir, file_list in os.walk('json_test_suites'):
    #     for file_name in file_list:

    #         print(check_syntax_json(f"{path}/{file_name}"))
