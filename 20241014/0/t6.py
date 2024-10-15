def bih(fr , to):
    mw = len(f"{to:b}{to:x}")
    for i in range(fr, to + 1):
        w = mw - len (f"{i:b}{i:x}")
        print(f"0b{i:b} = {' '* w}0x{i:x}")

print(bih(12, 23))
