a = int(raw_input("a"))
b = int(raw_input("b"))
c = int(raw_input("c"))
d = int(raw_input("d"))
e = int(raw_input("e"))
area = c*a*2 + c*b*2 + a*b*2 + d*8*(b-e-e+c-e-e+a-e-e)
V = a*b*c-d*((a-e-e)*(c-e-e)+(a-e-e)*(b-e-e)+(b-e-e)*(c-e-e))*2
print area, V