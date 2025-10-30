#IMPLEMENTING INTERACTIVE FEACTURE IN PLOTLY:Plotly provides various interactive features which allows users to zoom,hover and click for deeper 
# insights.Beyond these built-in interactions it allows customization with tools like dropdown menus,buttons and sliders.These can be added using 
# the update menu attribute in the plot layout. 

# 1.dropdown menu:A drop-down menu allows users to select different options to modify the chart.The update method is used to control the chart 
# based on dropdown choices.In plotly there are 4 possible methods to modify the charts by using update menu method.
# restyle: modify data or data attributes
# relayout: modify layout attributes
# update: modify data and layout attributes
# animate: start or pause an animation
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd

df = px.data.tips()
plot = go.Figure(data=[go.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',)
])
plot.update_layout(
    updatemenus=[
        dict(buttons=list([
            dict(
                args=["type", "scatter"],
                label="Scatter Plot",
                method="restyle"
            ),
            dict(
                args=["type", "bar"],
                label="Bar Chart",
                method="restyle"
            )
        ]),
            direction="down",
        ),
    ]
)
plot.show()
print("_________________________________________________________________________________")

# 2.adding buttons:

plot = go.Figure(data=[go.Scatter(
    x=df['day'],
    y=df['tip'],
    mode='markers',)
])
plot.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            direction="right",
            buttons=list([
                dict(
                    args=["type", "scatter"],
                    label="Scatter Plot",
                    method="restyle"
                ),
                dict(
                    args=["type", "bar"],
                    label="Bar Chart",
                    method="restyle"
                )
            ]),
        ),
    ]
)
plot.show()
print("_________________________________________________________________________________")

# 3.creating sliders and selector to the plot
import plotly.graph_objects as px
import plotly.express as go
import numpy as np
df = go.data.tips()
x = df['total_bill']
y = df['tip']
plot = px.Figure(data=[px.Scatter(
    x=x,
    y=y,
    mode='markers',)
])
plot.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                    step="day",
                    stepmode="backward"),
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
    )
)
plot.show()
print("_________________________________________________________________________________")

#BUILDING INTERACTIVE DASHBOARDS WITH PLOTLY DASH
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 15, 13, 17, 14]
})
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure=px.scatter(df, x='x', y='y', title='Scatter Plot in Dash')
    )
])
if __name__ == '__main__':
    app.run(debug=True, port=8050)