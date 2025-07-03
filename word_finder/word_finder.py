
import os

start_path = os.getcwd()

files_visited = set()

SPECIFIC_WORD = 'help'

def search_word_in_file(curr_path, file):
    with open(curr_path) as f:
        lines = f.readlines()
        for row in lines:
            word = SPECIFIC_WORD
            if row.find(word) != -1:
                print(f"didnt find anything in file {file}")
                return


def walk_folder():
    for root, dirs, files in os.walk(start_path):
        print(dirs)
        for file in files:
            print(file)
            file_path = os.path.join(root, file)
            search_word_in_file(file_path, file)

if __name__ == '__main__':
    walk_folder()     
