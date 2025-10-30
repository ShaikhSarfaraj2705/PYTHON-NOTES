import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()

diabetes_X = np.array([[1], [2], [3]])

diabetes_X_train = diabetes_X
diabetes_X_test = diabetes_X

diabetes_y_train = np.array([3,2,4])
diabetes_y_test = np.array([3,2,4])

model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = model.predict(diabetes_X_test)

print("mean squared error:", mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("weighted value (m):", model.coef_)
print("intercept (b):", model.intercept_)

plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
plt.show()