(name, age, hobby) = ("김종국", 20, "코딩") # name="김종국", age=20, hobby="코딩"


students = [1, 2, 3, 4, 5]
print(students) # [1, 2, 3, 4, 5]

# 한 줄 for 를 이용하여 각 항목에 100 을 더함
students = [i + 100 for i in students] # list 안에서 for 문 작동
print(students) # [101, 102, 103, 104, 105]

students = ["Iron man", "Thor", "I am groot"]
print(students) # ["Iron man", "Thor", "I am groot"]

# 한 줄 for 를 이용하여 각 이름을 대문자로 변경
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']
