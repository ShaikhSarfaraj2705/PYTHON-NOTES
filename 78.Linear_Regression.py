import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes = datasets.load_diabetes()
# print(diabetes.keys())
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

# diabetes_X = diabetes.data[:, np.newaxis, 2]
diabetes_X = diabetes.data

diabetes_X_train = diabetes_X[:-30]
diabetes_X_test = diabetes_X[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = model.predict(diabetes_X_test)

print("mean squared error:", mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("weighted value (m):", model.coef_)
print("intercept (b):", model.intercept_)

# plt.scatter(diabetes_X_test, diabetes_y_test, color='black')
# plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)
# plt.show()
# mean squared error: 3035.060115291269
# weighted value (m): [941.43097333]
# intercept (b): 153.39713623331644