div = 1

def modulu( bla ):
    for i in range(1,21):
        if bla % i != 0:
            return False
    return True

while True:
    if not modulu(div):
        div = div + 1
    else:
        print(div)
        break
