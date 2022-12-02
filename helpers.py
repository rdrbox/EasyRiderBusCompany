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


def stops_list(data):
    result = set((block.get("stop_id"), block.get("stop_name")) for block in data)
    return {item[0]: item[1] for item in result}


def get_unique_id(data):
    id_list = [block["bus_id"] for block in data]
    return set(id_list)


def stop_id_list(data, bus_id):
    return [block["stop_id"] for block in data if block["bus_id"] == bus_id]


def stop_type_list(data, bus_id):
    return [block["stop_type"] for block in data if block["bus_id"] == bus_id]


def check_line_names_number(data):
    result = []
    bus_id_list = get_unique_id(data)
    for bus_id in bus_id_list:
        stop_id = set(stop_id_list(data, bus_id))
        result.append({"bus_id": bus_id, "stops": len(stop_id)})

    return result, 3


def check_one_start_stop(stop_type_list_):
    if all([stop_type_list_.count("S") == 1, stop_type_list_.count("F") == 1]):
        return True
    return False


def start_stop_name(data):
    start_name = []
    stop_name = []
    for block in data:
        if block.get("stop_type") == "S":
            start_name.append(block.get("stop_name"))

        elif block.get("stop_type") == "F":
            stop_name.append(block.get("stop_name"))

    return set(start_name), set(stop_name)


def transfer_stops(stop_id_all):
    transfer_stops_id = set()
    for i in range(len(stop_id_all) - 1):
        for k in range(i + 1, len(stop_id_all)):
            new_id = (set(stop_id_all[i])).intersection(set(stop_id_all[k]))
            if len(new_id):
                transfer_stops_id.update(new_id)

    return transfer_stops_id


def transfer_name(transfer_stops_id, data):
    stops_list_ = stops_list(data)
    return [stops_list_.get(stops_id) for stops_id in transfer_stops_id]


def special_stops(data):
    bus_id_list = get_unique_id(data)
    stop_id_all = []
    for bus_id in bus_id_list:
        stop_type_list_ = stop_type_list(data, bus_id)

        if check_one_start_stop(stop_type_list_):
            el = stop_id_list(data, bus_id)
            stop_id_all.append(el)

        else:
            return {}, 4, bus_id

    transfer = transfer_name(transfer_stops(stop_id_all), data)
    start, stop = start_stop_name(data)
    return [sorted(start), sorted(transfer), sorted(stop)], 5, None


def output_print(output, variant, bus_id):
    message = {
        1: "Type and required field validation",
        2: "Format validation",
        3: "Line names and number of stops",
        4: "There is no start or end stop for the line",
        5: ["Start stops", "Transfer stops", "Finish stops"],
        6: "Arrival time test"
    }

    if variant == 3:
        print(f"{message[variant]}:")
        for item in output:
            print(",".join([f"{key}: {val}" for key, val in item.items()]))

    elif variant == 4:
        print(f"{message[variant]}: {bus_id}.")

    elif variant == 5:
        for item in zip(message[variant], output):
            print(f"{item[0]}: {len(item[1])} {item[1]}")

    elif variant == 6:
        print(f"{message[variant]}:")

    else:
        print(f"{message[variant]}: {count_errors(output)} errors")
        for key, val in output.items():
            print(f"{key}: {val}")
