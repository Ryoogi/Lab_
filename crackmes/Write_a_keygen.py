import sys

# key related
constant = 4
key_length = constant + constant * constant - 1
key = [0] * key_length

# key_chunk related
chunk_index = 0
previous_ascii = 0

keys_printed = 0 # to limit key output

# prime checker
def is_prime(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0: return 0
    return 1

# key hyphen
for i in range(constant-1):
    key[constant + (constant + 1) * i] = '-'

# key chunk generator
for a in range(48, 123):
    if not (a >= 48 and a <= 57) and not (a >= 65 and a <= 90) and not (a >= 97 and a <= 122): continue # if not alphanumeric ascii

    for b in range(48, 123):
        if not (b >= 48 and b <= 57) and not (b >= 65 and b <= 90) and not (b >= 97 and b <= 122): continue # if not alphanumeric ascii

        for c in range(48, 123):
            if not (c >= 48 and c <= 57) and not (c >= 65 and c <= 90) and not (c >= 97 and c <= 122): continue # if not alphanumeric ascii

            for d in range(48, 123):
                if not (d >= 48 and d <= 57) and not (d >= 65 and d <= 90) and not (d >= 97 and d <= 122): continue # if not alphanumeric ascii
                current_ascii = a + b + c + d

                if is_prime(current_ascii) and current_ascii > previous_ascii:
                    # fill key
                    for i in range(4):
                        var = [a, b, c, d]
                        key[chunk_index * 5 + i] = chr(var[i])
                    
                    chunk_index = (chunk_index + 1) % 4
                    previous_ascii = current_ascii

                    if chunk_index == 0: 
                        previous_ascii = 0
                        print("".join(key))

                        # limit key output
                        keys_printed += 1
                        if keys_printed == 10: sys.exit("\nOutput is limited to 10 keys.")