import json
from helpers import check_format as check
from helpers import output_print
from outpyt import output_format as output_
from rules import rules_format as rules

data = json.loads(input())
output = output_

for block in data:
    check(block, rules, output)

output_print(output, variant=2)
