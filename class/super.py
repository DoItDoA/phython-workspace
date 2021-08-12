class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0) # speed 0 : 건물은 지상 이동 불가
        super().__init__(name, hp, 0) # 위와 마찬가지로 부모 클래스 접근. self 없이 사용
        self.location = location
 
 #다중 상속일 경우
class Unit2:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
        
# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit2): # 순서 변경
    def __init__(self):
        super().__init__() # 부모 첫번째 호출 (Flyable)
        

# 드랍쉽
dropship = FlyableUnit()