from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd


def LinearModelNP(x: np.ndarray, y:np.ndarray)->LinearRegression:
  """toma como entradas los datos x e y en formato numpy y retorna un modelo lineal sklearn"""
  
  
  if x.shape[0] != y.shape[0]:
    raise ValueError("The number of samples in X and y must be the same.")  
  model = LinearRegression()
  model.fit(x, y)
  return model

def LinearModelPD(x: pd.DataFrame, y:pd.Series)->LinearRegression:
  """toma como entradas los datos x e y en formato pandas y retorna un modelo lineal"""

  if x.shape[0] != y.shape[0]:
    raise ValueError("The number of samples in X and y must be the same.")
  model = LinearRegression()
  model.fit(x,y)
  return model
