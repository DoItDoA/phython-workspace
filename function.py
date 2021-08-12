#return이 2개
def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 출금 수수료 100원
    return commission, balance - money - commission # 튜플 형식으로 반환
    
balance = 0 # 최초 잔액
# 저녁에 출금 시도
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))


#가변인자
def profile(name, age, *language): # 언어 정보를 전달하고 싶은 갯수 만큼 전달 가능    
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # print(type(language)) # tuple
    for lang in language:
        print(lang, end=" ") # 언어들을 모두 한 줄에 표시
    print() # 줄바꿈 목적

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript") # JavaScript 추가
profile("김태호", 25, "Kotlin", "Swift")