rules_type_required = {
    "bus_id": {"type": "int", "required": True, "value": b''},
    "stop_id": {"type": "int", "required": True, "value": b''},
    "stop_name": {"type": "str", "required": True, "value": b''},
    "next_stop": {"type": "int", "required": True, "value": b''},
    "stop_type": {"type": "char", "required": False, "value": [b'S', b'O', b'F', b'']},
    "a_time": {"type": "str", "required": True, "value": b''}
}

rules_format = {
    "stop_name": "([A-Z]+\w*\s?)+(Road|Avenue|Boulevard|Street)$",
    "stop_type": "^(S|O|F){0,1}$",
    "a_time": "^([012]\d)\:([0-5]\d)$"
}
