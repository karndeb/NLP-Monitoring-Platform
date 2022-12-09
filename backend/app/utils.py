import csv

FIELD_NAMES = ["Timestamp", "Log level", "Logger", "Line Number", "File", "Request ID", "Correlation ID", "Log message"]

FIELD_DELIMITER = ' - '


def log_lines_to_json(log_file, field_names, field_delimiter):
    result = []
    with open(log_file) as f:
        lines = (line.rstrip() for line in f)
        lines = list(line for line in lines if line)
        for line in lines:
            if line.startswith('2'):
                fields = line.split(field_delimiter)
                if len(fields) == 8:
                    result.append({field_name: fields[idx] for idx, field_name in enumerate(field_names)})
    return result


def json_to_csv(data, filename):
    with open(filename, "w", newline="") as f:
        keys = data[0].keys()
        cw = csv.DictWriter(f, keys)
        cw.writeheader()
        cw.writerows(data)

