import unittest
from datetime import datetime
import os
import sys
# Adjust the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer.filters import filter_logs_by_time


class TestFilters(unittest.TestCase):
    """
    Unit tests for the log filtering functions.
    """
    def test_filter_logs_by_time(self):
        """Test the filter_logs_by_time function."""
        logs = [
            {"timestamp": "2023-03-01 08:10:00"},
            {"timestamp": "2023-03-01 08:20:00"}
        ]
        start = datetime.strptime("2023-03-01 08:15:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime("2023-03-01 08:25:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(len(filter_logs_by_time(logs, start, end)), 1)

    def test_filter_logs_by_time_empty(self):
        """Test the filter_logs_by_time function with empty logs."""
        logs = []
        start = datetime.strptime("2023-03-01 08:15:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime("2023-03-01 08:25:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(filter_logs_by_time(logs, start, end), [])

    def test_filter_logs_by_time_no_match(self):
        """Test the filter_logs_by_time function with no matching logs."""
        logs = [
            {"timestamp": "2023-03-01 08:10:00"},
            {"timestamp": "2023-03-01 08:20:00"}
        ]
        start = datetime.strptime("2023-03-01 09:15:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime("2023-03-01 09:25:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(filter_logs_by_time(logs, start, end), [])

    def test_filter_logs_by_time_all_match(self):
        """Test the filter_logs_by_time function with all logs matching."""
        logs = [
            {"timestamp": "2023-03-01 08:10:00"},
            {"timestamp": "2023-03-01 08:20:00"}
        ]
        start = datetime.strptime("2023-03-01 08:05:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime("2023-03-01 08:25:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(len(filter_logs_by_time(logs, start, end)), 2)

    def test_filter_logs_by_time_same_time(self):
        """Test the filter_logs_by_time function with start and end time being the same."""
        logs = [
            {"timestamp": "2023-03-01 08:10:00"},
            {"timestamp": "2023-03-01 08:20:00"}
        ]
        start = datetime.strptime("2023-03-01 08:20:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime("2023-03-01 08:20:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(len(filter_logs_by_time(logs, start, end)), 1)

    def test_filter_logs_by_time_edge_case(self):
        """Test the filter_logs_by_time function with edge case of start and end time being the same."""
        logs = [
            {"timestamp": "2023-03-01 08:10:00"},
            {"timestamp": "2023-03-01 08:20:00"}
        ]
        start = datetime.strptime("2023-03-01 08:10:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime("2023-03-01 08:20:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(len(filter_logs_by_time(logs, start, end)), 2)

    def test_filter_logs_by_time_nonexistent_time(self):
        """Test the filter_logs_by_time function with nonexistent time."""
        logs = [
            {"timestamp": "2023-03-01 08:10:00"},
            {"timestamp": "2023-03-01 08:20:00"}
        ]
        start = datetime.strptime("2023-03-01 09:15:00", "%Y-%m-%d %H:%M:%S")
        end = datetime.strptime("2023-03-01 09:25:00", "%Y-%m-%d %H:%M:%S")
        self.assertEqual(filter_logs_by_time(logs, start, end), [])


if __name__ == "__main__":
    unittest.main()
