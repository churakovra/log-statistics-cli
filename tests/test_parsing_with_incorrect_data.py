from utils.parse_log_file import parse_log_line


def test_parse_log_line():
    # Строка, не относящаяся к django.request
    line1 = "2025-03-28 12:07:23,000 CRITICAL django.core.management: ConnectionError: Failed to connect to payment gateway"
    assert parse_log_line(line1) == (None, None)
