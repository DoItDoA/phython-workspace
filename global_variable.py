gun = 10

def checkpoint(soldiers):
    global gun # 전역공간에 있는 gun 이라는 변수를 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

#글로벌 변수 대신
gun = 10

def checkpoint_ret(gun, soldiers): # 전체 총 수와 군인 수를 전달받음
    gun = gun - soldiers # 전달받은 gun 을 사용
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2) # gun 값을 함수에 전달
print("남은 총 : {0}".format(gun))