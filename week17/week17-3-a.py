a= int(input())
temp = 1
ans = 0
while a >= ans:
	ans += temp
	temp += 1
print(temp-1,end='')