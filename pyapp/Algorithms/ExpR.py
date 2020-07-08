import numpy as np
import math

def ExpR(x, y, x2):
  y2 = np.log(y)
  p = np.polyfit(x, y2, 1)
  return math.exp(p[1]) * np.exp(x2 * p[0])