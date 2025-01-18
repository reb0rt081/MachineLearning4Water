from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, mean_squared_error, mean_absolute_error, r2_score
from sklearn.base import is_classifier
from sklearn.linear_model import Ridge
from sklearn.neural_network import MLPRegressor

#Models
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
    return model.cluster_centers_.flatten(), model.labels_, model.inertia_

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


def SVCModel (x,y,**kwargs):
  """Takes x and y as array-like inputs and returns a SVC classifier"""

  model = SVC(**kwargs)
  model.fit(x,y)
  
  return model



def KNNModel (x,y,**kwargs):
  """Takes x and y as array-like inputs and outputs a KNN classifier"""

  model=KNeighborsClassifier(**kwargs)
  model.fit(x,y)
  return model

#Model Eval

def RidgeRegressionModel (x,y, alpha, **kwargs):
  """takes x and y as array like object and outputs a RR model"""

  model = Ridge(alpha = alpha, **kwargs)
  model.fit(x,y)
  return model
  #
  
def evaluate_basic_metrics(model, X_test, y_test):
    """
    Evaluates basic metrics of a given model (classifier or regressor).
    
    Parameters:
    - model: Trained model (classifier or regressor)
    - X_test: Test data (features)
    - y_test: True labels/values (target)
    
    Returns:
    - Dictionary of basic evaluation metrics
    """
    metrics = {}

    # Check if the model is a classifier
    if is_classifier(model):
        # Predictions for classification models
        y_pred = model.predict(X_test)
        
        # Basic classification metrics
        metrics['accuracy'] = accuracy_score(y_test, y_pred)
        metrics['precision'] = precision_score(y_test, y_pred, average='macro', zero_division=0)
        metrics['confusion_matrix'] = confusion_matrix(y_test, y_pred)
    
    else:
        # Predictions for regression models
        y_pred = model.predict(X_test)
        
        # Basic regression metrics
        metrics['mean_squared_error'] = mean_squared_error(y_test, y_pred)
        metrics['mean_absolute_error'] = mean_absolute_error(y_test, y_pred)
        metrics['r2_score'] = r2_score(y_test, y_pred)
    
    return metrics


def NeuralNetworkRegressor(x,y,**kwargs):
  model = MLPRegressor(**kwargs).fit(x,y)
  return model
