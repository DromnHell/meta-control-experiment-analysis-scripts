#!/usr/bin/env python3
#encoding: utf-8

# ---------------------------------------------------------------------------
# IMPORT
# ---------------------------------------------------------------------------
import matplotlib.pyplot as plt
import math
import numpy as np
# ---------------------------------------------------------------------------

x = np.arange(-3, 0.1, 0.1)
y = [math.exp(i) for i in x]
y10 = [10*math.exp(i) for i in x]

fig = plt.figure()
plt.plot(x , y, c = "red", label = "Exp entropy")
plt.plot(x , y10, c = "blue", label = "Exp entropy * 2")
plt.grid(linestyle='--')
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xticks(np.arange(-3, 0.1, 0.1))
plt.legend()
plt.show()


