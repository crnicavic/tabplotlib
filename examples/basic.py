from tabplotlib import Tabplot
import matplotlib.pyplot as plt

import numpy as np


t = np.arange(0, 5, 0.01);
y = np.sin(2*np.pi*t)

# initialize the object
tp = Tabplot("test")

# add a tab
tp.add_plot("tab1")
# use matplotlib normally
plt.plot(t, y)

# create new tab
tp.add_plot("tab2")
# use normally!
plt.subplot(211)
plt.plot(t, y)
plt.subplot(212)
plt.plot(y, t)

# display the window
tp.show()
