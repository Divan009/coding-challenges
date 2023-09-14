from pathlib import Path
import argparse

def check_syntax_json(file):
    try:
        file = Path(file)
        # if file.exists:
        with open(file) as f:
            char = f.read()
            try:
                if char[0] == "{" and char[-1]== "}":
                    return "Valid Json file"
            except IndexError:
                return "Invalid Json file"     
    except Exception as e:
        return f"File {str(file).split('/')[-1]} does not exist."
    

if __name__ == '__main__':
    msg = "This validates JSON file"
    parser = argparse.ArgumentParser(description=msg)

    # Adding optional arguments    
    parser.add_argument("file_name", nargs='?', default=None, help="the file to analyze")
    # Read arg from command lineon
    args = parser.parse_args()

    print(check_syntax_json(args.file_name))
