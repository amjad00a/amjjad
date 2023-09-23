import pandas as pd
df=pd.read_csv("diabetes.csv")
X=df.drop(columns=['Outcome'])
Y=df['Outcome']
X_train=X[:X.shape[0]-100]
Y_train=Y[:Y.shape[0]-100]
X_test=X[X.shape[0]-100:]
Y_test=Y[Y.shape[0]-100:]
print(X_train.shape)
print(Y_train.shape)
print(X_test.shape)
print(Y_test.shape)


