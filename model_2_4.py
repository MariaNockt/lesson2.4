numbers_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_ = []
not_prime = []

for i in range(2, 16):
    for j in prime_:
        if i % j == 0:
            is_prime = False
            break
    else:
        is_prime = True
    if is_prime:
        prime_.append(i)
    else:
        not_prime.append(i)

print('Prime: ', prime_)
print('Not prime:', not_prime)