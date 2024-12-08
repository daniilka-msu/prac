def decode_cp1251_utf8_latin1(i):
    return i.encode('latin1', errors='replace').decode('cp1251', errors='replace')

try:
    while True:
        t = input()
        if t.lower() == 'exit':
            break
        print(decode_cp1251_utf8_latin1(t))
except EOFError:
    print()
