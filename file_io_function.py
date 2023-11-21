# def nums_sum(*args):
    
#     result = sum(int(i) for i in args)
#     # result = int(a) + int(b) + int(c)
#     print(f"{args[0]}, {args[1]}, {args[2]}의 합은 {result}입니다")

# nums = input("3개의 숫자를 입력하세요 ex. 2, 4, 6 > ")
# nums = nums.split(",")

# nums_sum(nums[0], nums[1], nums[2])

# print("----------------------------------------------------------")
# def nums_mul(num):
#     num1 = num.split(",")
#     result = 1
#     for i in num1:
#         result *= int(i)
#     print(f"{num}를 모두 곱한 결과는 {result}입니다")


# nums = input("숫자를 입력하세요 예 2, 4, 6, 10 ")
# nums_mul(nums)

# print("----------------------------------------------------------")
import random
import os

hanguls = list("가나다라마바사아자차카타파하")

# folder_path = "datas"
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)

# with open("datas/info.csv", "x", encoding='utf8') as file:

#     for i in range(20):
#         name = random.choice(hanguls) + random.choice(hanguls)

#         weight = random.randrange(40, 100)
#         height = random.randrange(140, 200)

#         file.write(f"{name}, {weight}, {height}\n")

with open("datas/info.csv", "r", encoding='utf8') as file:
    print(file.read())

# bmi 지수 계산하는 함수
def calculate_bmi(weight, height):
    height_m = height / 100 
    bmi = weight / (height_m **2)
    return bmi

# bmi 지수 판단 함수
def bmi_category(bmi):
    if bmi >= 25:
        return "과체중"
    elif 25 > bmi >= 18.5:
        return "정상 체중"
    else:
        return "저체중"

# 파일 읽기
with open("datas/info.csv", "r", encoding='utf8') as file:
    lines = file.readlines()

# 각 라인 bmi지수 처리하고 정보 출력
for line in lines:
    data = line.strip().split(', ') # 각 라인 데이터 분리(strip() 함수로 양쪽 공백 제거, 쉼표와 공백을 기준으로 문자열 분리)

    # 언패킹 기능 사용해 분리된 데이터를 순서대로 아래 변수에 저장
    name, weight, height = data # 이름 체중 키로 분리

    weight = int(weight)
    height = int(height)

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    # {bmi:.2f} : 소수점 이하 숫자를 특정 자릿수까지 표현하는 방법(2는 소수점 이하 2자리)
    print(f"{name}의 BMI지수는 {bmi:.2f}이며, {bmi_category(bmi)}입니다.")


