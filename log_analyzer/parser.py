import re


def parse_log_line(line):
    """Parses a log line into its components."""
    pattern = (r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - (?P<service_name>[\w]+) - (?P<log_level>[A-Z]+)"
               r" - (?P<message>.+)")

    invalid_logs = []
    if match := re.match(pattern, line):
        return {
            "timestamp": match.group("timestamp"),
            "service_name": match.group("service_name"),
            "log_level": match.group("log_level"),
            "message": match.group("message")
        }
    else:
        # Handle the case where the log line does not match the expected format
        print(f"Warning: Log line does not match expected format: {line}")
        invalid_logs.append(line)
    if invalid_logs:
        # Write invalid logs to a separate file for review
        with open("output/invalid_logs.txt", "a") as file:
            for invalid_log in invalid_logs:
                file.write(invalid_log + "\n")
    return None
