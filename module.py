# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
# trip_to = ThailandPackage() # travel.thailand. 는 생략
# trip_to.detail()

from travel import *
trip_to = vietnam.VietnamPackage() # 베트남 , 태국은 설정 안되어있어 호출 안됨
trip_to.detail()