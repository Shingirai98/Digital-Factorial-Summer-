
def factorial(n):
  if (n != 1):
    ans = (n)*factorial(n-1)
  
  else:
    ans = 1
  
  return ans

print(factorial(5))