# Auto regression model fitting

from statsmodels.tsa.ar_model import AutoReg
import numpy as np

def AR(x, y, x2):
  lag = 7;
  # fit model
  model = AutoReg(y, lags=lag)
  model_fit = model.fit()
  # make prediction
  yhat = model_fit.predict(0, len(y) + len(x2))
  return np.concatenate([np.zeros(lag-1), yhat])