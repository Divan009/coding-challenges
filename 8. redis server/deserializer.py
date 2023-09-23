def deserializer_simple_str(content):
    if (
        content.count("\r\n") == 1
        and content.endswith("\r\n")
        and content.startswith("+")
    ):
        return content[1:-2]
    else:
        return False


def deserializer_simple_err(content):
    if (
        content.count("\r\n") == 1
        and content.endswith("\r\n")
        and content.startswith("-")
    ):
        return content[1:-2]
    else:
        return False


def deserializer_integers_wo_signs(content):
    if (
        content.count("\r\n") == 1
        and content.endswith("\r\n")
        and content.startswith(":")
    ):
        return content[1:-2]
    else:
        return False


def deserializer_bulk_str(content):
    if content.startswith("$") and content.endswith("\r\n"):
        list_content = content[1:].split("\r\n")
        filtered_list = [item for item in list_content if item != ""]
        data = " ".join(filtered_list[1:])
        return None if data == 0 else data
    else:
        return False


def deserializer_array(content):
    response = []
    if content.startswith("*") and content.endswith("\r\n"):
        list_content = content[1:].split("\r\n")
        filtered_list = [item for item in list_content if item != ""]

        for item in range(1, len(filtered_list)):
            if filtered_list[item].startswith(':'):
                response.append(int(filtered_list[item][1:]))
            elif filtered_list[item].startswith('$'):
                response.append(filtered_list[item+1])
        return response
    else:
        return False
            


test = [
    "$-1\r\n",
    "*1\r\n$4\r\nping\r\n",
    "*3\r\n:1\r\n:2\r\n:3\r\n",
    "*2\r\n$4\r\necho\r\n$5\r\nhello world\r\n",
    "+OK\r\n",
    "-Error message\r\n",
    "*2\r\n$5\r\nhello\r\n$5\r\nworld\r\n",
    "*0\r\n",
    "$0\r\n\r\n",
    "+hello world\r\n"
]

for _ in test:
    if _.startswith('$'):
        op = deserializer_bulk_str(_)
    elif _.startswith('*'):
        op = deserializer_array(_)
    elif _.startswith('+'):
        op = deserializer_simple_str(_)
    elif _.startswith('-'):
        op = deserializer_simple_err(_)
    elif _.startswith(':'):
        op = deserializer_integers_wo_signs(_)   
        
    print(op)