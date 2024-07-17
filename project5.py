i = 0
sum_ = 0
while i < 50:
    if i % 3 == 0:
        sum_ += i
    i = i + 1

print(sum_)

n = 2
i = 2
is_prime = True
while i < n:
    if n % i == 0:
        is_prime = False
    i += 1 # i = i + 1
print(is_prime)