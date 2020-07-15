# Auto regression model fitting
# https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/

from statsmodels.tsa.arima_model import ARMA
import numpy as np

def MA(x, y, x2):
  lag = 1;
  # fit model
  model = ARMA(y, order=(2,1))
  model_fit = model.fit(disp=False)
  # make prediction
  yhat = model_fit.predict(0, len(y) + len(x2) -1)
  return np.concatenate([np.zeros(lag-1), yhat])