import argparse

from utils.check_file_exists import check_files_exist
from utils.count_requests import count_requests
from utils.print_report import print_report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("log_files", nargs="+", help="Файлы логов для анализа")
    parser.add_argument("--report", required=True, help="Тип отчета")
    args = parser.parse_args()

    if args.report != "handlers":
        print("Ошибка: поддерживается только отчет 'handlers'")
        exit(1)

    check_files_exist(args.log_files)
    stats, total = count_requests(args.log_files)
    print_report(stats, total)


if __name__ == "__main__":
    main()
