constant = 4
length = constant + constant * constant - 1
key = [0] * length

# hyphen
for i in range(constant-1):
    key[constant + (constant + 1) * i] = '-'

def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0: return 0
    return 1

for a in range(48, 123):
    if not (a >= 48 and a <= 57) and not (a >= 65 and a <= 90) and not (a >= 97 and a <= 122): continue # if not alphanumeric ascii

    for b in range(48, 123):
        if not (b >= 48 and b <= 57) and not (b >= 65 and b <= 90) and not (b >= 97 and b <= 122): continue # if not alphanumeric ascii

        for c in range(48, 123):
            if not (c >= 48 and c <= 57) and not (c >= 65 and c <= 90) and not (c >= 97 and c <= 122): continue # if not alphanumeric ascii
            
            for d in range(48, 123):
                if not (d >= 48 and d <= 57) and not (d >= 65 and d <= 90) and not (d >= 97 and d <= 122): continue # if not alphanumeric ascii

                if is_prime(a + b + c + d):
                    key[0] = chr(a)
                    key[1] = chr(b)
                    key[2] = chr(c)
                    key[3] = chr(d)

                    key[5] = chr(a)
                    key[6] = chr(b)
                    key[7] = chr(c)
                    key[8] = chr(d)

                    key[10] = chr(a)
                    key[11] = chr(b)
                    key[12] = chr(c)
                    key[13] = chr(d)

                    key[15] = chr(a)
                    key[16] = chr(b)
                    key[17] = chr(c)
                    key[18] = chr(d)
                    
                    print("".join(key))