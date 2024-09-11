a = 128  # 2**7          => 10000000
b = 129  # 2**7 + 2**0   => 10000001
c = 130  # 2**7 + 2**1   => 10000010

print(a, bin(a))
print(b, bin(b))

# bittitason "and"
print(a & b, bin(a & b))    # 10000000 & 10000001 => 10000000

# bittitason "or"
print(a | b, bin(a | b))    # 10000000 & 10000001 => 10000001

# bittitason "xor"
print(a ^ b, bin(a ^ b))    # 10000000 & 10000001 => 00000001
