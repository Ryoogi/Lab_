from z3 import *

# declaration
s = Solver()
c = [BitVec(f'c{i}', 8) for i in range(13)]

# constraint for domain
for i in range(13):
    if i == 3:
        s.add(c[3] == ord('-'))
    else:
        s.add(c[i] <= ord('9')) 
        s.add(c[i] >= ord('0')) 

master_sum = (c[0] - 48) + (c[1] - 48)  + (c[2] - 48)
for i in range(4, 13, 3):
    master_index = (i - 4) // 3
    segment_sum = (c[i] - 48) + (c[i+1] - 48) + (c[i+2] - 48) 
    s.add((c[master_index] - 48) ^ (master_sum % 3) == segment_sum % 9)

if s.check() == sat:
    m = s.model()
    serial = "".join([chr(m[c[i]].as_long()) for i in range(13)])
    print(serial)