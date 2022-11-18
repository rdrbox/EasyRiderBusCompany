def check_type(el):
    if isinstance(el, int):
        return "int"
    elif isinstance(el, str):
        return "str"


def check_type_required(block, rules, output):
    for key, value in block.items():
        if rules[key]["required"]:
            this_type = rules[key]["type"]
            this_value = rules[key]["value"]
            if any([check_type(value) != this_type, (str(value)).encode() == this_value]):
                output[key] += 1
        else:
            if str(value).encode() not in rules[key]["value"]:
                output[key] += 1


def check_format(block, rules, output):
    pass


def count_errors(output):
    return sum(output.values())


def output_print(output, variant):
    message = {
        1: "Type and required field validation",
        2: "Format validation"
    }
    print(f"{message[variant]}: {count_errors(output)} errors")
    for key, val in output.items():
        print(f"{key}: {val}")
