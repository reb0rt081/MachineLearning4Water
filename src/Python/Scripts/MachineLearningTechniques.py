from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression



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

def KMeansModel(clusters, x, **kwargs):
    """
    Returns a fitted KMeans model.
    
    Parameters:
    clusters (int): Number of clusters.
    x (array-like): Input data to cluster.
    **kwargs: Additional keyword arguments for sklearn's KMeans.
    
    Returns:
    KMeans: Fitted KMeans model.
    """
    model = KMeans(n_clusters=clusters, **kwargs)
    model.fit(x)
    return model


def KMeansParams(clusters, x, **kwargs):
    """
    Fits a KMeans model and returns cluster centers, labels, and inertia.
    
    Parameters:
    clusters (int): Number of clusters.
    x (array-like): Input data to cluster.
    **kwargs: Additional keyword arguments for sklearn's KMeans.
    
    Returns:
    tuple: (cluster_centers, labels, inertia)
    """
    model = KMeans(n_clusters=clusters, **kwargs)
    model.fit(x)
    return model.cluster_centers_, model.labels_, model.inertia_

def LogisticRegressionModel(x, y, **kwargs):
    """
    Fits a Logistic Regression model and returns the model itself.
    
    Parameters:
    x (array-like): Feature matrix.
    y (array-like): Target values.
    **kwargs: Additional keyword arguments for sklearn's LogisticRegression.
    
    Returns:
    LogisticRegression: The fitted Logistic Regression model.
    """
    model = LogisticRegression(**kwargs)
    model.fit(x, y)
    return model


def LogisticRegressionParams(x, y, **kwargs):
    """
    Fits a Logistic Regression model and returns coefficients and intercept.
    
    Parameters:
    x (array-like): Feature matrix.
    y (array-like): Target values.
    **kwargs: Additional keyword arguments for sklearn's LogisticRegression.
    
    Returns:
    tuple: (coefficients, intercept)
    """
    model = LogisticRegression(**kwargs)
    model.fit(x, y)
    return model.coef_, model.intercept_
