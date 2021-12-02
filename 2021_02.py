import sys

lines = open(sys.argv[1]).readlines()

a = h = f = 0
for c,n in [(x[0], int(x.split()[1])) for x in lines]:
	if c == 'f':
		h += n*a
		f += n
	else:
		a += n if c == 'd' else -n

print("Part 1: {:d}".format(a*f))
print("Part 2: {:d}".format(h*f))
