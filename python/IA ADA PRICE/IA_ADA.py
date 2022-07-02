
import numpy as np 
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
 
#x= [0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,136,140]
#y= [5,10,14,19,24,28,33,38,42,47,52,56,61,65,70,74,78,82,84,87,89,90,92,93,94,95,96,97,97,98,98,98,99,99,99,100]
#tiempo = [0,4,8,12,14,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80,84,88,92,96,100,104,108,112,116,120,124,128,132,135,136,150,170,173]
#nota = [0,0,0.5,0.5,6.7,1,1,2.2,3,2,2.8,3.5,3.7,4,5,5.5,6,3,6,6,6,7,7.2,8,6.9,7,7.4,7.5,7,8,8.2,8.5,4.2,9,4.3,7.2,2,9.3,7,10]
tiempo = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80]
nota = [1.090,1.088,1.089,1.089,1.090,1.090,1.091,1.091,1.091,1.092,1.092,1.093,1.093,1.092,1.092,1.093,1.093,1.093,1.094,1.093,1.094,1.094,1.094,1.093,1.092,1.093,1.093,1.093,1.094,1.094,1.093,1.093,1.092,1.092,1.094,1.094,1.093,1.094,1.094,1.093]
 
x = tiempo
y = nota
 
x = mean_data = np.array(x)
X=x[:,np.newaxis]
 
while True:
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    mlr=MLPRegressor(solver="lbfgs",alpha=1e-5,hidden_layer_sizes=(3,3), random_state=1)
    mlr.fit(X_train, y_train)
    print(mlr.score(X_train, y_train))
    if mlr.score(X_train,y_train) > 0.75:
        break

timess = 120
print("BASANDONOS EN PRECIOS HISTORICOS EL ADA A LOS "+str(timess)+" SEGUNDOS ESTARÁ A: ")
print(mlr.predict(np.array(timess).reshape(1, 1)))
#print(mlr.predict(np.array(73).reshape(1, 1)))

