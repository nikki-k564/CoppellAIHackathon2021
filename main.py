import matplotlib.pyplot as plot
from scipy import stats

x = []
y = []

print("LINEAR REGRESSION CALCULATOR")
numData = int(input("How many coordinates are being entered: "))

for i in range(numData): 
  print("Coordinate %d" % (i+1))
  xVal = int(input("x-coordinate: "))
  yVal = int(input("y-coordinate: "))

  x.append(xVal)
  y.append(yVal)

print("Your linear regression line has been created")

slope, intercept, r, p, error = stats.linregress(x, y)

print()
print("LINEAR REGRESSION INFORMATION: ")
print("Slope: %f" % slope)
print("Y-Intercept: %f" % intercept)
print("R-value: %f" % r); 
print("Standard Error: %f" % error)

def calculateYCoor(x): 
  return slope * x + intercept

graph = list(map(calculateYCoor, x))

plot.scatter(x, y)
plot.plot(x, graph)
plot.show()
