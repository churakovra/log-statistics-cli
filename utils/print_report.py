from preferences.log_level import LogLevel

l = LogLevel

def print_report(stats, total):
    print(f"Total requests: {total}\n")

    print("{:<25} {:<8} {:<8} {:<8} {:<8} {:<8}".format(
        "HANDLER", l.DEBUG.value, l.INFO.value, l.WARNING.value, l.ERROR.value, l.CRITICAL.value
        )
    )

    for handler in sorted(stats.keys()):
        counts = stats[handler]
        print("{:<25} {:<8} {:<8} {:<8} {:<8} {:<8}".format(
            handler,
            counts.get(l.DEBUG.value, 0),
            counts.get(l.INFO.value, 0),
            counts.get(l.WARNING.value, 0),
            counts.get(l.ERROR.value, 0),
            counts.get(l.CRITICAL.value, 0)
            )
        )

    totals = {l.DEBUG.value: 0, l.INFO.value: 0, l.WARNING.value: 0, l.ERROR.value: 0, l.CRITICAL.value: 0}
    for handler_counts in stats.values():
        for level, count in handler_counts.items():
            totals[level] += count

    print("{:<25} {:<8} {:<8} {:<8} {:<8} {:<8}".format(
        "TOTAL",
        totals.get(l.DEBUG.value, 0),
        totals.get(l.INFO.value, 0),
        totals.get(l.WARNING.value, 0),
        totals.get(l.ERROR.value, 0),
        totals.get(l.CRITICAL.value, 0)
        )
    )
