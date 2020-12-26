"""
클래스 class 특징
- 객체마다 고유한 성격을 가진다. 
- 다른 객체에게 서로 영향을 주지 않는다.
- 1개의 클래스로 무수히 많은 객체를 만들 수 있다.

객체변수 특징
- 객체변수 : 객체의 고유 값을 저장할 수 있는 공간
- 객체변수는 다른 객체들 영향받지 않고 독립적으로 그 값을 유지한다.
"""

class FourCal : #사칙연산 클래스 만들기
    def __init__(self, first, second) :    #생성자 메서드 : 객체가 생성되는 시점에서 자동으로 호출됨
        self.first = first
        self.second = second

    def setdata(self, first, second) :     #입력데이터를 받는 메서드 setdata 생성
        self.first = first
        self.second = second
    
    def add(self) :         #더하기 메서드
        result = self.first + self.second
        return result
    
    def mul(self) :         #곱하기 메서드
        result = self.first * self.second
        return result
    
    def sub(self) :         #빼기 메서드
        result = self.first - self.second
        return result
    
    def div(self) :
        result = self.first / self.second
        return result


a = FourCal(4,2) #객체 a 생성
b = FourCal(3,7) #객체 b 생성
#a.setdata(4,2)
#b.setdata(3,7)
print('a1 = %d' % a.first)  #객체 a 의 첫 번째 변수
print('a2 = %d' % a.second) #객체 a 의 두 번째 변수
print('b1 = %d' % b.first)  #객체 b 의 첫 번째 변수
print('b2 = %d' % b.second) #객체 b 의 두 번째 변수

print(id(a.first))          #객체 a 의 첫 번째 변수의 주소값
print(id(b.first))          #객체 b 의 첫 번째 변수의 주소값 #a와 b가 저장된 곳이 완전 다르다.

print("a1 + a2 = %d" % a.add())
print("a1 * a2 = %d" % a.mul())
print("a1 - a2 = %d" % a.sub())
print("a1 / a2 = %d" % a.div())
print("b1 + b2 = %d" % b.add())
print("b1 * b2 = %d" % b.mul())
print("b1 - b2 = %d" % b.sub())
print("b1 / b2 = %d" % b.div())

"""
상속 : 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것
"""

class MoreFouCal(FourCal) : #FourCal 클래스를 상속하는 클래스
    def pow(self) :         #FourCal 클래스 기능 확장함
        result = self.first ** self.second
        return result
    
c = MoreFouCal(4,2)
print("c1 + c2 = %d" % c.add())   #FourCal 기능을 그대로 사용할 수 있음
print("c1 ** c2 = %d" % c.pow())  #FourCal에서 확장된 기능을 사용할 수 있음


class SafeFourCal(FourCal) :
    def div(self) :               #오버라이딩 : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것
        if self.second == 0 :
            return 0
        else :  
            return self.first / self.second
d = SafeFourCal(4,0)
print("d1 / d2 = %d " % d.div())

"""
클래스 변수 : 클래스 안에 변수를 선언함
클래스 변수 특징 : 클래스로 만든 모든 객체에 공유된다
"""