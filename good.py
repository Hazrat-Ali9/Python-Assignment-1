from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))

mp = defaultdict(int)
for num in a:
    mp[num] += 1

ans = 0
for num, count in mp.items():
    if count < num:
        ans += count
    else:
        ans += count - num

print(ans)