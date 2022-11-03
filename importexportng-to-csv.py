"""Convert a CSV from ImportExportNG into better CSV

Usage: python importexportng-to-csv.py <in.csv> <out.csv>
"""

import sys
from email.utils import parseaddr
import pandas as pd

input_file = pd.read_csv(
    sys.argv[1], header=None, names=["subject", "from", "to", "date", "extra", "extra2"]
)
new_data = {
    "first_name": [],
    "last_name": [],
    "email": [],
}

for (name, email) in input_file["from"].map(parseaddr).values:
    if email == "info@cambridgebikesafety.org":
        continue
    parts = name.strip().split()
    if parts:
        first_name = parts[0]
        last_name = " ".join(parts[1:])
    else:
        first_name = ""
        last_name = ""
    new_data["first_name"].append(first_name)
    new_data["last_name"].append(last_name)
    new_data["email"].append(email)

output_file = pd.DataFrame(new_data)
output_file.to_csv(sys.argv[2])
