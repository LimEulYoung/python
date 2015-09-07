# -*- coding: utf-8 -*-
#식별자 만드는법
#식별자 : 변수, 함수, 모듈 ,클래스 또는 객체를 식별하는데 사용되는 이름
#대소문자 구분함.

a=10
A=20
print a,A

_aaa=10
_AAA=20
print a,A

#2_aaa=20 : 불가능 (숫자가 앞에올수 없음)

#예약어는 변수이름으로 만들면 안된다.

print str(12345)
#str='abc'
#print str(12345)

#변수를 선언할때 타입을 선언하는것이 아니라 변수를 사용할때 type이 정의됨.

a =1.0
print type(a)

print str(a)

#del : 변수의 삭제
del a
#print a


#연속라인
a = 1
b = 3
if(a==1) and \
(b==3):
    print 'connected line!'

#할당문
a = 1
b = a
# 1+3 = a :불법

a = 1
a = a + 1
print a

c, d = 3, 4
print c,d
x = y = z = 0
print x,y,z

#swap하는 방법
e = 4.5
f = 5.5
e, f = f, e
print e

a = 1
a += 4
print a

a = 10
a *= 2+3
print a

#객체와 할당
a = [1,2,3]
b = [10,a,20]
print b
c = ['x',a,'y']
print c

a[1] = 1000
print c

