year = int(input())

if (year%4==0 and year%100 !=0)or(year%400==0):
    print("1")
else:
    print("0")

# 1. 4의 배수이면서  &
# 2. 100의 배수가 아닐때   또는!!!
# 3. 400의 배수일때