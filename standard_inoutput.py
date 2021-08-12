print("Python", "Java", sep=",") # 값들을 콤마(,) 로 구분

import sys # sys 모듈을 가져와서 사용하겠다는 의미
print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 표준 에러

# file= 에 sys.stdout (Standard Output, 표준 출력) 와 sys.stderr (Standard Error, 표준 에러) 를 각각 넣었는데, 
# 출력결과는 크게 달라보이지 않습니다. 머지 않은 미래에 보다 큰 규모의 파이썬 프로젝트를 진행하게 되면 필요해질텐데, 
# stdout 과 stderr 은 사용하는 용도가 조금 다릅니다.
# 보통 프로그램 수행 과정에서 몇 시에 어떤 작업을 어떤 식으로 수행하고 있으며 그 결과는 어떠한지 등의 정보를 가지는 
# 로그를 남길 때 stdout 은 일반적인 내용을, stderr 는 에러 발생 시 관련 내용을 출력하기 위해 사용할 수 있습니다. 
# 이렇게 구분지어주면 프로그램이 의도치 않은 동작을 하는 경우에 에러 로그만 확인하면 보다 빠르게 상황 파악 및 조치가 가능해집니다.


scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items(): # key, value
    print(subject, score)


scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")


for num in range(1, 10): # 1~9 까지의 숫자
    print("대기번호 : " + str(num).zfill(3))