def travel(n):
    for _ in range(n):
        yield "по кочкам"
    return "и в яму"

def travelwrap(n):
    result = yield from travel(n)
    yield result

for msg in travelwrap(5):
    print(msg)

