from pwn import *
import json

HOST = "socket.cryptohack.org"
PORT = 11112

r = remote(HOST, PORT)


def json_recv():
    line = r.readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


print(r.readline())
print(r.readline())
print(r.readline())
print(r.readline())

request = {
    "buy": "flag"
}
json_send(request)

response = json_recv()

print(response)

# flag: crypto{sh0pp1ng_f0r_fl4g5}

# for this challenge, the sample script was provided
# the script can be simplified as such when you're in an actual CTF

# from pwn import *
# import json

# r = remote("socket.cryptohack.org", 11112)

# for i in range(4):
#     print(r.readline())

# request={"buy":"flag"}

# request = json.dumps(request).encode()
# r.sendline(request)

# line = r.readline()
# response = json.loads(line.decode())

# print(response)