# 업다운 게임
# 1 ~ 10 사이의 숫자를 맞춰보세요! 총 기회는 3번 있습니다.
# 1.1 ~ 10사이의 정수를 랜덤하게 생성 
# 2.3번의 맞출 기회를 줌
# 3.사용자 입력이 들어올때마다 맞으면 '정답', 작으면 업, 크면 다운을 출력
# 틀릴때 마다 몇번의 기회가 남았는지 출력.
import random
print("="*20)
print(" *업다운 게임* ")
ran_num = random.randint(1, 10)
cnt = 3 
while cnt > 0:
    user_num = int(input("1 ~ 10 사이의 정수를 입력하세요:"))
    # 업다운 조건문
    if user_num < ran_num:
        print("업")
    elif user_num > ran_num:
        print("다운")
    else:
        print("정답입니다!")
        break
    cnt -=1 
    print(f"남은 기회 :{cnt}")
if cnt == 0:
    print(f"기회를 모두 사용하셨습니다.... 정답은 {ran_num}")


