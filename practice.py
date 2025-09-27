

# quiz) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 옾라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.
# 1 : 랜덤으로 날짜를 뽑아야 함
# 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함
# 3. 매월 1~3일은 스터디 준비를 해야 하므로 제외 
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월"+ str(date) + "일로 선정되었습니다.")
print(not 5>6)

print('---')

print((3>0) & (3<1))

print('---')

print(abs(-5)) #5

print(pow(4, 2)) #4^2

print(round(3.14))

print(round(4.99))

from math import *

print(floor(4.99))

print(ceil(3.14))

print(sqrt(16))


sentence = """
i am a boy"""

print(sentence)