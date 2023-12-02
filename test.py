class Obj:
    def __init__(self) -> None:
        pass

def a(obj: Obj) -> bool:
    return obj


x = None
s = Obj()

print(a(x))
print(a(s))