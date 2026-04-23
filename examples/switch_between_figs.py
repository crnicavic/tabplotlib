
from tabplotlib import Tabplot
import matplotlib.pyplot as plt

import numpy as np

tp = Tabplot("test")

tp.add_plot("tab1")
t = np.arange(0, 5, 0.01);
y = np.sin(2*np.pi*t)
plt.plot(t, y)

tp.add_plot("tab2")
plt.subplot(211)
plt.plot(t, y)
plt.subplot(212)
plt.plot(y, t)

plt.figure("tab1")
y=np.cos(2*np.pi*t)
plt.plot(t, y)

tp.show()
