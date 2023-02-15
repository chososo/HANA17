name = input('이름 :')

kor = int(input('국어 :'))
math = int(input('수학 :'))
eng =int ( input('영어 :'))

tot = kor + eng + math 
grade = None
avg = tot/3
if avg >= 90: 
    grade = 'A'
elif avg >=80:
    grade = 'B'
    
elif avg >=70:
    grade = 'C'
    
elif avg >=60:
    grade = 'D'
    
else :     grade = 'F'

print ("이름은 : %s 국어는 %d 수학은 %d 영어는 %d 학점은 %s" %(name, kor, math, eng, grade))


print ("총점 =%d , 평균은 %.2f, 평점 = %s" %(tot, avg,grade))