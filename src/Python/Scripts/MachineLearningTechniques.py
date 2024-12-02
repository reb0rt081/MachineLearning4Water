from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd


def LinearModel(x, y):
  """returns fit linear model from sklearn"""
  
  
  if x.shape[0] != y.shape[0]:
    raise ValueError("The number of samples in X and y must be the same.")  
  model = LinearRegression()
  model.fit(x, y)
  return model

def LinearModelParams(x,y):

  """returns slope and intercept for linear estimator"""
  if x.shape[0] != y.shape[0]:
    raise ValueError("The number of samples in X and y must be the same.")  
  model = LinearRegression()
  model.fit(x, y)
  slope = model.coef_
  intercept = model.intercept_
  return slope, intercept
  
