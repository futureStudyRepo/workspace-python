# 문자열 관련 함수 
print("hello".find('e')) #특정 문자열의 인덱스 찾는함수.
print("    hello    ".strip()) #양쪽 공백제거 lstrip 왼,rstrip오른 공백제거
arr = "hello world".split() # 구분자를 기준으로 문자열을 자름,()디폴트 공백
print(arr)
arr2 = "nick,jack,alice".split(',')
print(arr2)
print("hello world".replace("world", "python")) # 변경 

# 사용자에게 문장을 입력받아 줄임말을 만들어 주세요 
# 갑자기 분위기 싸함 <-- 입력
# 갑분싸            <-- 출력
# 1.입력받기
# 2.특정 기준으로 문자열 자르기
# 3.자른 문자 만큼 반복하며 첫글자 더하기
# 4.출력
abc = ""
abc+="a"
abc+="b"
abc+="c"
print(abc)

