import numpy as np
import math

def GaussR(x, y, x2):
  y2 = np.log(y)
  p = np.polyfit(x[:y.shape[0]], y2, 2)

  gc = p[0]
  gb = -p[1]/ (2*p[0])
  ga = math.exp(p[2] - p[1] * p[1] / (4 * p[0]) )

  return ga * np.exp(np.power(x2 - gb, 2) * gc )