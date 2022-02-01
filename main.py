from datetime import datetime
import logging
from time import sleep

from core import Extract, Load, Transform

logging.basicConfig(
    format='%(asctime)s - %(levelname)s | %(message)s',
    encoding='utf-8',
    level=logging.DEBUG,
)

while True:
    # Extract TRs
    trs = Extract.get_trs()

    # Transform to CSV row
    now = datetime.now()
    rows = [Transform.convert_tr_to_row(now, tr) for tr in trs]

    # Load data in the CSV
    Load.add_rows_to_csv(rows)
    logging.info('New lines: {}'.format(len(rows)))

    # Sleep until next minute
    sleeptime = (60 - datetime.utcnow().second) + 1
    sleep(sleeptime)
