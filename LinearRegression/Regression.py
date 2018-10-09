import numpy as np
import matplotlib.pyplot as  plot
import pandas as panda

x = np.arange(0,10,0.1)
y = 1 + (x*2) + (np.random.normal(0,1,len(x)) *5)

mx = x.mean()
my = y.mean()

temp  = x- mx
print(mx)
c1 = np.sum(temp * (y - my)) / np.sum(temp**2)
c0 = my - c1*mx

x2 = [0, 10]
y2 = [c0 + c1*0, c0 + c1*10]

my_dpi = 96

plot.figure(figsize=(800/my_dpi, 800/my_dpi), dpi = my_dpi)

plot.scatter(x,y, color='b', s = 20) #data
plot.plot(x2, y2, color='r', linewidth=5 ) #line

plot.axis([0,10,-5,30])

plot.xlabel('X')
plot.ylabel('Y')

plot.show()