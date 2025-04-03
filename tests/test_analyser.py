import unittest
import os
import sys
# Adjust the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from log_analyzer.analyzer import tally_log_levels, tally_services, find_most_common_error


class TestAnalyzer(unittest.TestCase):
    """
    Unit tests for the log analyzer functions.
    """
    def test_tally_log_levels(self):
        """Test the tally_log_levels function."""
        logs = [{"log_level": "INFO"}, {"log_level": "ERROR"}, {"log_level": "WARN"}]
        self.assertEqual(tally_log_levels(logs), {"INFO": 1, "ERROR": 1, "WARN": 1})

    def test_tally_services(self):
        """Test the tally_services function."""
        logs = [{"service_name": "ServiceA"}, {"service_name": "ServiceB"}]
        self.assertEqual(tally_services(logs), {"ServiceA": 1, "ServiceB": 1})

    def test_find_most_common_error(self):
        """Test the find_most_common_error function."""
        logs = [{"log_level": "ERROR", "message": "Null pointer exception"},
                {"log_level": "ERROR", "message": "Null pointer exception"}]
        self.assertEqual(find_most_common_error(logs), {"Null pointer exception": 2})

    def test_find_most_common_error_no_errors(self):
        """Test the find_most_common_error function when there are no ERROR logs."""
        logs = [{"log_level": "INFO", "message": "All good"}]
        self.assertEqual(find_most_common_error(logs), {None: 0})

    def test_find_most_common_error_empty_logs(self):
        """Test the find_most_common_error function with empty logs."""
        logs = []
        self.assertEqual(find_most_common_error(logs), {None: 0})

    def test_tally_log_levels_empty(self):
        """Test the tally_log_levels function with empty logs."""
        logs = []
        self.assertEqual(tally_log_levels(logs), {})

    def test_tally_services_empty(self):
        """Test the tally_services function with empty logs."""
        logs = []
        self.assertEqual(tally_services(logs), {})


if __name__ == "__main__":
    unittest.main()
