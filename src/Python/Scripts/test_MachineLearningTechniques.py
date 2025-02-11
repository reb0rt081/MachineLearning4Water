import MachineLearningTechniques as ML
import numpy as np
# model tests for libs

def test_LinearModelParams():
  x_nat = [[1],[2],[3],[4]]
  y_nat= [1,2,3,4]
  x=np.array(x_nat)
  y=np.array(y_nat)
  slope,intercept = ML.LinearModelParams(x,y)
  assert slope[0]==1
  assert intercept==0

def test_KMeansParams():
  x=[[1],[2],[2],[3],[6],[7],[7],[8]]
  clusters = 2
  centers,labels,inertia = ML.KMeansParams(clusters,x)
  centers = np.sort(centers)
  assert abs(centers[0]-2)<0.1
  assert abs(centers[1]-7)<0.1
  assert abs(inertia-4.0)<0.1

def test_LogisticRegressionParams():
  x=[[1],[2],[3],[4],[5],[6]]
  y=[0,0,0,1,1,1]
  coeff, intercept = ML.LogisticRegressionParams(x,y)
  assert abs(coeff-1.1206)<0.1
  assert abs(intercept+3.9221)<0.1

def test_SVCModel():
  x=[[1],[2],[3],[4],[5],[6]]
  y=[0,0,0,1,1,1]
  model = ML.SVCModel(x,y,kernel='linear')
  assert abs(model.coef_-1)<0.1
  assert abs(model.intercept_+3.5)<0.1

def test_KNNModel():
  x=[[1],[2],[3],[4],[5],[6]]
  y=[0,0,0,1,1,1]
  model = ML.KNNModel(x,y,n_neighbors=3)
  assert model.predict([[2.5]])==0
  assert model.predict([[6]])==1
