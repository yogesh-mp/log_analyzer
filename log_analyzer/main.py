import csv
from parser import parse_log_line
from analyzer import tally_log_levels, tally_services, find_most_common_error
from filters import filter_logs_by_time
from datetime import datetime


def read_log_file(filepath):
    """Reads and parses a log file."""
    logs = []
    with open(filepath, "r") as file:
        for line in file:
            parsed = parse_log_line(line.strip())
            if parsed:
                logs.append(parsed)
    return logs


def write_summary_to_csv(summary, filepath):
    """Writes summary data to a CSV file with proper headers."""
    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Type", "Count"])
        for key, value in summary.items():
            if isinstance(value, dict):
                for sub_key, sub_value in value.items():
                    writer.writerow([key, sub_key, sub_value])
            else:
                # Handle cases where value is not a dict
                writer.writerow([key, "", value])


def main():
    """Main function to read logs, process them, and write a summary to CSV."""
    log_file = input("Enter the log file path (or press Enter to use default 'logs/sample.log'): ")
    if not log_file:
        log_file = "logs/sample.log"
    logs = read_log_file(log_file)

    # Take user input for date filtering
    start_time_str = input("Enter start time (YYYY-MM-DD HH:MM:SS) or press Enter to skip: ")
    end_time_str = input("Enter end time (YYYY-MM-DD HH:MM:SS) or press Enter to skip: ")

    if start_time_str and end_time_str:
        try:
            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS.")
            return
        logs = filter_logs_by_time(logs, start_time, end_time)

    summary = {
        "Log Levels": tally_log_levels(logs),
        "Services": tally_services(logs),
        "Most Common Error": find_most_common_error(logs)
    }

    print("Summary:")
    print(summary)

    output_file = "output/summary.csv"
    write_summary_to_csv(summary, output_file)
    print(f"Summary saved to {output_file}")


if __name__ == "__main__":
    main()
