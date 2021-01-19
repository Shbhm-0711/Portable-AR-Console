inp = "a12204b7428c9896d-602e-399f-475g3220742541h"
a = inp.index("a")
b = inp.index("b")
c = inp.index("c")
d = inp.index("d")
e = inp.index("e")
f = inp.index("f")
g = inp.index("g")
h = inp.index("h")

Ax = int(inp[a+1:b])
Ay = int(inp[b+1:c])
Az = int(inp[c+1:d])

Gx = int(inp[d+1:e])
Gy = int(inp[e+1:f])
Gz = int(inp[f+1:g])

id = int(inp[g+1:h])

processed = [id,Ax,Ay,Az,Gx,Gy,Gz]

print(processed)

