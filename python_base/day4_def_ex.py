import random
def make_lotto():
    user_lotto = set()
    while len(user_lotto) < 6:
        number = random.randint(1, 45)
        user_lotto.add(number)
    return user_lotto
# 로또를 생성후 리턴하는 함수를 작성하시오 
# 함수명 make_lotto
# 매개변수 없음
# 리턴 set자료 형태 (로또 번호)
my_lotto = make_lotto() 
print(my_lotto) 
