# 1から100までの素数を求める
# 2は自明なので入れておく
prime = [
    2,
]

for num in range(3, 101, 2):
    for i in prime:
        if num % i == 0:
            # これまでの素数で割り切れたら非素数
            break
    else:
        # これまでの素数で割り切れる値が無ければ素数
        prime.append(num)

print(prime)
