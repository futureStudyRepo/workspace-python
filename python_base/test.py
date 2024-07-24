import json
import os
root = os.getcwd()
print(root + "/python_base/")
# JSON 파일 읽기
file_path =root + "/python_base/"+ 'grades.json'

with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 과목별 점수를 저장할 딕셔너리
scores = {}

# 학생들의 성적을 과목별로 분류
for student in data['students']:
    for subject, score in student['scores'].items():
        if subject not in scores:
            scores[subject] = []
        scores[subject].append(score)

# 과목별 평균 계산 및 출력
print("과목별 평균 성적:")
for subject, score_list in scores.items():
    average = sum(score_list) / len(score_list)
    print(f"{subject}: {average:.2f}")
