'''
# 자료형
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# 참 / 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)

# 애완동물을 소개해 주세요.
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"

print("우리집" + animal + "의 이름은" + name + "예요")
print(name + "는" + str(age) + "살이며 " + hobby + "을 좋아해요")

print("우리집", animal, "의 이름은", name, "예요")
print(name, "는", age, "살이며 ", hobby, "을 좋아해요")

# +로 연결하게 되면 모두 문자형으로 바꿔줘야 함.
# ,로 연결하게 되면 굳이 모든 것을 문자로 바꿀 필요는 없음. 대신에 ,에는 띄어쓰기가 들어감.


station = "사당"
print(station, "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station, "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station, "행 열차가 들어오고 있습니다.")
'''

'''

print(2**3) # 2^3 = 8
print(5%3) # 나머지
print(5//3) # 몫

print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

'''

'''
# 파이썬에서 숫자 처리 함수

print(abs(-5)) # 5 (절댓값)
print(pow(4, 2)) # 4^2 == 16 (제곱)
print(max(5, 12))
print(min(5, 12))
print(round(3.14)) # 3 (반올림)
print(round(4.99)) # 3 (반올림)

from math import *
print(floor(4.99)) # 4 (내림)
print(ceil(3.14)) # 4 (올림)
print(sqrt(15)) # 3.8xxx (제곱근)
'''

'''
# 랜덤함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 값을 생성.
print(random() * 10) # 0.0 ~ 10.0 미만의 값을 생성
print(int(random() * 10)) # 0 ~ 10 미만의 정수값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하의 정수값 생성

print(randrange(1, 46)) # 1 ~ 46 미만의 임의의 값 생성.
print(randint(1, 45)) # 1 ~ 45 이하의 임의의 값 생성.


print("오프라인 스터디 모임 날짜는 매월", randint(4, 28), " 일로 선정되었습니다.")
'''

'''
# 슬라이싱
jumin = "990120-1234567"

print("성별: " + jumin[7])
print("연: " + jumin[0:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) # 7번째부터 마지막까지
print("뒤 7자리 (뒤에서부터)" + jumin[-7:]) # 마찬가지로 맨 뒤에서부터 쭉
'''

'''
# 문자열 처리

python = "Python is amazing"
print(python.upper()) # 문자열을 대문자로 바꿔주는 함수
print(python.lower()) # 문자열을 소문자로 바꿔주는 함수
print(python[0].isupper()) # 대문자인지 확인해주는 함수
print(len(python))
print(python.replace("Python", "Java")) # 문자열을 치환 (replace!!)

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 첫 번째 n, 그 다음 번째의 n의 index 값
print(index)

print(python.find("Java")) # find의 경우, 없으면 return -1
#print(python.index("Java")) #  index의 경우, 없으면 Error를 return 한다.

print(python.count("n")) # 문자열이 나오는 횟수를 return

'''

# 문자열 포맷

# 방법 1
# print("나는 %d살입니다." %20)
# print("나는 %s를 좋아해요." %"파이썬")
# print("Apple은 %c로 시작해요." %"A")

# print("나는 %s과 %s가 좋아요." %("영", "주"))

# 방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {}과 {}가 좋아요.".format("영", "주"))
# print("나는 {0}과 {1}가 좋아요.".format("영", "주"))
# print("나는 {1}과 {0}가 좋아요.".format("영", "주"))

# 방법 3
# print("나는 {age}이고 {color}이 좋아요.".format(age = 20, color = "파란색"))
# print("나는 {age}이고 {color}이 좋아요.".format(color = "파란색", age = 20))

# 방법 4 (v3.6 이상 ~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")


# 탈출 문자

# \n: 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# 저는 "나도코딩"입니다.
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# \\: 문장 내에 \를 표현하기 위해
# print("\\usr\\local\\bin\\python3 \\Users\\sunghunkim\\python_basic\\practice.py")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine") # "Red "를 삭제하고 "Pine"이 들어감.

# \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple")

'''
# Quiz
url = "http://naver.com"
my_style = url.replace("http://", "")
my_style = my_style.replace(".com", "")

password = my_style + str(len(my_style)) + str(my_style.count("e")) + "!"
print(password)
'''


# 리스트 [] !!
'''
# 지하철 칸별로 10, 20, 30명

suyway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탐.
subway.append("하하")
print(subway)

# 정형돈이 유재석 / 조세호 사이에 탐.
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄.
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬
# num_list = [5,2,3,1,4]
# num_list.sort()
# print(num_list)

# 순서 뒤집기
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장 (extend)
num_list = [5,2,3,1,4]
mix_list = ["조세호", 20, True]

num_list.extend(mix_list)
print(num_list)

'''

# Dictionary(사전)
# key와 value

'''
cabinet = {3: "유재석", 100: "김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3)) # 값을 가져오는 또 다른 방법

#print(cabinet[5]) # 이 경우엔 그냥 Error를 return한다.
#print(cabinet.get(5)) # 이 경우엔 "None"을 return한다.
#print(cabinet.get(5, "사용 가능")) # 이 경우엔, 뒤의 문자열을 Default로 사용한다.

# print(3 in cabinet) # cabinet안에 3이 있는지 확인 -> True
# print(5 in cabinet) # 마찬가지로 확인 -> False

# 문자열로도 key를 설정할 수 있다.
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet)

# 새 손님 등장
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 손님 삭제 -> del
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# key, value 쌍으로 출력
print(cabinet.items())

# Dictionary 초기화
cabinet.clear()
print(cabinet)

'''

# 튜플
'''
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

#menu.add("생선가스") -> 이런 것은 없다.

# 튜플은 기존에 있는 값들로만 사용됨.
'''

# 집합 (set)
# 중복 안됨, 순서 없음
'''
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 위와 현재 코드는 같은 의미이다.

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 또는 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java O, python X)
print(java - python)
print(java.difference(python))

# python을 할 줄 아는 사람이 늘어남. (-> add 명령어)
python.add("김태호")
print(python)

# java를 까먹음 (-> remove 명령어)
java.remove("김태호")
print(java)
'''

# 자료구조 변경
# 커피숍
'''
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))
'''

# Quiz

# 활용 예제
'''
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst) # 리스트를 무작위로 변경
print(lst)
print(sample(lst, 1)) # n개의 샘플을 추출
'''

# 총 20명의 학생이 존재. 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰.

from random import *

student = list(range(1, 21)) # range함수에 대해 잘 알아두자!!!

print(student)
shuffle(student)
winners = sample(student, 4)
chiken = winners[0]
coffee = winners[1:]

print(f"치킨 당첨자 : {chiken}")
print(f"커피 당첨자 : {coffee}")
