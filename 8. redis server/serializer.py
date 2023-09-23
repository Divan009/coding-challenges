import ast


def serialize_array(content):
    content_len = len(content)
    response = [f'*{content_len}']
    print(content)
    
    for item in range(content_len):
        try:
            if content[item].isdigit() :
                item = int(content[item])
                response.append(f"\\r\\n:{item}")
            else:
                op = f"${len(content[item])}\\r\\n{content[item]}"
                response.append(op)
        except AttributeError as e:
            if isinstance(content[item], int):
                response.append(f"\\r\\n:{content[item]}")
            
    op = "\\r\\n"
    response.append(op)
    return ''.join(response)


def is_valid_list(s):
    try:
        parsed_value = ast.literal_eval(s)
        if isinstance(parsed_value, (list, str)):
            print("^^^")
            if isinstance(parsed_value, list):
                response = serialize_array(parsed_value)
                return response
            elif isinstance(parsed_value, str):
                return "STRR"
    except (SyntaxError, ValueError):
        return False
    

x = "['ping', 1, 2]"
x = "['1','2','3']"
x = '[1,2,3]'
x = ''
print(is_valid_list(x))


