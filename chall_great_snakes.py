# download and run the python program using $ python <filename>.py

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
print("".join(chr(o ^ 0x32) for o in ords))

# flag: crypto{z3n_0f_pyth0n}