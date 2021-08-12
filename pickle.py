import pickle # pickle 모듈 가져다 쓰기

profile_file = open("profile.pickle", "wb") # 바이너리(binary) 형태로 저장
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
pickle.dump(profile, profile_file) # profile 데이터를 file 에 저장
profile_file.close()


profile_file = open("profile.pickle", "rb") # 읽을 때에도 바이너리(binary) 명시
profile = pickle.load(profile_file) # file 에 있는 정보를 불러와서 profile 에 저장
print(profile)
profile_file.close()


with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))