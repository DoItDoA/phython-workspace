#수학
print(abs(-5)) # -5 의 절대값 = 5
print(pow(4, 2)) # 4의 2제곱 = 4 * 4 = 16

from math import * # math 모듈 내의 모든 내용을 가져다 쓰겠다는 의미, math. 안해도 됨

print(floor(4.99)) # 4.99 의 내림 = 4
print(ceil(3.14)) # 3.14 의 올림 = 4
print(sqrt(16)) # 16 의 제곱근 = 4

print("-------1-------")

from random import * # random 모듈에서 모든 것들을 가져다 쓰겠다는 의미

print(random()) # 0.0 이상 1.0 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 이상 10 이하 (11 미만) 의 임의의 정수 값 생성
print(randrange(1, 46)) # 1 이상 46 미만의 임의의 정수 값 생성
print(randint(1, 45)) # 1 이상 45 이하(45를 포함해요!!)의 임의의 정수 값 생성
