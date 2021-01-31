# 1から100までの素数を求める（関数利用）
def check_prime(num):
    if num < 2:
        # 2未満は素数ではない
        return False
    elif num == 2:
        # 2は素数
        return True
    elif num % 2 == 0:
        # 偶数は素数ではない
        return False

    # 奇数を確認
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True


prime = []
for num in range(1, 101):
    if check_prime(num):
        prime.append(num)

print(prime)
