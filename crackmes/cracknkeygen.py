from z3 import *

s = Solver()
length = len("secret")

raw_key = [BitVec(f'r_{i}', 8) for i in range(length)]
key = [raw_key[i] ^ i for i in range(length)]

for i in range(length):
    char_code = key[i]
    s.add(Or(
        And(char_code >= 48, char_code <= 57),
        And(char_code >= 65, char_code <= 90),
        And(char_code >= 97, char_code <= 127)
    ))
    s.add(raw_key[i] >= 32, raw_key[i] <= 127)

if s.check() == sat:
    m = s.model()
    
    raw_result = "".join([chr(m[raw_key[i]].as_long()) for i in range(length)])
    
    key_result = "".join([chr(m.evaluate(key[i]).as_long()) for i in range(length)])

    print(f"Raw key: {raw_result}")
    print(f"Key (XOR result): {key_result}")