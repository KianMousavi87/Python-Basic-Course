def to_base(number, base):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = []
    while number !=0:
        r = number % base #باقی مانده
        number = number // base #خارج قسمت 
        digits.insert(0, r)
    return "".join([mapping[d] for d in digits])

print(to_base(17, 3)) # 122
print(to_base(23, 4)) # 113
print(to_base(255, 16)) # FF