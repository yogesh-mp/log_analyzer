from datetime import datetime


def filter_logs_by_time(logs, start_time, end_time):
    """Filters logs within a specified date-time range."""
    return [log for log in logs if start_time <= datetime.strptime(log["timestamp"], "%Y-%m-%d %H:%M:%S") <= end_time]
