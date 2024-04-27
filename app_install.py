import matplotlib.pyplot as plt
import pandas as pd

# Access the dataset from Power BI
df = dataset  # Assuming 'dataset' is the name of your dataset in Power BI

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Extract day of the month from the 'date' column
df['day_of_month'] = df['date'].dt.day

# Aggregate data for each day by summing the values
daily_data = df.groupby('day_of_month').agg({'app_installs': 'sum', 'app_opens': 'sum'})

# Plot the area chart
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot 'app_installs' on the primary y-axis with the specified color and thicker line
ax1.plot(daily_data.index, daily_data['app_installs'], color='white', alpha=0.5, linewidth=3.0, label='App Installs')
ax1.fill_between(daily_data.index, daily_data['app_installs'], color='white', alpha=0.2)  # Reduce alpha for less noise

# Set the labels and title for the primary y-axis
ax1.set_xlabel('Day of Month', color='white', weight='bold')  # Set x-axis label text color to white and bold
ax1.set_ylabel('App Installs', color='white', weight='bold')  # Set y-axis label text color to white and bold
ax1.tick_params(axis='y', labelcolor='white', labelsize=12)  # Set y-axis tick label color and size
ax1.tick_params(axis='x', labelcolor='white', labelsize=12)  # Set x-axis tick label color and size

# Create a secondary y-axis for 'app_opens' with the specified color
ax2 = ax1.twinx()
ax2.plot(daily_data.index, daily_data['app_opens'], color='white', alpha=0.5, label='App Opens')
ax2.fill_between(daily_data.index, daily_data['app_opens'], color='white', alpha=0.2)  # Reduce alpha for less noise

# Set the labels and title for the secondary y-axis
ax2.set_ylabel('App Opens', color='white', weight='bold')  # Set y-axis label text color to white and bold
ax2.tick_params(axis='y', labelcolor='white', labelsize=12)  # Set y-axis tick label color and size

# Add a legend with white text color
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left', facecolor='#060F53', edgecolor='white', fontsize=10)

# Set background color
fig.patch.set_facecolor('#060F53')  # Set background color for the figure

# Set edge color to match the background color
for spine in ax1.spines.values():
    spine.set_edgecolor('#060F53')

for spine in ax2.spines.values():
    spine.set_edgecolor('#060F53')

# Set background color of the plot area
ax1.set_facecolor('#060F53')
ax2.set_facecolor('#060F53')

# Set title (if needed)
plt.title('App Installs and Opens by Day of Month', color='white', weight='bold', fontsize=14)  # Set title text color to white and bold

# Show the plot
plt.show()
