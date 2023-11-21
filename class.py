# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def who(self):
#         print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

# areum = Human("아름", 25, "여자")
# print("이름:", areum.name, "나이:", areum.age, "성별:", areum.gender)


print("----------------------------------------------------------------")
# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def who(self):
#         print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

# areum = Human("다희", 24, "여자")
# areum.who()     # Human.who(areum)


print("----------------------------------------------------------------")
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # 소멸자 : 객체가 소멸할 호출되는 함수
    def __del__(self):
        print("나의 죽음을 알리지 말라")

    def who(self):
        print("이름 : {}, 나이 : {}, 성별 : {}".format(self.name, self.age, self.gender))

    #이미 존재하는 값이 아닌 새로운 값을 받아 속성 업데이트하기 위해 who와 달리 인자 새로 받음
    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름", 25, "여자")
del(areum) # 위에서 생성된 areum 객체가 삭제되고, __del__함수에 있는 코드가 실행됨. 

print("----------------------------------------------------------------")
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code

# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)

a = Stock(None, None)
# 객체 a의 set_name 메서드를 호출하는 방법입니다. 파이썬에서는 이런 형태로 메서드를 호출하며, a 객체 자체가 메서드의 첫 번째 인자인 self로 전달
a.set_name("삼성전자") # Stock.set_name(a, "삼성전자")
print(a.name)

a = Stock(None, None)
a.set_code("005930")
print(a.code)


삼성 = Stock("삼성전자", "005930")
print(삼성.get_name()) 
print(삼성.get_code())


print("----------------------------------------------------------------")
class Stock:
    def __init__(self, name, code, per, pbr, profit):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.profit = profit
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)

print("----------------------------------------------------------------")
class Stock:
    def __init__(self, name, code, per, pbr, profit):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.profit = profit
    
    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, per):
        self.per = per
    
    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_profit(self, profit):
        self.profit = profit

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
삼성.set_per(12.75)
print(삼성.per)