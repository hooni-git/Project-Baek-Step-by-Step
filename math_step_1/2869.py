a, b, v = map(int, input().split())

snail_p = 0
ans = 0

snail_p = v - a
speed = a - b

ans = (snail_p // speed) + 1

if snail_p % speed:
    ans += 1

print(ans)