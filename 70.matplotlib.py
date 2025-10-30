# CUSTOMIZE MATPLOTLIB VISUALIZATIONS:

# 1.line chart
# Color: Change the color of the line
# Linewidth: Adjust the width of the line
# Marker: Change the style of plotted points
# Markersize: Change the size of the markers
# Linestyle: Define the style of the line like solid, dashed, etc.
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]
plt.plot(x,y, color="yellow",linewidth=3,marker='o',markersize=15,linestyle='--')
plt.plot(y,x)
plt.title("Line Chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
print("_________________________________________________________________________________")

# 2.Bar chart:x
# Color: Fill color of the bars
# Edgecolor: Color of the bar edges
# Linewidth: Thickness of the edges
# Width: Width of each bar
plt.bar(x,y,color='purple',edgecolor='black',linewidth=2)
plt.title("Line Chart")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
print("_________________________________________________________________________________")

# 3.Histogram plot
# Bins: Number of groups (bins) to divide data into
# Color: Bar fill color
# Edgecolor: Bar edge color
# Linestyle: Style of the edges like solid, dashed, etc.
# Alpha: Transparency level (0 = transparent, 1 = opaque)
z = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]
plt.hist(z,bins=10, color="grey",edgecolor='blue',linestyle='--',alpha=0.5)        #Bins: Number of groups (bins) to divide data into
plt.title("histogram chart")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
print("_________________________________________________________________________________")

# 4.Scatter plot
# S: Marker size (single value or array)
# C: Color of markers or sequence of colors
# Marker: Marker style like circle, diamond, etc.
# Linewidths: Width of marker borders
# Edgecolor: Color of marker borders
# Alpha: Blending value, between 0 (transparent) and 1 (opaque)
x = ['Thur', 'Fri', 'Sat', 'Sun', 'Thur', 'Fri', 'Sat', 'Sun']
y = [170, 120, 250, 190, 160, 130, 240, 200]
size = [2, 3, 4, 2, 3, 2, 4, 3]  
bill = [170, 120, 250, 190, 180, 130, 260, 200] 
plt.scatter(x,y,c=size,s=bill,marker='D',alpha=0.5)
plt.title("scatter")
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()
print("_________________________________________________________________________________")

# 5.pie chart:
# Explode: Moving the wedges of the plot
# Autopct: Label the wedge with their numerical value.
# Color: Colors of the slices
# Sadow: Used to create a shadow effect
explode = [0.1, 0.5, 0, 0, 0,0,0,0]
colors = ( "orange", "cyan", "yellow","grey", "green","purple","white","pink")
plt.pie(y,labels=x,explode=explode, autopct='%1.2f%%',colors=colors, shadow=True)
plt.title("pie chart")
plt.show()
print("_________________________________________________________________________________")