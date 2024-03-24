import pwn,Crypto.Util.number,json,codecs

d={
    "base64": pwn.b64d,
    "hex": pwn.unhex,
    "utf-8": bytes,
    "rot13": lambda s: codecs.encode(s,"rot_13").encode(),
    "bigint": lambda s: Crypto.Util.number.long_to_bytes(int(s,0))
}

def dec(o):
    return d[o["type"]](o["encoded"])

r = pwn.remote("socket.cryptohack.org", 13377)
for _ in range(100):
    o = json.loads(r.recvline())
    r.sendline(json.dumps({"decoded": dec(o).decode()}))
r.interactive()

# flag: crypto{3nc0d3_d3c0d3_3nc0d3}