import re


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
    for out_key in list(output):
        if re.match(rules.get(out_key), block.get(out_key)) is None:
            output[out_key] += 1


def count_errors(output):
    return sum(output.values())


def get_unique_id(data):
    id_list = [block["bus_id"] for block in data]
    return set(id_list)


def stop_id_set(data, bus_id):
    return set([block["stop_id"] for block in data if block["bus_id"] == bus_id])


def check_line_names_number(data):
    result = []
    bus_id_list = get_unique_id(data)
    for bus_id in bus_id_list:
        stop_id = stop_id_set(data, bus_id)
        result.append({"bus_id": bus_id, "stops": len(stop_id)})

    return result


def output_print(output, variant):
    message = {
        1: "Type and required field validation",
        2: "Format validation",
        3: "Line names and number of stops"
    }

    if variant == 3:
        print(f"{message[variant]}:")
        for item in output:
            print(",".join([f"{key}: {val}" for key, val in item.items()]))

    else:
        print(f"{message[variant]}: {count_errors(output)} errors")
        for key, val in output.items():
            print(f"{key}: {val}")
