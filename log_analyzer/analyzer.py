def tally_log_levels(logs):
    """Counts occurrences of each log level."""
    log_counts = {}
    for log in logs:
        if "log_level" in log:
            log_counts[log["log_level"]] = log_counts.get(log["log_level"], 0) + 1

    return log_counts


def tally_services(logs):
    """Counts occurrences of each service."""
    service_counts = {}
    for log in logs:
        if "service_name" in log:
            service_counts[log["service_name"]] = service_counts.get(log["service_name"], 0) + 1

    return service_counts


def find_most_common_error(logs):
    """Finds the most common error message."""
    error_counts = {}
    for log in logs:
        if log.get("log_level") == "ERROR":
            error_counts[log["message"]] = error_counts.get(log["message"], 0) + 1

    if not error_counts:
        return {None: 0}

    # Find the maximum count and filter messages with that count
    max_count = max(error_counts.values())

    # Create a dictionary of messages with the maximum count
    most_common_messages = {msg: count for msg, count in error_counts.items() if count == max_count}

    return most_common_messages
