print(9 ** 0.5 * 5) # "1st program"
print(9.99 > 9.98 and 1000 != 1000.1) # "2nd program"
print(((1234 % 1000) // 10)+((5678 % 1000) // 10)) # "3rd program"
a, b = 13.42, 42.13    # "4rd program"
ai, bi = int(a), int(b)
af, bf = int((a - ai) * 100), int((b - bi) * 100)
print(ai == bf or bi == af)