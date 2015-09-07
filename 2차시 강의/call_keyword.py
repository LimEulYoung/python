# -*- coding: utf-8 -*-
import keyword


print keyword.kwlist
print
print len(keyword.kwlist)
#대표적 내장함수
#abs,max, min, sum, str, range, type...

#abs:
print abs(-2)
#max :
print max(1,2)
print max([1,2,3])

#min:
print min(1,2,3,4,5)

#pow:
print pow(2,5)

#chr : 아스키코드값을 문자를 반환
print chr(97)

#str : 해당객체를 문자열로 반환해주는 함수
print str(3)
print str([1,3,4])

#range : 
print range(10)
print range(3,10)
print range(3,10,2) #2는 step의 역할: 2씩 건너뛰게함.
#range(start,[stop],[step])

#type : 객체의 자료형을 반환
print type(-1)
print type('abc')
print type([1,2,3])



