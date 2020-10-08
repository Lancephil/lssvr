import numpy as np
import pandas as pd
from lssvr import LSSVR

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


data = pd.read_csv("mycycle.csv") 

X = data['input'].values.reshape(-1,1)
y = data['output'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LSSVR(kernel='rbf', gamma=2**-4)

model.fit(X_train, y_train)
y_hat = model.predict(X_test)
print(mean_squared_error(y_test, y_hat))

plt.plot(X, y, '.r', alpha=0.5)
plt.plot(X, model.predict(X), '-b')
plt.show()