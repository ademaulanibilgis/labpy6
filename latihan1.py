#mengubah kode def menjadi lambda

a = lambda x : x ** 2
print(a(4))

b = lambda x, y : x ** 2  + y ** 2
print(b(9,2))

c = lambda *args : sum(args)/len(args)
print(c(10,20,30))

d = lambda s: "".join(set(s))
print(d("dipo"))
