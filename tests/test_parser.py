import unittest
import os
import sys
# Adjust the path to include the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from log_analyzer.parser import parse_log_line


class TestParser(unittest.TestCase):
    """
    Unit tests for the log parser functions.
    """
    def test_parse_valid_log_line(self):
        """Test the parse_log_line function with a valid log line."""
        line = "2023-03-01 08:15:27 - ServiceA - INFO - Started processing request #123"
        expected = {
            "timestamp": "2023-03-01 08:15:27",
            "service_name": "ServiceA",
            "log_level": "INFO",
            "message": "Started processing request #123"
        }
        self.assertEqual(parse_log_line(line), expected)

    def test_parse_invalid_log_line(self):
        """Test the parse_log_line function with an invalid log line."""
        line = "Malformed log entry without proper format"
        self.assertIsNone(parse_log_line(line))

    def test_parse_empty_log_line(self):
        """Test the parse_log_line function with an empty log line."""
        line = ""
        self.assertIsNone(parse_log_line(line))

    def test_parse_log_line_with_extra_spaces(self):
        """Test the parse_log_line function with extra spaces."""
        line = "   2023-03-01 08:15:27 - ServiceA - INFO - Started processing request #123   "
        expected = {
            "timestamp": "2023-03-01 08:15:27",
            "service_name": "ServiceA",
            "log_level": "INFO",
            "message": "Started processing request #123"
        }
        self.assertEqual(parse_log_line(line.strip()), expected)

    def test_parse_log_line_with_special_characters(self):
        """Test the parse_log_line function with special characters."""
        line = "2023-03-01 08:15:27 - ServiceA - ERROR - Null pointer exception at line 42"
        expected = {
            "timestamp": "2023-03-01 08:15:27",
            "service_name": "ServiceA",
            "log_level": "ERROR",
            "message": "Null pointer exception at line 42"
        }
        self.assertEqual(parse_log_line(line), expected)

    def test_parse_log_line_with_unicode(self):
        """Test the parse_log_line function with unicode characters."""
        line = "2023-03-01 08:15:27 - ServiceA - INFO - Processing request with ID #1234 🚀"
        expected = {
            "timestamp": "2023-03-01 08:15:27",
            "service_name": "ServiceA",
            "log_level": "INFO",
            "message": "Processing request with ID #1234 🚀"
        }
        self.assertEqual(parse_log_line(line), expected)

    def test_parse_log_line_with_invalid_timestamp(self):
        """Test the parse_log_line function with an invalid timestamp."""
        line = "2023-03-01 25:15:27 - ServiceA - INFO - Invalid timestamp"
        expected = {
            "timestamp": "2023-03-01 25:15:27",
            "service_name": "ServiceA",
            "log_level": "INFO",
            "message": "Invalid timestamp"
        }
        self.assertEqual(parse_log_line(line), expected)


if __name__ == "__main__":
    unittest.main()
