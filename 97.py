x = 1
p = 1
i = 0
for i in xrange(7830457):
    x = (2*x)%10000000000

x = x*28433 + 1
x = str(x)[-10:]
print x
