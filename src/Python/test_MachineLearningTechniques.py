import MachineLearningTechniques as ML

# model tests for libs

def test_LinearModelParams():
  x = [1,2,3,4]
  y= [1,2,3,4]
  slope,intercept = ML.LinearModelParams(x,y)
  assert slope==1
  assert intercept==0

def test_KMeansParams():
  x=[1,2,2,3,6,7,8,9]
  clusters = 2
  centers,labels,inertia = ML.KMeansParams(clusters,x)
  assert abs(centers[0]-2)<0.1
  assert abs(centers[1]-7.5)<0.1
  assert labels == [0,0,0,0,1,1,1,1]
  assert abs(inertia-7)<0.1

def test_LogisticRegressionParams():
  x=[1,2,3,4,5,6]
  y=[0,0,0,1,1,1]
  coeff, intercept = ML.LogisticRegressionParams(x,y)
  assert abs(coeff-1.1206)<0.1
  assert abs(intercept+3.9221)<0.1

def test_SVCModel():
  x=[1,2,3,4,5,6]
  y=[0,0,0,1,1,1]
  model = ML.SVCModel(x,y)
  assert abs(model.coef_-1)<0.1
  assert abs(mofel.intercept_+3.5)<0.1

def test_KNNModel():
  x=[1,2,3,4,5,6]
  y=[0,0,0,1,1,1]
  model = ML.KNNModel(x,y,n_neighbors=3)
  assert model.predict([2.5])==0
  assert model.predict([6])==1