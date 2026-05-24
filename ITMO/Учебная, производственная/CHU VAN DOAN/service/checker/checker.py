#!/usr/bin/env python3

import copy
import sys
import os

argv = copy.deepcopy(sys.argv)

from pwn import *

context.log_level = 'critical'

OK, CORRUPT, MUMBLE, DOWN, CHECKER_ERROR = 101, 102, 103, 104, 110
SERVICENAME = "todoapp"
PORT = os.environ['PORT'] if 'PORT' in os.environ else 10001

def get_random_string(N=16):
    return ''.join(random.choice(string.ascii_letters) for i in range(N))

def close(code, public="", private=""):
    if public:
        print(public)
    if private:
        print(private, file=sys.stderr)
    print('Exit with code {}'.format(code), file=sys.stderr)
    exit(code)

def put(*args):
    team_addr, flag_id, flag = args[:3]

    try:
        io = remote(team_addr, PORT)

        username  = get_random_string()
        password  = get_random_string()
        note_name = get_random_string()

        help_message = io.recvuntil(b"Choose an option: ")
        if b"TODO List" not in help_message:
            close(MUMBLE, "Invalid help message")

        io.sendline(b"1")
        io.sendlineafter(b"Enter new username: ", username.encode())
        io.sendlineafter(b"Enter new password: ", password.encode())
        io.sendline()

        io.sendlineafter(b"Choose an option: ", b"2")
        io.sendlineafter(b"Username: ", username.encode())
        io.sendlineafter(b"Password: ", password.encode())
        io.sendline()

        io.sendlineafter(b"Choose an option: ", b"3")
        io.sendlineafter(b"Enter TODO name (e.g., todo1): ", note_name.encode())
        io.sendlineafter(b"Enter your note content: ", flag.encode())
        io.sendline()

        io.sendlineafter(b"Choose an option: ", b"4")
        notes = io.recvall(timeout=1)

        if flag.encode() not in notes:
            close(CORRUPT, "Newly created not found")

        io.close()

        close(OK, "{}:{}".format(username, password))

    except Exception as e:
        close(MUMBLE, "PUT Failed")

def error_arg(*args):
    close(CHECKER_ERROR, private="Wrong command {}".format(sys.argv[1]))

def info(*args):
    close(OK, "vulns: 1")

def check(*args):
    team_addr = args[0]

    try:
        io = remote(team_addr, PORT)

        username     = get_random_string()
        password     = get_random_string()
        note_name    = get_random_string()
        note_content = get_random_string()
        print(username)
        print(password)
        print(note_name)
        print(note_content)

        help_message = io.recvuntil(b"Choose an option: ")
        if b"TODO List" not in help_message:
            close(MUMBLE, "Invalid help message")
        io.sendline(b"1")
        io.sendlineafter(b"Enter new username: ", username.encode())
        io.sendlineafter(b"Enter new password: ", password.encode())
        io.sendline()

        io.sendlineafter(b"Choose an option: ", b"2")
        io.sendlineafter(b"Username: ", username.encode())
        io.sendlineafter(b"Password: ", password.encode())
        io.sendline()

        io.sendlineafter(b"Choose an option: ", b"3")
        io.sendlineafter(b"Enter TODO name (e.g., todo1): ", note_name.encode())
        io.sendlineafter(b"Enter your note content: ", note_content.encode())
        io.sendline()

        io.sendlineafter(b"Choose an option: ", b"4")
        notes = io.recvall(timeout=1)

        if note_content.encode() not in notes:
            close(CORRUPT, "Newly created not found")

        io.close()

        close(OK)

    except Exception as e:
        print(f"{e}")
        print("AMOGUS")
        # close(MUMBLE, f"{e}")

def get(*args):
    team_addr, auth_data, flag = args[:3]

    try:
        username, password = auth_data.split(":")

        io = remote(team_addr, PORT)

        io.sendlineafter(b"Choose an option: ", b"2")
        io.sendlineafter(b"Username: ", username.encode())
        io.sendlineafter(b"Password: ", password.encode())
        io.sendline()

        io.sendlineafter(b"Choose an option: ", b"4")
        notes = io.recvall(timeout=1)

        if flag.encode() not in notes:
            close(CORRUPT, "Flag not found")

        io.close()

        close(OK)

    except Exception as e:
        close(CORRUPT)

def init(*args):
    close(OK)

COMMANDS = {
    'put': put,
    'check': check,
    'get': get,
    'info': info,
    'init': init
}

if __name__ == '__main__':
    try:
        COMMANDS.get(argv[1], error_arg)(*argv[2:])
    except Exception as ex:
        close(CHECKER_ERROR, private="INTERNAL ERROR: {}".format(ex))
