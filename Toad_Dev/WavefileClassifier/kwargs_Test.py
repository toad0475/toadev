def test(*args):
    for p in args:
        print(p[0])

a = 1
b = 2
c = 3
test((a,"aaa"), (b,"bbb"),(c,"ccc"))