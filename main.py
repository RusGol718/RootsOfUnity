import matplotlib.pyplot as plt
import numpy as np
import cmath 

try:
	n_polygon = int(input("Please enter the number of sides you want for a regular pollygon\n"))
except:
	print("Sorry, couldn't get your answer. Number of sides is set to 3")
	n_polygon = 3
try:
	phase = float(input("Please enter the phase in radians on the amount of rotation of the polygon\n"))
except:
	print("Sorry, couldn't get your answer. Extra phase for rotation is set to 0")
	phase = 0
try:
	length = float(input("Please enter the length between the points (0, 0) and vertex of the polygon\n"))
except:
	print("Sorry, couldn't get your answer. Length is set to 0")
	length = 1
p = complex(length*cmath.cos(phase), length*cmath.sin(phase)) #p for phase

z = [complex(abs(p)*cmath.cos((phase + cmath.tau*k)/n_polygon), abs(p)*cmath.sin((phase + cmath.tau*k)/n_polygon)) for k in range(0, n_polygon+1)]
#Creating the numbers

x = np.array([x.real for x in z]) #Real
y = np.array([y.imag for y in z]) #Imaginary

plt.xlim(-1.35*abs(p), 1.35*abs(p)) #Scaling x-axis
plt.ylim(-1.125*abs(p), 1.125*abs(p)) #Scaling y-axis

for re, im in zip(x, y):
	if re == 1.0 and im == 0.0:
		continue
	else:
		plt.text(re, im, f"({re:.3f}, {im:.3f})", color="midnightblue") #Writing coodinates

plt.ylabel("Im axis")
plt.xlabel("Re axis")

plt.axhline(color='black', lw=0.5)
plt.axvline(color='black', lw=0.5)

plt.scatter(x, y)
plt.plot(x, y)
plt.show() #Plotting the polygon
