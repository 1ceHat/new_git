import os
import time

current_dir = os.getcwd()
for root, dirs, files in os.walk(current_dir):
    if '.git' in root or '.idea' in root or '__' in root:
        continue
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file)
        file_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f"Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size}, "
              f"Время изменения: {file_time}, Родительская директория: {parent_dir}")
