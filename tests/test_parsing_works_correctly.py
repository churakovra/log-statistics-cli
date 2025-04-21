from utils.parse_log_file import parse_log_line


def test_parse_log_line():
    line1 = "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]"
    assert parse_log_line(line1) == ("/api/v1/reviews/", "INFO")

    line2 = "2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data"
    assert parse_log_line(line2) == ("/admin/dashboard/", "ERROR")
