# SEABORN:Seaborn is a popular Python library Built on Matplotlib for creating attractive statistical visualizations 
# and integrated with Pandas.

# 1.Line Plot
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {'Name': ['ANSH', 'SAHIL', 'JAYAN', 'ANURAG'], 'Age': [21, 23, 20, 24]}
df = pd.DataFrame(data)
sns.lineplot(x='Name', y='Age', data=df) #x, y: Numeric input variables. 
# plt.xlabel('Index')                           These can be arrays, lists or column names from a DataFrame.
plt.ylabel('Age')                        #data: DataFrame containing the data.
plt.title('Age Line Plot')
plt.show()

# 2.Scatter Plot
sns.scatterplot(x='Name', y='Age', data=df)
plt.show()

# 3.Box Plot
sns.boxplot(y='Age', data=df)
plt.show()

# 4.Violin Plot:A violin plot is similar to a boxplot. It shows several quantitative data across one or more 
# categorical variables such that those distributions can be compared.
sns.violinplot(y='Age', data=df)
plt.show()

# 5.Swarm Plot:A swarm plot displays individual data points without overlap along a categorical axis which provides
# a clear view of distribution density.
sns.swarmplot(x=df.index, y='Age', data=df)
plt.show()

# 6.Bar plot
sns.barplot(x='Name', y='Age', data=df)
plt.show()

# 7.Point Plot:Point plot show point estimates and confidence intervals using scatter glyphs which represents the
# central tendency of a numeric variable.
sns.pointplot(x='Name', y='Age', data=df)
plt.show()

# 8.Count plot:A Count plot displays the number of occurrences of each category using bars to visualize the 
# distribution of categorical variables.
sns.countplot(x='Name', data=df)
plt.title("Frequency of Names")
plt.show()

# 9.KDE Plot:KDE Plot (Kernel Density Estimate) is used for visualizing the Probability Density of a continuous 
# variable at different values in a continuous variable.We can also plot a single graph for multiple samples which
# helps in more efficient data visualization.
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['Species'] = iris.target
df['Species'] = df['Species'].map({ 0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})
sns.kdeplot(data=df[df['Species'] == 'Virginica'], x='sepal length (cm)', fill=True, label='Virginica')
plt.legend()
plt.show()