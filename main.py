from datetime import datetime

from core import Extract, Load, Transform


# Extract TRs
trs = Extract.get_trs()

# Transform to CSV row
now = datetime.now()
rows = [Transform.convert_tr_to_row(now, tr) for tr in trs]

# Load data in the CSV
Load.add_rows_to_csv(rows)
