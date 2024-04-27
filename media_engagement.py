import matplotlib.pyplot as plt
import pandas as pd

# Access the dataset from Power BI
df = dataset  # Assuming 'dataset' is the name of your dataset in Power BI

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract day of the month from the 'date' column
df['day_of_month'] = df['date'].dt.day

# Aggregate data for each day by summing the values of media_engagement
daily_media_engagement = df.groupby('day_of_month')['media_engagements'].sum()

# Plot the line chart with markers
plt.figure(figsize=(10, 6))
plt.plot(daily_media_engagement.index, daily_media_engagement.values, marker='o', color='white')  # Set line color
plt.scatter(daily_media_engagement.index, daily_media_engagement.values, color='#00008B', marker='o')  # Set marker color to dark blue

# Set the labels and title
plt.xlabel('Day of Month', color='white', weight='bold')  # Set text color to black and bold
plt.ylabel('Media Engagement', color='white', weight='bold')  # Set text color to black and bold
plt.title('', color='#000000', weight='bold')  # Set title color to black and bold

# Set background color
plt.gca().set_facecolor('#060F53')
plt.gcf().set_facecolor('#060F53')  # Set background color for the entire figure

# Set color for the axis
plt.gca().tick_params(axis='x', colors='white')  # Set text color to black
plt.gca().tick_params(axis='y', colors='white')  # Set text color to black

# Set the color of the edges and corners to #F0F0F0
plt.gca().spines['top'].set_color('#060F53')
plt.gca().spines['bottom'].set_color('#060F53')
plt.gca().spines['left'].set_color('#060F53')
plt.gca().spines['right'].set_color('#060F53')

# Show the plot
plt.show()