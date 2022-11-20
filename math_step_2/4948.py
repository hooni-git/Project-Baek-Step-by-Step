n=123456

def prime_list(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True		

primes_list = list(range(2,246912))
ans_list = []

for i in primes_list:
    if prime_list(i):
        ans_list.append(i)
        
        
while True:
    
    cnt = 0

    num = int(input())

    if num == 0:
        break
    
    for i in ans_list:
        if num < i < 2*num+1:
            cnt += 1
            
    print(cnt)