import sys
input = sys.stdin.readline

num = input().split('-')
sum = 0
for i in num[0].split('+'):
    sum += int(i)
for i in num[1:]:
    for j in i.split('+'):
        sum -= int(j)
print(sum)