def convert_to_flat_str(source: str) -> str:
    buffer = ''
    currentstr = ''
    count_open_break = 0
    count_close_break = 0
    multiplicator = 1
    idx = 0
    for item in source:
        if item.isdigit():
            multiplicator = int(item)
        elif item == '[':
            if count_open_break:
                sub_str, multiply = get_str_and_multiply(source[idx-1:])
                buffer += sub_str * multiply
                currentstr += buffer
                buffer = ''
                count_open_break = 0
            else:
                count_open_break += 1
        elif item == ']':
            count_close_break += 1
            if count_open_break:
                currentstr += buffer * multiplicator
                buffer = ''
        else:
            buffer += item
        idx += 1

    return currentstr


def get_str_and_multiply(source: str):
    currentstr = ''
    multiplicator = 1
    for item in source:
        if item.isdigit():
            multiplicator = int(item)
        elif item == '[':
            ...
        elif item == ']':
            break
        else:
            currentstr += item

    return currentstr, multiplicator