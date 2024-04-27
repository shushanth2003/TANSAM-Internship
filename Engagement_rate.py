import matplotlib.pyplot as plt
import pandas as pd

# Access the dataset from Power BI
df = dataset  # Assuming 'dataset' is the name of your dataset in Power BI

# Calculate the total sum of engagement rate
total_engagement_rate = df['engagement_rate'].sum()

# Calculate the percentage of each day's engagement rate compared to the total
df['engagement_rate_percentage'] = df['engagement_rate'] / total_engagement_rate * 100

# Plot the waterfall chart
plt.figure(figsize=(10, 6))
bars = plt.bar(df['day'], df['engagement_rate_percentage'], color='#F5F5F5', alpha=0.5)
plt.xlabel('Day',color="white",size=15)
plt.ylabel('% of Total Engagement Rate',color="white",size=15)
plt.title('')

# Display the percentage values above the bars
for bar, percentage in zip(bars, df['engagement_rate_percentage']):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage:.2f}%', ha='center', va='bottom')

# Set background, edges, and panel color
plt.gcf().set_facecolor('#060F53')
plt.gca().set_facecolor('#060F53')

# Set color of x and y tick labels
plt.xticks(color='white', size=12)
plt.yticks(color='white', size=12)

# Show plot
plt.show()
