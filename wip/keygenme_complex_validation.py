from z3 import *
import sys

# declaration
usn = "RyooGi"
for exp_1 in range(123): 
    if not bytes([exp_1]).isalnum(): continue
    for exp_2 in range(123):
        if not bytes([exp_2]).isalnum(): continue
        c = [Int(f'c{i}') for i in range(25)]
        s = Solver()
        mul = [Int(f'mul{i}') for i in range(25)]
        mul[0] = 1
        printed = 0

        usn_first_char = ord(usn[0])
        usn_second_char = ord(usn[1])
        usn_third_char = ord(usn[2])
        usn_last_char = ord(usn[len(usn) - 1])
        usn_chksum = Int('usn_chksum')
        serial_chksum = Int('serial_chksum')

        # constraints
        # -- serial char --
        for i in range(len(c)):
            if i == 1: 
                s.add(c[i] == exp_1)
                continue
            elif i == 2:
                s.add(c[i] == exp_2)
                continue
            s.add(Or(
                And(c[i] >= ord('0'), c[i] <= ord('9')),
                And(c[i] >= ord('a'), c[i] <= ord('z')),
                And(c[i] >= ord('A'), c[i] <= ord('Z')),
            ))
        # -- usn chksum --
        if usn_last_char < usn_third_char:
            s.add(usn_chksum == usn_second_char + usn_third_char // len(usn) - usn_last_char)
        elif usn_last_char > usn_third_char:
            s.add(usn_chksum == usn_second_char + usn_last_char // len(usn) - usn_third_char)
        else:
            s.add(usn_chksum == usn_second_char + len(c))
        # -- serial chksum --
        s.add(serial_chksum == 153000 - usn_first_char * usn_chksum)
        s.add(serial_chksum == sum([c[i] * mul[i]for i in range(len(c))]))
        # -- mul chksum --
        for i in range(1, len(c)):
            s.add(mul[i] == c[i-1])

        # more constraints 
        if exp_1 == exp_2: s.add((c[13] - c[0] < 0)) # simplification
        else: s.add(((c[13]**exp_1) - (c[0]**exp_2) < 0))

        s.add(c[0] - c[19] > 0)
        s.add(c[12] + c[7] < 140)
        s.add(c[10] * c[8] <= c[16] * c[4])
        
        # model
        while s.check() == sat:
            # print model
            m = s.model()
            serial = "".join([chr(m[c[i]].as_long()) for i in range(len(c))])
            print(usn, serial)

            # print limit
            s.add(Or([c[i]!=m[c[i]] for i in range(25)]))
            printed = printed + 1
            if printed == 10: sys.exit('Limit!')
