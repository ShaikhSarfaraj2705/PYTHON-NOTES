#MATPLOTLIB:Matplotlib is a widely-used Python library used for creating static, animated and interactive data 
#visualizations. It is built on the top of NumPy and it can easily handles large datasets for creating various types
#of plots such as line charts, bar charts, scatter plots, etc.

#1.Line Chart:Line chart is one of the basic plots and can be created using plot() function.
import matplotlib.pyplot as plt
x=[10,20,30,40]
y=[20,25,35,55]
plt.plot(x,y)
plt.title("line chart")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()


#2.Bar Chart:Bar chart displays categorical data using rectangular bars whose lengths are proportional to the values
#they represent.
plt.bar(x,y)
plt.title("bar chart")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()

#3.Histogram:Histogram shows the distribution of data by grouping values into bins.The hist() function is used.
z = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]
plt.hist(z,bins=10, color="red")        #Bins: Number of groups (bins) to divide data into
plt.title("histogram chart")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()

#4.Scatter Plot:Scatter plots are used to observe relationships between variables.The scatter() methodis used.
x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190, 160, 130, 240, 200]
plt.scatter(x,y)
plt.title("scatter")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()

#5.Pie Chart:Pie chart is a circular chart used to show data as proportions or percentages.It is created using the pie().
plt.pie(y,labels=x)
plt.title("pie chart")
plt.show()

#6.Box Plot:Box plot is a simple graph that shows how data is spread out.It displays the minimum, maximum, median 
#and quartiles and also helps to spot outliers easily.
data=[[10,20,30,40],
      [15,25,35,45],
      [8,16,24,32]]
plt.boxplot(data)
plt.title("box plot")
plt.ylabel("groups")
plt.xlabel("values")
plt.show()

#7. Heatmap:Heatmap is a graphical representation of data where values are shown as colors.It helps visualize 
#patterns, correlations or intensity in a matrix-like format.It is created using imshow() method in Matplotlib.
import numpy as np

np.random.seed(0)
data = np.random.rand(10, 10)
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Heatmap')
plt.show()