from ScubaTank import ScubaTank

t = ScubaTank("A", 80)
print(t)
t.fill(40)
print(t.get_bar())
t.set_bar(250)
print(t)
t.set_bar(400)
print(t.get_bar())
t.release(0)
t.release(300)
t.release(50)
print(t)

src = ScubaTank("A", 150)
dst = ScubaTank("B", 20)
transfer_air(src, dst, 50)
print(src)
print(dst)
print(src.get_bar())
print(dst.get_bar())


