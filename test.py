# generate_report.py
from datetime import datetime

with open("log.txt", "a") as f:
    f.write(f"Script ran at {datetime.now()}\n")
