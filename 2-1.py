from mip import Model, maximize, minimize, xsum

m = Model()
a = m.add_var('a')
b = m.add_var('b')
c = m.add_var('c')
m.objective = maximize (150*a+200*b+300*c)
m += 3*a+b+2*c <= 60
m += a+3*b <= 36
m += 2*b+4*c <= 48  

m.optimize()
print(a.x)
print(b.x)
print(c.x)