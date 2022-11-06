import json

rules = {
    "bus_id": {"type": "int", "required": True, "value": b''},
    "stop_id": {"type": "int", "required": True, "value": b''},
    "stop_name": {"type": "str", "required": True, "value": b''},
    "next_stop": {"type": "int", "required": True, "value": b''},
    "stop_type": {"type": "char", "required": False, "value": [b'S', b'O', b'F', b'']},
    "a_time": {"type": "str", "required": True, "value": b''}
}

output = {
    "bus_id": 0,
    "stop_id": 0,
    "stop_name": 0,
    "next_stop": 0,
    "stop_type": 0,
    "a_time": 0
}


def check_type(el):
    if isinstance(el, int):
        return "int"
    elif isinstance(el, str):
        return "str"


def check_rules(block_, rules_):
    for key, value in block_.items():
        if rules_[key]["required"]:
            this_type = rules_[key]["type"]
            this_value = rules_[key]["value"]
            if any([check_type(value) != this_type, (str(value)).encode() == this_value]):
                output[key] += 1
        else:
            if str(value).encode() not in rules_[key]["value"]:
                output[key] += 1


def count_errors(out_):
    return sum(out_.values())


def output_print():
    print(f"Type and required field validation: {count_errors(output)} errors")
    for key, val in output.items():
        print(f"{key}: {val}")


data = json.loads(input())

for block in data:
    check_rules(block, rules)

output_print()
