
# recursive functiuon to calculate n!
def factorial(n):
  if (n != 1):
    ans = (n)*factorial(n-1)
  
  else:
    ans = 1
  
  return ans

# def sum():
#   return 

fact = (lambda x: 1 if x == 0 else x* fact(x-1))

sum = 0
#print(list(str(fact(5))))
#print((lambda y: (for digit in str(fact): sum+=eval(digit)))

for digit in str(str(fact(5))):
  sum += eval(digit) 
  
print(sum)