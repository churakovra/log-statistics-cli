from typing import Optional, Tuple

from preferences.log_level import LogLevel
from preferences.http_methods import HttpMethods

l = LogLevel
h = HttpMethods


def parse_log_line(line: str) -> Tuple[Optional[str], Optional[str]]:
    if "django.request" not in line:
        return None, None

    level = None
    for log_level in l.levels.value:
        if f" {log_level} " in line:
            level = log_level
            break

    handler = None

    for method in h.methods.value:
        method_with_space = f"{method} "
        if method_with_space in line:
            index = line.find(method_with_space)
            after_method = line[index + len(method_with_space):]
            handler = after_method.split()[0]
            if '?' in handler:
                handler = handler.split('?')[0]
            break

    if handler is None and "Internal Server Error:" in line:
        index = line.find("Internal Server Error:")
        after_error = line[index + len("Internal Server Error:"):].strip()
        if after_error:
            handler = after_error.split()[0]
            if '?' in handler:
                handler = handler.split('?')[0]

    return handler, level
