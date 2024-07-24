# 조건문 if 는 조건에 따라 코드 블록을 실행하거나 실행하지 않도록 제어함.
# 주의사항(들여쓰기, 조건식의 순서, None, [], 0 은 False인식)
# num = int(input("숫자를 입력하세요:"))
# if num > 5 :
#     print("입력은 5보다 큼")
# elif num > 7 :
#     print("이부분은 실행되지 않음")
# elif num == 3:
#     print("3이군요!")
# else:
#     pass  # 아무 작업을 하지않을때 
print("종료")

# 중첩 if  (if문안에 if문)
# 영화관람 체크
# 조건1 : 18세 이상관람가 
# 조건2 : 신분증이 있어야함 (있으면 :y, 없으면 n)
# upper()대문자로, lower()소문자로 
print('LAG'.lower())
age = int(input("나이를 입력하세요:"))
has_id = input("신분증을 가지고 있습니까?(y/n):").lower()
if age >= 18:
    if has_id == 'y':
        print("영화 관람이 가능합니다.")
    else:
        print("신분증이 없으면 불가능합니다.......")
else:
    print("미성년자는 안됩니다...")

