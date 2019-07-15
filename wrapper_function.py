def check(func):
    def inside(a, b):
        if b == 0:
            print("b cant zero")
            return
        func(a, b)
    return inside


@check
def div(a, b):
    return a / b

print(div(10, 0))