# MATPLOTLIB CORE COMPONENT
# 1.Figure class
# The Figure class represents the full drawing area or canvas that can hold one or more plots.It is created using
# the figure() function and lets user control the overall size, layout and background of the plot window.
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 5), facecolor='lightblue')
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]
ax.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()
print("_________________________________________________________________________________")  

# 2.Axes class
# Axes class represents actual plotting area where data is drawn.A single figure can contain multiple axes but each 
# Axes object belongs to only one figure. It can create an Axes object using axes() function.
from matplotlib.figure import Figure
x = [10, 20, 30, 40]
y = [20, 25, 35, 55]
fig = plt.figure(figsize=(5, 4))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
ax.plot(x, y)
ax.plot(y, x)
ax.set_title("Linear Graph")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend(labels=('line 1', 'line 2'))
plt.show()
print("_________________________________________________________________________________")  

#ADVANCED TECHNIQUES FOR DATA VISUALIZATIONS:
#1.Using add_axes()
# add_axes() method allows us to manually add axes to a figure in Matplotlib.It takes a list of four values 
# [left, bottom, width, height] to specify the position and size of the axes.
fig = plt.figure(figsize=(10, 4)) 
ax1 = fig.add_axes([0.1, 0.1, 0.35, 0.8]) 
ax2 = fig.add_axes([0.55, 0.1, 0.35, 0.8])

ax1.plot(x, y)
ax2.plot(y, x)
plt.show()
print("_________________________________________________________________________________")  

# 2.Using subplot()
# The subplot() method adds a plot to a specified grid position within the current figure.It takes three arguments:
# the number of rows, columns and plot index.
plt.figure()
plt.subplot(121)
plt.plot(x, y)

plt.subplot(122)
plt.plot(y, x)
plt.show()
print("_________________________________________________________________________________")  

# 3.Using subplot2grid()
# The subplot2grid() creates axes object at a specified location inside a grid and also helps in spanning the axes
# object across multiple rows or columns.
axes1 = plt.subplot2grid ((7, 1), (0, 0), rowspan = 2, colspan = 1)

axes2 = plt.subplot2grid ((7, 1), (2, 0), rowspan = 2, colspan = 1)

axes1.plot(x, y)
axes2.plot(y, x)
plt.show()
print("_________________________________________________________________________________")  

# SAVING PLOT USING savefig()
# When plots are created using Matplotlib,users may want to save them as image files for use in reports,
# presentations or sharing.Matplotlib offers savefig() function to save the current plot to a file.By changing file 
# extension,users can store the plot in different formats such as .png, .jpg, .pdf or .svg.
year = ['2010', '2002', '2004', '2006', '2008']
production = [25, 15, 35, 30, 10]
plt.bar(year, production)
plt.savefig("71.output.jpg")
plt.savefig("71.output1.jpg", facecolor='y', bbox_inches="tight",pad_inches=0.3, transparent=True)