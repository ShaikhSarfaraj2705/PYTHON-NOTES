# CUSTOMIZE SEABORN PLOT
# 1.Built-in Styles and Grids in Seaborn
# darkgrid – Dark background with light gridlines. Great for clear contrast.
# whitegrid – White background with light gridlines. Ideal for statistical plots.
# dark – Dark background without gridlines. Clean and modern look.
# white – Plain white background without gridlines. Good for simple visuals.
# ticks – White background with axis ticks styled sharply. Suitable for publications.
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")

sns.boxplot(x='species', y='petal_length', data=sns.load_dataset('iris'))
plt.title('Petal Length Distribution by Species')
plt.show()

# 2.Customizing Color Palettes:You can choose from built-in palettes like "deep", "muted", or "bright" or define 
# your own using sns.color_palette().
sns.set_palette("pastel") 

sns.violinplot(x='species', y='petal_length', data=sns.load_dataset('iris'))
plt.title('Petal Length Distribution by Species')
plt.show()

# Using a Custom Palette:
custom_colors = ['#FF5733', '#33FFBD', '#335BFF']
sns.set_palette(custom_colors)

sns.violinplot(x='species', y='petal_length', data=sns.load_dataset('iris'))
plt.title('Custom Colored Petal Length Distribution')
plt.show()

# 3.Adjusting Figure Size and Aspect Ratio:We can adjust the figure size using plt.figure(figsize=(width,height)) to
# control the plot's dimensions. This allows for better customization to fit different presentation or reports.
plt.figure(figsize=(10, 6))

sns.lineplot(x='year', y='passengers', data=sns.load_dataset('flights'))
plt.title('Number of Passengers Over Time')
plt.show()

# 4.Adding Markers to Line Plots:Markers can be added to Seaborn line plots using the marker argument to highlight data points
sns.lineplot(x='year', y='passengers', data=sns.load_dataset('flights'), marker='o')
plt.title('Number of Passengers Over Time')
plt.show()

#VISUALIZING RELATIONSHIPS AND PATTERS WITH SEABORN
# 1.pair Plot:Pair plots are used explore relationships between several variables by generating scatter plots for 
# every pair of variables in a dataset along with univariate distributions on the diagonal.
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
custom_palette = sns.color_palette("husl", 8)
sns.set_palette(custom_palette)

data = sns.load_dataset("iris")
sns.pairplot(data, hue="species")
plt.show()