a = int(input())
ans = 1
while a>0:
	print(a%10*ans, end=' ' )
	ans = ans*10
	a = a//10