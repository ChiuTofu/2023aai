a = int(input())
b = a//60//60
c = a//60%60
d = a%60
print(f'{b:02}:{c:02}:{d:02}',end='')
