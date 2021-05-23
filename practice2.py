# weather = input("오늘 날씨는 어때?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크 챙기세요")
# else:
#     print("준비물 필요없어요.")

# if 조건문

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요.")
# elif 10 <= temp and temp < 30:  # 기본적인 if 조건
#     print("괜찮은 날씨에요!")
# elif 0 <= temp < 10:            # 조건을 이렇게 줄 수도 있다.
#     print("추워요!")
# else:
#     print("나가지마세용")


# 반목문 for

# for waiting_num in [0, 1, 2, 3, 4]:
#     print(f"대기번호: {waiting_num}")

# for waiting_nums in range(6):
#     print(f"대기번호: {waiting_nums}")

# starbucks = ["아이언맨", "토르", "원더우먼"]
# for customer in starbucks:
#     print(f"{customer}님, 커피가 준비되었습니다.")

# 반복문 while

# customer = "토르"
# index = 5
# while index >= 1:
#     print(f"{customer}님, 커피가 준비되었습니다.")
#     index = index - 1
#     if index == 0:
#         print("커피는 폐기처분 됨")

# 조건을 통한 반복
# customer = "토르"
# person = "Unknown"

# while person != customer:
#     print(f"{customer}님, 커피가 준비되었습니다.")
#     person = input("이름이 어떻게 되세요? ")


# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(f"오늘 수업은 여기까지. {student}는 교무실로 따라와.")
#         break;
#     else:
#         print(f"{student}는 책 읽어봐.")


# 한 줄 for문
# 출석번호가 1 2 3 4 앞에 100을 붙이기로 함.

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환

# student = ["Iron man", "Thor", "I am groot"]
# student = [len(i) for i in student]
# print(student)


# Quiz

# from random import *

# sum = 0;
# for i in range(1, 51):
#     running_time = randint(5, 50)
#     if 5 <= running_time <= 15:
#         check = "O"
#         sum += 1
#     else:
#         check = " "
#     print(f"[{check}] {i}번째 손님 (소요시간 : {running_time}분)")
# print(f"총 탑승 승객 : {sum} 분")


# 함수
'''
def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}원 입니다.")
    return balance + money

def withdraw(balance, money):
    if balance > money:
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
        return balance - money
    else:
        print(f"출금이 완료되지 않았습니다. 잔액은 {balance}원 입니다.")
        return balance

def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission # 튜플 형태로 return 을 한다.

balance = 0
balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(balance)

commission, balance = withdraw_night(balance, 500)
print(f"수수료는 {commission}원 이고 잔액은 {balance}원 입니다.")
'''

# 기본값.

# def profile(name, age, main_lang):
#     print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 이렇게 기본값을 지정할 수 있다.
# def profile(name, age=17, main_lang="파이썬"):
#     print(f"이름: {name}\t나이: {age}\t주 사용 언어: {main_lang}")

# profile("유재석")
# profile("김태호")


# 가변인자

# 이 경우엔 함수의 인자가 정해져있음.
'''
def profile(name, age, lang1, lang2, lang3, lang4):
    print(f"이름: {name}\t나이: {age}\t", end=" ")
    print(lang1, lang2, lang3, lang4)

profile("유재석", 20, "Python", "Java", "C", "C++")
profile("김태호", 25, "Kotlin", "JS", "", "")
'''

# 아래처럼 가변인자를 통해 해결 가능.
'''
def profile(name, age, *language):
    print(f"이름: {name}\t나이: {age}\t", end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "Nodejs")
profile("김태호", 25, "Kotlin", "JS")
'''
'''
gun = 10

def checkpoint(soldiers):
    global gun # 전역 공간에 있는 gun을 사용하겠다는 의미
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")
gun = checkpoint_ret(gun, 2)
print(f"남은 총 : {gun}")
'''

# Quiz6
'''
def std_weight(height, gender):
    if gender == "남자":
        weight = round(height * height / 10000 * 22, 2)
        print(f"키 {height}cm 남자의 표준 체중은 {weight}kg 입니다.")
    if gender == "여자":
        weight = round(height * height / 10000 * 21, 2)
        print(f"키 {height}cm 여자의 표준 체중은 {weight}kg 입니다.")

std_weight(175, "남자")
'''

# 표준 입출력
'''
print("Python", "Java") # 이 경우엔, 띄어쓰기가 된다.
print("Python", "Java", sep = " vs ", end = "?") # sep이라는 속성, end라는 속성
'''

# 시험 성적
'''
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
'''

# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))

'''
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐, +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고 빈칸으로 _채우기
print("{0:_<10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(1000000000000))
# 3자리 마다 콤마 + 부호까지
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))
# 3자리 마다 콤마 찍기 + 부호 붙이기 + 자릿수 확보
# 빈 자리는 ^로 채우기
print("{0:^<+30,}".format(1000000000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리까지 (나머지는 반올림)
print("{0:.2f}".format(5/3))
'''
'''
# 파일에 쓰기 (w)

score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 100", file=score_file)
print("영어 : 0", file=score_file)
score_file.close()

# 파일에 이어서 쓰기 (a)

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

# 파일 읽어오기 (r)

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 파일을 한 줄씩 읽기 (readline())

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄 별로 읽기, 한 줄 읽고 커서는 다음으로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
'''
'''
# 몇 줄인지 모를 때 처리 방법 (while문으로 조지기)

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()

# 파일의 내용을 리스트 형태로 담기.

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()
'''

# pickle은 파이썬 객체 자체를 저장하기 위한 모듈
'''
import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # dump라는 것을 통해 profile_file에 profile을 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # load라는 것을 통해 profile_load를 불러온다.
print(profile)
profile_file.close()
'''

# with
'''
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬을 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
'''

# Quiz 7

for week in range(1, 51):
    file = open(f"{week}주차.txt", "w", encoding="utf8")
    # file = open("{}주차.txt".format(week), "w", encoding="utf8") 로 해도 된다.
    file.write(f"- {week} 주차 주간보고 -\n")
    file.write("부서 :\n")
    file.write("이름 :\n")
    file.write("업무 요약 :\n")
    file.close()











