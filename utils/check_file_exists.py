import os


def check_files_exist(file_paths):
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"Ошибка: файл {file_path} не найден!")
            exit(1)
