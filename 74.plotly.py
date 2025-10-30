#PLOTLY:It helps users to explore data through features like zooming,additional details and clicking for deeper insights.It handles the interactivity 
#with JavaScript behind the scenes so that we can focus on writing Python code to build the charts.
import plotly.express as px
fig = px.line(x=[1, 2], y=[3, 4])
fig.show()
print("_________________________________________________________________________________")

# 1.line chart:It can be created using the px.line() method with each data position is represented as a vertex of a polyline mark in 2D space.
df=px.data.iris()
fig=px.line(df,y="sepal_width",line_dash='species',line_group='species',color='species')
fig.show()
# data_frame: Dataset to plot.
# x: Column name for the X-axis.
# y: Column name for the Y-axis.
# color: Color the lines based on this column.
# title: Title of the plot.
print("_________________________________________________________________________________")

# 2.bar plot:
df = px.data.tips()
fig = px.bar(df, x='day', y="total_bill")
fig.show()
print("_________________________________________________________________________________")

df = px.data.tips()
fig = px.bar(df, x='day', y="total_bill", color='sex',facet_row='time', facet_col='sex')
fig.show()
# color: Used to color the bars.
# facet_row: Divides the graph into rows according to the data passed
# facet_col: Divides the graph into columns according to the data passed
print("_________________________________________________________________________________")

#3.scatter plot:
fig = px.scatter(df, x='total_bill', y="tip")
fig.show()
print("_________________________________________________________________________________")

# color: Color the points.
# symbol: Gives a symbol to each point according to the data passed.
# size: Size for each point.
fig = px.scatter(df, x='total_bill', y="tip", color='time',symbol='sex', size='size', facet_row='day',facet_col='time')
fig.show()
print("_________________________________________________________________________________")

# 4.histogram
fig = px.histogram(df, x="total_bill")
fig.show()
print("_________________________________________________________________________________")

# nbins: Set the number of bins.
# histnorm: Normalize the histogram (e.g"percent", "density").
# barmode:group: Bars are stacked above zero for positive values and below zero for negative values
                #overlay: Bars are drawn on the top of each other
                #group: Bars are placed beside each othe
fig = px.histogram(df, x="total_bill", color='sex',nbins=50, histnorm='percent',barmode='overlay')
fig.show()
print("_________________________________________________________________________________")

# 5.pie chart
# names: Column name for the pie chart labels.
# values: Column name for the size of the slices.
# hole: Creates a donut chart when set between 0 and 1.
# color_discrete_sequence: Strings defining valid CSS colors
# opacity: It finds how transparent or solid the markers (such as points on a scatter plot) appear. The value should be between 0 and 1
fig = px.pie(df, values="total_bill", names="day")
fig.show()
print("_________________________________________________________________________________")

fig = px.pie(df, values="total_bill", names="day",color_discrete_sequence=px.colors.sequential.RdBu,opacity=0.7, hole=0.5)
fig.show()
print("_________________________________________________________________________________")

