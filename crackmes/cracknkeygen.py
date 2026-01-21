import sys

length = len("secret")
key = [0] * length

comp_cks = 0
key_cks = 0 
for i in range(length):  comp_cks += (ord("secret"[i]) ^ i)

trial_count = 0

pointer = length - 1
key[pointer] = 48

while(1):
    if key[pointer] > 123:
        key[pointer] = 48
        key[pointer-1] += 1
        if key[pointer-1] > 123:
            key[pointer-1] = 48
            key[pointer-2] += 1
            if key[pointer-2] > 123:
                key[pointer-2] = 48
                key[pointer-3] += 1
                if key[pointer-3] > 123:
                    key[pointer-3] = 48
                    key[pointer-4] += 1
                    if key[pointer-4] > 123:
                        key[pointer-4] = 48
                        key[pointer-5] += 1
                        if key[pointer-5] > 123: break

    key_cks = 0
    for i in range(length):
        key_cks += (key[i] ^ i)
    
    if key_cks == comp_cks:
            print(trial_count)
            sys.exit("".join([chr(n) for n in key]))
    # else: print(f"{key_cks} != {comp_cks}")
    
    key[pointer] += 1
    trial_count += 1