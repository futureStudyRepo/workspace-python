# 사용자로 부터 주민등록번호를 입력 받아 
# 여자일 경우 대상자 입니다. 출력
# 아닐경우 대상자가 아닙니다.를 출력하시오. 뒷자리 1,3은 남자 2,4는 여자
id_num = input("주민등록번호를 입력하세요(예:20001202-3)")
# 1.문자열 인덱스를 이용하여 마지막자리 가져오기.
# 2.조건문(if)을 이용하여 출력
gender_code = int(id_num[-1])
# if gender_code == 2 or gender_code == 4:
#     print("대상자 입니다.")
# else:
#     print("대상자가 아닙니다.")
if gender_code % 2 == 0:
    print("대상자 입니다.")
else: 
    print("대상자가 아닙니다.")


