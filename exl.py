# Excercise 
second =input('초단위의 시간을 입력하세요 : ')
print ('second 변수의 타입 = ', type(second))

second = int(second)
print ('second 변수의 타입 = ', type(int(second)))

print (f'{second//3600}시간 {second%3600//60}분 {second%60}초 입니다. ' )

