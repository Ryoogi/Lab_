import sys
length = len("secret")
raw_key = [127] * length
key = [0] * length
incremented = 0

for i in range(length - 1):
    raw_key = [127] * length
    
    raw_key[i] = 32
    raw_key[i+1] -= 32
    for j in range(i + 1, length):
        while(1): # transfer value loop
            for counter in range(0, length, 1): # xor to key loop
                key[counter] = raw_key[counter] ^ counter
                if not (key[counter] >= 48 and key[counter] <= 57) and not (key[counter] >= 65 and key[counter] <= 90) and not (key[counter] >= 97 and key[counter] <= 127): 
                    break;
                if counter == length - 1:
                    print("".join([chr(n) for n in key]))
            
            if raw_key[i] < 127 and raw_key[j] == 32: 
                if j == length - 1: j = i + 1
                else: 
                    j += 1
                    incremented = 1
            elif raw_key[i] == 127: 
                if incremented == 1: 
                    j -= 1
                    incremented = 0
                break
            raw_key[i] += 1
            raw_key[j] -= 1

# this solver's logic is failed to generate alphanumerical logic despite key worked
# writer know the supposed logic but refused to remodel (bro i've been 2 days here)