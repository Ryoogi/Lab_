from z3 import *

# declaration
usn = "Ryoogi"
c = [BitVec(f'c{i}', 32) for i in range(25)]
# c = [Int(f'c{i}') for i in range(25)]
s = Solver()
mul = [BitVec(f'mul{i}', 32) for i in range(25)]
# mul = [Int(f'mul{i}') for i in range(25)]
mul[0] = 1

usn_first_char = ord(usn[0])
usn_second_char = ord(usn[1])
usn_third_char = ord(usn[2])
usn_last_char = ord(usn[len(usn) - 1])
usn_chksum = BitVec('usn_chksum', 32)
# usn_chksum = Int('usn_chksum')
serial_chksum = BitVec('serial_chksum', 32)
# serial_chksum = Int('serial_chksum')

# constraints
# -- serial char --
for i in range(len(c)):
    s.add(Or(
        And(c[i] >= ord('0'), c[i] <= ord('9')),
        And(c[i] >= ord('a'), c[i] <= ord('z')),
        And(c[i] >= ord('A'), c[i] <= ord('Z')),
    ))
# -- usn chksum --
if usn_last_char < usn_third_char:
    s.add(usn_chksum == usn_second_char + usn_third_char // len(c) - usn_last_char)
elif usn_last_char > usn_third_char:
    s.add(usn_chksum == usn_second_char + usn_last_char // len(c) - usn_third_char)
else:
    s.add(usn_chksum == usn_second_char + len(c))
# -- serial chksum --
s.add(serial_chksum == 153000 - usn_first_char * usn_chksum)
s.add(serial_chksum == sum([c[i] * mul[i]for i in range(len(c))]))
# -- mul chksum --
for i in range(1, len(c)):
    s.add(mul[i] == c[i-1])

# more constraints 
# s.add((pow(c[13], c[1]) - pow(c[0], c[2]) < 0))
# s.add(((c[13]**c[1]) - (c[0]**c[2]) < 0))
# s.add(c[0] - c[19] > 0)
# s.add(c[12] + c[7] < 140)
# s.add(c[10] * c[8] <= c[16] * c[4])
    
# print(s.check())
# model
if s.check() == sat:
    m = s.model()
    serial = "".join([chr(m[c[i]].as_long()) for i in range(len(c))])
    print(serial)
