import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the dataset using Pandas
df = pd.read_csv('epa-sea-level.csv')

# Create a scatter plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data', marker='o', color='b')

# Perform linear regression on the entire dataset
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create a line of best fit for the entire dataset, including predictions for 2050
years = list(range(1880, 2051))
line = [slope * year + intercept for year in years]
plt.plot(years, line, label='Best Fit Line (1880-2050)', color='r')

# Perform linear regression on data from year 2000 onwards
recent_data = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])

# Create a line of best fit for data from 2000 to the latest year, including predictions for 2050
years_recent = list(range(2000, 2051))
line_recent = [slope_recent * year + intercept_recent for year in years_recent]
plt.plot(years_recent, line_recent, label='Best Fit Line (2000-2050)', color='g')

# Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')

# Add legend
plt.legend()



# Show the plot
plt.grid(True)
plt.show()
