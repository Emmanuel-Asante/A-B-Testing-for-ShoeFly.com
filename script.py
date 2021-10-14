import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

# Examine the first 10 rows of ad_clicks
print(ad_clicks.head(10))

# Variable views_from_utm_source to hold the total number of views from each utm_source
views_from_utm_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()

# Display views_from_utm_source
print(views_from_utm_source)

# A new column called is_click, which is True if ad_click_timestamp is not null and False otherwise
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

# Get the percent of people who clicked on ads from each utm_source and assign it to the variable clicks_by_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

# Display clicks_by_source
print(clicks_by_source)

# Pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id and assign it to the variable clicks_pivot
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()

# Examine clicks_pivot
print(clicks_pivot)

# Create a new column in clicks_pivot called percent_clicked which is equal to the percent of users who clicked on the ad from each utm_source
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])

# Examine clicks_pivot
print(clicks_pivot)

# Group experimental_group and count the number users 
print(ad_clicks.groupby('experimental_group').user_id.count().reset_index())

# Group both experimental_group and is_click and count the number of user_id's, and create a pivoton the data
print(
  ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()\
  .pivot(
    columns = 'is_click',
    index = 'experimental_group',
    values = 'user_id'
  ).reset_index()
)

# Variable a_clicks to hold the results for A group
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']

# Variable b_clicks to hold the results for B group
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

# Create a pivot data for a_clicks and assign it to a_clicks_pivot
a_clicks_pivot = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()\
.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

# Calculate the percent of users who clicked on the ad by day for a_clicks
a_clicks_pivot['percentage_clicked'] = a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False])

# Examine a_clicks_pivot
print(a_clicks_pivot)

# Create a pivot data for b_clicks and assign it to b_clicks_pivot
b_clicks_pivot = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()\
.pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()

# Calculate the percent of users who clicked on the ad by day for b_clicks
b_clicks_pivot['percentage_clicked'] = b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False])

# Examine b_clicks_pivot
print(b_clicks_pivot)