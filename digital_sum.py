
def factorial(n):
  if (n != 1):
    ans = (n)*factorial(n-1)
  
  else:
    ans = 1
  
  return ans

num = str(factorial(5))
sum = 0
for digit in num:
  sum += eval(digit) 
  
print(sum)