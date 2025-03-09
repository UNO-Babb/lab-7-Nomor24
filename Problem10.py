#Problem10.py
#Project Euler problem 10
#finds the sum of all prime numbers under 2 million
from NumberTests import isPrime

def main():
    total = 0
    for i in range(2000001):
       if isPrime(i):
          total += i
    print(total)
if __name__ == '__main__':
  main()
