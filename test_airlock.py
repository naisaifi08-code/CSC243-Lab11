from Airlock import Airlock

a = Airlock("H1")
print(a)
a.seal()
print(a.is_sealed())
a.seal()
a.unseal()
print(a)
a.unseal()
