# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
df = pd.read_csv('AusApparalSales4thQrt2020.csv')

# %%
print(df.info())
print(df.describe())
print(df.columns.tolist())
print(df.head())

# %%
print(f"Date is na: {df[df['Date'].isna()].size}\n")
print(f"Time is na: {df[df['Time'].isna()].size}\n")
print(f"Sate is na: {df[df['State'].isna()].size}\n")
print(f"Group is na: {df[df['Group'].isna()].size}\n")
print(f"Unit is na: {df[df['Unit'].isna()].size}\n")
print(f"Sales is na: {df[df['Sales'].isna()].size}\n")

# %%
print(f"Date is null: {df[df['Date'].isnull()].size}\n")
print(f"Time is null: {df[df['Time'].isnull()].size}\n")
print(f"Sate is null: {df[df['State'].isnull()].size}\n")
print(f"Group is null: {df[df['Group'].isnull()].size}\n")
print(f"Unit is null: {df[df['Unit'].isnull()].size}\n")
print(f"Sales is null: {df[df['Sales'].isnull()].size}\n")

# %%
print(f"Date is not na: {df[df['Date'].notna()].size}\n")
print(f"Time is not na: {df[df['Time'].notna()].size}\n")
print(f"Sate is not na: {df[df['State'].notna()].size}\n")
print(f"Group is not na: {df[df['Group'].notna()].size}\n")
print(f"Unit is not na: {df[df['Unit'].notna()].size}\n")
print(f"Sales is not na: {df[df['Sales'].notna()].size}\n")

# %%
print(df.dtypes)

# %%
df['Date'] = pd.to_datetime(df['Date'])

# %%
df.dtypes

# %%
df['Sales_Thousands'] = df['Sales']/1000
df['Month'] = df['Date'].dt.month
df['Year_Week'] = df['Date'].dt.isocalendar().week
df['Weekday'] = df['Date'].dt.weekday

# %%
def annote_bar_chart(chart, dist):
    for bar in chart.patches:
        height = bar.get_height()
        chart.text(
            x=bar.get_x() + bar.get_width() / 2,
            y=height + dist,
            s=f'{height:,.0f}',
            ha='center'
        )

# %% [markdown]
#  # Sales per state: Higher sales in VIC and NSW, lower sales in TAS, NT and WA
df_sales_per_state = df.groupby('State').agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).sort_values(by='Sales_Thousands', ascending=False).reset_index()
print(df_sales_per_state)

# %%
plt.figure(figsize=(10, 5))
plt.pie(df_sales_per_state['Sales_Thousands'], labels=df_sales_per_state['State'], autopct='%1.1f%%', startangle=90)
plt.title('Sales distribution per state')
plt.show()

plt.figure(figsize=(10, 5))
sales_per_state_bar_chart = sns.barplot(x='State', y='Sales_Thousands', data=df_sales_per_state)
annote_bar_chart(sales_per_state_bar_chart, 3000)
plt.ylabel('Sales in thousand AUD')
plt.title('Sales state')
plt.show()

# %% [markdown]
# # Sales per Month: Higher sales in December, followed by October then November
df_sales_per_month = df.groupby('Month').agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).reset_index()
print(df_sales_per_month)

# %%
sales_per_month_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month)
annote_bar_chart(sales_per_month_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month')
plt.show()

sales_per_month_bar_chart_units = sns.barplot(x='Month', y='Unit', data=df_sales_per_month)
annote_bar_chart(sales_per_month_bar_chart_units, 1000)
plt.xlabel('Month')
plt.ylabel('Units sold')
plt.title('Units sold per month')
plt.show()

# %% [markdown]
# # Sales per week: no inference to draw here
df_sales_per_week = df.groupby(['Year_Week']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).reset_index()
print(df_sales_per_week)

# %%
plt.figure(figsize=(15, 6))
sales_per_week_bar_chart = sns.barplot(x='Year_Week', y='Sales_Thousands', data=df_sales_per_week)
annote_bar_chart(sales_per_week_bar_chart, 1000)
plt.xlabel('Week')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per week')
plt.show()

plt.figure(figsize=(15, 6))
sales_per_week_bar_chart_units = sns.barplot(x='Year_Week', y='Unit', data=df_sales_per_week)
annote_bar_chart(sales_per_week_bar_chart_units, 1000)
plt.xlabel('Week')
plt.ylabel('Units sold')
plt.title('Units sold per week')
plt.show()

# %% [markdown]
# # Average price analysis: The average price per day is always 2500. That is unlikely if different items have different prices. The data might be incorrect or corrupted.
df_sales_per_day = df.groupby(['Month', 'Date']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).reset_index()
df_sales_per_day['Avg_Price'] = df_sales_per_day['Sales_Thousands'] / df_sales_per_day['Unit'] * 1000
print(df_sales_per_day)

# %%
print((df['Sales'] / df['Unit']).value_counts())
print(df_sales_per_day.describe())

# %% [markdown]
# # Sales per Month and State
df_sales_per_month_state = df.groupby(['Month','State']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).sort_values(by='Sales_Thousands', ascending=False).reset_index()
plt.figure(figsize=(15, 6))
sales_per_month_state_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_state, hue = "State")
annote_bar_chart(sales_per_month_state_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and state')
plt.show()

# %% [markdown]
# # Sales are not correlated to Groups
df_sales_per_month_group = df.groupby(['Month','Group']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).sort_values(by='Sales_Thousands', ascending=False).reset_index()
plt.figure(figsize=(15, 6))
sales_per_month_group_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_group, hue = "Group")
annote_bar_chart(sales_per_month_group_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and group')
plt.show()

# %% [markdown]
# ## The time of the day does not impact sales
df_sales_per_month_time = df.groupby(['Month','Time']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).reset_index()

plt.figure(figsize=(10, 5))
sales_per_month_time_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_time, hue = "Time")
annote_bar_chart(sales_per_month_time_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and time of day')
plt.show()

# %% [markdown]
# ## <b>The trend of sales per weekday depended on the month</b>
# In total, sales appear to be fairly stable across the days of teh week.
# However:
# - In October: most sales happened on Thursdays and Fridays
# - In November: most sales happened on Mondays and Sundays
# - In December: most sales happened on Tuesdays and Wednesdays

# %%
df_sales_per_month_weekday = df.groupby(['Month','Weekday']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).reset_index()

plt.figure(figsize=(15, 6))
sales_per_month_weekday_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_weekday, hue = "Weekday")
annote_bar_chart(sales_per_month_weekday_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and day of the week')
plt.show()

# %% [markdown]
# ## I assumed there were a few specific days (holidays maybe) during the month that could explain different weekday sales trend each month, but there is no datapoint to support that.

# %% [markdown]
# # Sales per day trend

# %%
plt.figure(figsize=(15, 6))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day)
plt.show()

# %%
plt.figure(figsize=(15, 6))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day[df_sales_per_day['Month'] == 10])
plt.show()

# %%
plt.figure(figsize=(15, 6))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day[df_sales_per_day['Month'] == 11])
plt.show()

# %%
plt.figure(figsize=(15, 6))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day[df_sales_per_day['Month'] == 12])
plt.show()

# %%
df[df['Date'] == '2020-12-06']

# %%
import plotly.express as px
df_sales_per_week_and_day = df.groupby(['Year_Week', 'Weekday']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).reset_index()
df_sales_per_week_and_day

# %%
fig = px.scatter(df_sales_per_week_and_day, x="Year_Week", y="Sales_Thousands")
fig.show()

# %% [markdown]
# # Applying MinMAx Scaling and One-Hot encoding and checking correlations
df_engineered = df.copy()
df_engineered = df_engineered.drop('Sales_Thousands', axis=1, errors='ignore')

# %%
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_engineered[['Sales']] = scaler.fit_transform(df_engineered[['Sales']])
df_engineered

# %%
df_engineered = pd.get_dummies(df_engineered, columns=['Time', 'State', 'Group'])
print(df_engineered)

# %%
sales_data_eng_correlations = df_engineered.corr(numeric_only=True)
plt.figure(figsize=(12, 12))
sns.heatmap(sales_data_eng_correlations, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0.5)
plt.title('Sales data correlations')
plt.show()

# %% [markdown]
# <span style="font-size: 400%; font-weight: bold">Final Report</span>

# %% [markdown]
# #### 1. Average price analysis: The average price per day is always 2500. That is unlikely if different items have different prices. The data might be incorrect or corrupted.
# #### 2. Sales per day across all states:
# #### ------Average: 3.7M  AUD
# #### ------Minimum: 2.7M  AUD
# #### ------Maximum: 4.8M  AUD
# #### 3. Units sold per day across all states:
# #### ------Average: 1512 units
# #### ------Minimum: 1090 units
# #### ------Maximum: 1906 units

# %% [markdown]
# #### 4. Sales per state: Higher sales are in VIC and NSW, lower sales in TAS, NT and WA

# %%
plt.figure(figsize=(10, 5))
plt.pie(df_sales_per_state['Sales_Thousands'], labels=df_sales_per_state['State'], autopct='%1.1f%%', startangle=90)
plt.title('Sales distribution per state')
plt.show()

plt.figure(figsize=(10, 5))
sales_per_state_bar_chart = sns.barplot(x='State', y='Sales_Thousands', data=df_sales_per_state)
annote_bar_chart(sales_per_state_bar_chart, 3000)
plt.ylabel('Sales in thousand AUD')
plt.title('Sales state')
plt.show()

# %% [markdown]
# #### 5. Sales per Month: Higher sales in December, followed by October then November
sales_per_month_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month)
annote_bar_chart(sales_per_month_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month')
plt.show()

# %% [markdown]
# #### 6. Sales per Month and State: the states rank the same whether we consider sales for the entire quarter or sales per month
df_sales_per_month_state = df.groupby(['Month','State']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).sort_values(by='Sales_Thousands', ascending=False).reset_index()
plt.figure(figsize=(15, 6))
sales_per_month_state_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_state, hue = "State")
annote_bar_chart(sales_per_month_state_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and state')
plt.show()

# %% [markdown]
# #### 7. These factors do not influence sales one way or another, so the marketing strategy should be driven by them:
# #### -----------Groups: Women, Men, Kids, Seniors - sales are the same for all groups
# #### -----------Time of day: Morning, Afternoon, Evening - sales are the same for all times of day

# %%
df_sales_per_month_group = df.groupby(['Month','Group']).agg({'Sales_Thousands': 'sum', 'Unit': 'sum'}).sort_values(by='Sales_Thousands', ascending=False).reset_index()
plt.figure(figsize=(10, 5))
sales_per_month_group_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_group, hue = "Group")
annote_bar_chart(sales_per_month_group_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and group')
plt.show()

plt.figure(figsize=(10, 5))
sales_per_month_time_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_time, hue = "Time")
annote_bar_chart(sales_per_month_time_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and time of day')
plt.show()

# %% [markdown]
# #### 8. Overall, sales appear to be stable across the days of the week. However:
# #### ---------- In October: most sales happened on Thursdays and Fridays
# #### ---------- In November: most sales happened on Mondays and Sundays
# #### ---------- In December: most sales happened on Tuesdays and Wednesdays

# %%
plt.figure(figsize=(15, 6))
sales_per_month_weekday_bar_chart = sns.barplot(x='Month', y='Sales_Thousands', data=df_sales_per_month_weekday, hue = "Weekday")
annote_bar_chart(sales_per_month_weekday_bar_chart, 1000)
plt.xlabel('Month')
plt.ylabel('Sales in thousand AUD')
plt.title('Sales per month and day of the week')
plt.show()

# %% [markdown]
# #### 9. We could have assumed there were specific days (e.g., holidays) during certain months that could explain different trends each month, but there is no datapoint to support that. In Australia, apart from Black Friday, Cyber Monday, Boxing Day, Christmas Eve, and Christmas Day, there are no other days that would justify a peak or a valley in clothing sales.
# 
# #### On any given month, there is no specific outlier day that stands <b>significanfly</b> out compared to other days
# 
# #### So, sales cannot be predicted based solely on specific days of the week.

# %%
plt.figure(figsize=(15, 6))
sns.boxplot(x='Month', y='Sales_Thousands', data=df_sales_per_day)
plt.title('Sales per Month and Days')
plt.show()

plt.figure(figsize=(20, 4))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day)
plt.xticks(rotation=45)
plt.title('Sales trend per day for the whole quarter')
plt.show()

plt.figure(figsize=(20, 4))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day[df_sales_per_day['Month'] == 10])
plt.xticks(rotation=45)
plt.title('October sales')
plt.show()

plt.figure(figsize=(20, 4))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day[df_sales_per_day['Month'] == 11])
plt.xticks(rotation=45)
plt.title('November sales')
plt.show()

plt.figure(figsize=(20, 4))
sns.lineplot(x='Date', y='Sales_Thousands', data=df_sales_per_day[df_sales_per_day['Month'] == 12])
plt.xticks(rotation=45)
plt.title('December sales')
plt.show()

# %% [markdown]
# #### 10. As a conclusion, to increase sales, the marketing funds should be directed to WA, NT and TAS states, with no specific regard to the groups of people, days of the week or time of the day



