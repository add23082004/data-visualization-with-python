import plotly.express as px
import pandas as pd

# Load the dataset into a data frame using Python.

mydata = pd.read_csv('/Users/amadoudiakhadiop/Downloads/Africa_climate_change.csv')

# Clean the data as needed.

mydata['DATE'] = pd.to_datetime(mydata['DATE'])
mydata['Year'] = mydata['DATE'].dt.year

missing_values = mydata.isnull().sum()
print(missing_values)

df_filled = mydata.fillna({'TAVG': pd.NA})
columns_to_fill = ['PRCP', 'TAVG', 'TMAX', 'TMIN']
new_dataset = df_filled.groupby(['COUNTRY', 'DATE'])[columns_to_fill].mean().reset_index()
new_dataset2 = df_filled.groupby(['COUNTRY', 'Year'])[columns_to_fill].mean().reset_index()

missing_values_after = new_dataset.isnull().sum()
print(missing_values_after)
print(new_dataset)
print(new_dataset2)

# Plot a line chart to show the average temperature fluctuations in Tunisia and Cameroon. Interpret the results.
Tunisia_Cameroon = ['Tunisia', 'Cameroon']

filtered_data = new_dataset[new_dataset['COUNTRY'].isin(Tunisia_Cameroon)]

fig = px.line(filtered_data, x='DATE', y='TAVG', color='COUNTRY', markers=True,
              labels={'TAVG': 'Average Temperature (TAVG)', 'DATE': 'Date'},
              title='Average temperature fluctuations in Tunisia and Cameroon')

fig.show()

# Interpretation
print("The evolution of both curves follows a sawtooth pattern, indicating the alternation of two seasons throughout\n"
      "the year. However, due to the distinct geographical locations of the two countries, we observe some differences\n"
      "in the trends of the two curves. The curve for Cameroon primarily fluctuates between temperatures of 70 and 90,\n"
      "while that of Tunisia varies mainly between 50 and 90. The highest recorded temperature for Cameroon is 102,\n"
      "whereas for Tunisia, it is 99.8. The lowest recorded temperature for Cameroon is 49, and for Tunisia, it is 38.\n"
      "This temperature data spans from 1980 to 2023.\n"
      "In conclusion, the sawtooth pattern suggests a cyclical nature of temperature changes, likely corresponding to\n"
      "the seasonal shifts. The differences in temperature ranges and extreme values between Cameroon and Tunisia are\n"
      "attributed to their distinct geographical contexts. Cameroon experiences a warmer temperature range, with higher\n"
      "extremes, compared to Tunisia. These findings provide insights into the unique climatic characteristics of each\n"
      "country over the observed period.")
"""
"""# Zoom in to only include data between 1980 and 2005, try to customize the axes labels.
fig = px.line(filtered_data, x='DATE', y='TAVG', color='COUNTRY', markers=True,
              labels={'TAVG': 'Average Temperature (TAVG)', 'DATE': 'Date'},
              title='Average temperature fluctuations in Tunisia and Cameroon')


fig.update_xaxes(range=['1980-01-01', '2005-12-31'])

fig.show()

# Create Histogram to show temperature distribution in Senegal between [1980,2000] and [2000,2023] (in the same figure).
# Describe the obtained results.

# Create a 'Period' column based on the year
mydata['Period'] = pd.cut(mydata['DATE'].dt.year,
                      bins=[1980, 2000, 2023],
                      labels=['1980-2000', '2000-2023'],
                      include_lowest=True)

# Filter data for Senegal
senegal_data = mydata[mydata['COUNTRY'] == 'Senegal']

# Create histograms for two time periods
fig = px.histogram(senegal_data, x='TAVG', color='Period',
                   nbins=30,
                   labels={'TAVG': 'Temperature', 'Period': 'Time Period'})

# Set the layout
fig.update_layout(title='Temperature Distribution in Senegal (1980-2000 and 2000-2023)',
                  xaxis_title='Temperature',
                  yaxis_title='Frequency')

# Show the figure
fig.show()

print("This histogram represents e temperature distribution in Senegal from 1980 to 2000 and 2000 to 2023.\n"
      "We can see that we can see that between those two periods the temperatures were pretty high (80-90)\n"
      "but during the 2000-2023 period the temperatures were higher and on the other hand, the temperatures\n"
      "were lower between 1980-2000.")

# A choropleth map is the best chart to show the Average temperature per country.

fig = px.choropleth(
    new_dataset2,
    locations='COUNTRY',
    locationmode='country names',
    color='TAVG',
    color_continuous_scale='Viridis',
    animation_frame='Year',
    title='Average Temperature per Country'
)

fig.show()

# Are the variables in the dataset correlated ?

fig = px.scatter(new_dataset, x='TMAX', y='PRCP', title='Scatter Plot of X and Y')
fig.show()

print("These two variables are not correlated")


