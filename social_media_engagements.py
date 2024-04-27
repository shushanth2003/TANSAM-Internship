import matplotlib.pyplot as plt
import pandas as pd

# Assuming 'dataset' is the name of your dataset in Power BI
df = dataset

# Group data by monthname and sum the values for likes, retweets, follows, and replies
monthly_data = df.groupby('MonthName').agg({'likes': 'sum', 'retweets': 'sum', 'follows': 'sum', 'replies': 'sum'})

# Plot the stacked bar chart with inverted axes
ax = monthly_data.plot(kind='barh', stacked=True, figsize=(10, 6))  # Set kind to 'barh' for horizontal orientation

# Set labels and title
plt.xlabel('Count', color='white', fontsize=20, fontweight='bold')
plt.ylabel('Metrics', color='white', fontsize=20, fontweight='bold')
plt.title('', color='white', fontsize=20, fontweight='bold')

# Set background color
plt.gca().set_facecolor('#060F53')  # Set background color for the plot area
plt.gcf().set_facecolor('#060F53')  # Set background color for the entire figure

# Set edge color to #F0F0F0
plt.gca().spines['top'].set_color('#060F53')
plt.gca().spines['right'].set_color('#060F53')
plt.gca().spines['bottom'].set_color('#060F53')
plt.gca().spines['left'].set_color('#060F53')

# Set text and values color to black and bold
plt.gca().tick_params(axis='x', colors='white', labelsize=20)
plt.gca().tick_params(axis='y', colors='white', labelsize=20)

# Show plot
plt.show()