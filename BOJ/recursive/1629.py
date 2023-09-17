# 자연수 A를 B번 곱한 수를 알고 싶다
# 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성
# INPUT
# A, B, C는 모두 2,147,483,647 이하의 자연수
# OUTPUT
# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력

# 1. b의 값이 짝수인지 홀수인지 파악한다.
# 2. b의 값이 짝수라면 10 ^10 -> (10^5)^2 형태로 바꿔준다.
# 3. b의 값이 홀수라면 10 ^11 -> (10^5)^2 * 10 형태로 바꿔준다.
# # 2^10 -> (2^5)^2
# # 2^11 -> (2^5)^2*10

import sys

a, b, c = map(int, sys.stdin.readline().split())

def mul(a, b):
    if b == 1:
        return a % c
    else:
        temp = mul(a, b // 2) # a^(b // 2)
        if b % 2 == 0:
            return temp * temp % c
        else:
            return temp * temp * a % c

print(mul(a, b))

# pow(밑,지수,나눗셈수) : pow(5,2,3) = 5 * 5 % 3
# print(pow(a,b,c))

# 분할정복
#  10을 10번 곱한 결과는 10을 5번 곱한 것을 2번 곱한것과 같다
# 따라서 이러한 연산이 반복되면 연산횟수가 약 절반으로 줄어든다. 그리고 지수승이 홀수인지 짝수인지 구분
# 이 문제에서는 ‘나는 a^b%c의 값을 반환하는 함수를 만들거야’ 라고 목적을 가지고 반환값을 a^b%c로 설정해주면 이 함수는 목적에 맞게 설계된
# 것이라고 생각하고 더이상 깊게 생각하지 않도록 하는 것이 바람직하다.