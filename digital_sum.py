import numpy as np

# recursive functiuon to calculate n!
def factorial(n):
  if (n != 1):
    ans = (n)*factorial(n-1)
  else:
    ans = 1
  return ans

def summing(arr):
  arr2 = []
  for i in arr:
    arr2.append(int(i))
  return np.sum(np.array(arr2))

fact = (lambda x: 1 if x == 0 else x* fact(x-1))
print(summing(list(str(fact(5)))))
