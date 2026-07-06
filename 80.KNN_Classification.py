from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# loading datasets
iris= datasets.load_iris()
features= iris.data
labels= iris.target

# # printing description and features
# print(iris.DESCR)
# print(features[0] , labels[0])

# training the classifier
clf= KNeighborsClassifier()
clf.fit(features, labels)

preds=clf.predict([[5.1, 3.5, 1.4 ,0.2]])
print(preds) 