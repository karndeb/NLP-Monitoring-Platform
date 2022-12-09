from utils import *

entries = log_lines_to_json('../../sample-data/dts-logs.log', FIELD_NAMES, FIELD_DELIMITER)
output = json_to_csv(entries, "data/dts-logs.csv")
