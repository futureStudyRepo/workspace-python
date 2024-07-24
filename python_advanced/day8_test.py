import os
import csv

# CSV 파일 경로
csv_file_path = './python_advanced/github_202407.csv'

# CSV 파일 읽기
with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # 헤더 건너뛰기
    names_initials = [(row[0], row[1].lower()) for row in reader]

# 폴더 생성
for name, initial in names_initials:
    os.makedirs(initial, exist_ok=True)
    print(f"Folder '{initial}' created for {name}")

print("All folders created successfully.")
