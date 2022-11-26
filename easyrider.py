import json
from helpers import check_line_names_number as check
from helpers import output_print
# from outpyt import output_line_number_stops as output
# from rules import rules_format as rules

data = json.loads(input())

# for block in data:
#     check(block, rules=None, output=None)

output = check(data)

output_print(output, variant=3)
