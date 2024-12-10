import pyperclip

def intify(item):
    if type(item) is str:
        try:
            return int(item)
        except ValueError:
            return item
    elif type(item) is list:
        return [intify(x) for x in item]
    elif type(item) is set:
        return {intify(x) for x in item}
    elif type(item) is tuple:
        return tuple([intify(x) for x in item])
    elif type(item) is dict:
        return {intify(k): intify(v) for k, v in item.items()}
    return item

    
def copy_result(result) -> None:
    pyperclip.copy(result)
    print(result)
