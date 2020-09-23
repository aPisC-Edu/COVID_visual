import numpy as np

def LR(x, y, x2):
  p = np.polyfit(x, y[:x.shape[0]], 1)
  return p[0] * x2 + p[1]