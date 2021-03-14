# 계산기 클래스 만들기
class FourCal :
    def setdata(self, first, second) :  # 메서드 : 클래스 안에 구현된 함수
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def mul(self) : 
        result = self.first * self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result

a = FourCal()
print(type(a))  # <class '__main__.FourCal'>

a.setdata(4, 2)
print(a.first)  # 4
print(a.second) # 2

#####################
# 클래스로 만든 객체의 객체 변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지한다.

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 7)
print(a.first)  # 4
print(b.first)  # 2

# 서로 다른 주소에 저장되어 있음을 알 수 있다.
print(id(a.first))  # 140717040936832
print(id(b.first))  # 140717040936800

############# 
a = FourCal()
a.setdata(10,2)
print(a.add())  # 12
print(a.mul())  # 20
print(a.sub())  # 8
print(a.div())  # 5.0

########### setdata 메서드를 수행한 후에 사칙연산 함수들을 사용할 수 있다.
c = FourCal()
# print(c.add())  # AttributeError: 'FourCal' object has no attribute 'first'
# 번거롭다 : setdata와 같은 메서드를 호출하여 초깃값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법이다.
# 생성자 : 객체가 생성될 때 자동으로 호출되는 메서드
# __init__ 


class FourCal2 :
    def __init__(self, first, second) :  # 생성자 : 객체가 생성될 때 자동으로 호출됨
        self.first = first
        self.second = second
    def setdata(self, first, second) :  # 메서드 : 클래스 안에 구현된 함수
        self.first = first
        self.second = second
    def add(self) :
        result = self.first + self.second
        return result
    def mul(self) : 
        result = self.first * self.second
        return result
    def sub(self) :
        result = self.first - self.second
        return result
    def div(self) :
        result = self.first / self.second
        return result

a = FourCal2(2,4)   # 따로 setdata를 선언하지 않아도 작동된다.
print(a.first)  # 2
print(a.second) # 4
print(a.add())  # 6

############### 상속 : 어떤 클래스를 만들 떄 다른 클래스의 기능을 물려받을 수 있다. 상속한 클래스의 기능을 모두 사용할 수 있다.
class MoreFourCal(FourCal2) :    # 괄호 안에 상속할 클래스 이름을 넣어준다.
    def pow (self) :
        result = self.first ** self.second
        return result
    pass

a = MoreFourCal(4, 8)
print(a.add())  # 12
print(a.mul())  # 32
print(a.pow())  # 65536

############# 오버라이딩 : 상속한 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것 (덮어 씌우기)
a = MoreFourCal(8, 0)
# print(a.div())  # ZeroDivisionError: division by zero

class SafeFourCal (MoreFourCal) :
    def div(self) :
        if self.second == 0 :
            return 0
        else :
            return self.first / self.second
a = SafeFourCal(8, 0)
print(a.div())   # 0

########## 클래스 변수 : 클래스 안에 변수를 선언하여 생성한다.
class Family :
    lastname = "황"
print(Family.lastname)  # 황

a = Family( )
b = Family()
print(a.lastname)   # 황

# 클래스 변수 변경 >> 클래스로 만든 모든 객체에 공유된다.
Family.lastname = "박"
print(a.lastname)   # 박
print(b.lastname)   # 박
