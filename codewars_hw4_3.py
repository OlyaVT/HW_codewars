def solution(n):
    return sum(range(3, n, 3)) + sum(range(5, n, 5)) - sum(range(15, n, 15))
    

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
  