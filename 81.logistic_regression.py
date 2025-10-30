# train a logistic  regression classifier to predict whether a flower is iris virginica or not
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np

iris=datasets.load_iris()
# print(list(iris.keys()))
# print(iris['DESCR'])
# print(iris['data'].shape)
# print(iris['target'])

x=iris['data'][:, 3:]  # petal width
y=(iris['target']==2).astype(int)  # 1 if iris virginica, else 0

# training the logistic regression classifier
clf=LogisticRegression()
clf.fit(x, y)

preds=clf.predict([[1.7], [1.5], [0.2]])
print(preds)  # expect [1, 1, 0]

# using matplotlib to visualize the results
import matplotlib.pyplot as plt
x_new=np.linspace(0, 3, 1000).reshape(-1, 1)
y_proba=clf.predict_proba(x_new)

plt.plot(x_new, y_proba[:, 1], "g-", label="Iris virginica")
plt.plot(x_new, y_proba[:, 0], "b--", label="Not Iris virginica")
plt.xlabel("Petal width (cm)")
plt.ylabel("Probability")
plt.legend()
plt.show()