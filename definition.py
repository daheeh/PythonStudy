def print_coin():
    print("비트코인")

print_coin() 

print("----------------------------------------------------------------")
def print_coins():
    for i in range(100):
        print_coin() 

# print("----------------------------------------------------------------")
# str = input("문자를 입력해주세요")
# def print_with_smile(str):
#     print(str, ":D")

# print_with_smile(str)

print("----------------------------------------------------------------")
price = int(input("가격을 입력해주세요"))
def print_upper_price(price):
    print(int(price* 1.3), "원")

print_upper_price(price)

print("----------------------------------------------------------------")
def print_sum(a, b):
    print(a + b)

print("----------------------------------------------------------------")
def print_arithmetic_operation(a, b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)

print("----------------------------------------------------------------")
def print_max(a, b, c):
    print(max(a, b, c))

print("----------------------------------------------------------------")
def print_reverse(str):
    # print(str.reverse())
    # reverse()는 리스트 외 다른 자료형에서 사용 불가.
    # 문자열을 역순으로 만드는 파이썬의 슬라이싱 표현
    print(str[::-1])

print("----------------------------------------------------------------")
def print_score(score_list):
    print(sum(score_list) / len(score_list))

print("----------------------------------------------------------------")
#223할 차례












































