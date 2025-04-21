from collections import defaultdict

from utils.parse_log_file import parse_log_line
from preferences.log_level import LogLevel

l = LogLevel

def count_requests(log_files):
    stats = defaultdict(lambda: {
            l.INFO.value: 0,
            l.DEBUG.value: 0,
            l.WARNING.value: 0,
            l.ERROR.value: 0,
            l.CRITICAL.value: 0
        }
    )
    total = 0

    for file_path in log_files:
        with open(file_path, "r") as f:
            for line in f:
                result = parse_log_line(line)
                if result:
                    handler, level = result
                    if handler and level:
                        stats[handler][level] += 1
                        total += 1

    return stats, total
