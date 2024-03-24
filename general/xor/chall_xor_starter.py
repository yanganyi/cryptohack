s = "label"

print("".join(chr(ord(i)^13) for i in s))

# flag: crypto{aloha}