a = 123456789
b = 987654321
 

def gcd (a, b):
  print(a, b)
  if a == 0: return b 
  if b == 0: return a 
  return gcd(b, a%b)

ans = gcd(a, b)
print(ans)
  