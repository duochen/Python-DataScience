import functions as f

xval = [x/3.0 for x in range(-10, 10)]
yval1 = [f.sinc(x) for x in xval]
yval2 = [f.step(x) for x in xval]

print("xval: ", xval)
print("yval1:", yval1)
print("yval2:", yval2)