from sklearn import datasets

iris= datasets.load_iris()

print(iris.DESCR)
features= iris.data
labels= iris.target
print(features[0] , labels[0])