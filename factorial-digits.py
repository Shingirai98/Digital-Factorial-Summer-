# -------------------------------------------------------
# |  Name: Digital Factorial Sum                              |
# |  @Author: Shingirai Denver Maburutse              |
# |  Date:   18/07/2021                                            |
# -----------------------------------------------------
import numpy as np
import sys

# allow for a high recursion limit
sys.setrecursionlimit(10**8)

# convert an array type to another type
def cast(arr, data_type):
    return np.array(list(map(data_type, arr)))

# ->convert list to integers  -> convert list to numpy array  -> sum up the elements  
def summing(arr):
  return np.sum(np.array(cast(arr, int)))

# lambda function to find factorial by recursion
fact = (lambda num: 1 if num == 0 else num* fact(num-1)) # Assignment operator(=) was used because its a recursive function but it is stored as a pointer which is space efficient

def main():
  # ->listify the factorial -> find the sum
  try:
    print(summing(list(str(fact(int(sys.argv[1])))))) # sys.argv[1] -> user input bash argument
  
  except:
    print("Please enter a positive real number")

if __name__ == '__main__':
  main()
