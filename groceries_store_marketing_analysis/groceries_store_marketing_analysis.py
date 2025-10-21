# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# %%
pd.set_option('display.max_columns', None)
df = pd.read_csv('marketing_data.csv')
df

# %%
df.shape

# %%
df.info()

# %%
df.describe()

# %%
columns_list = df.columns.tolist()
print(columns_list)

# %%
type(df['Education'].value_counts())

# %%
selected_columns = ['Education', 'Marital_Status', 'Kidhome', 'Teenhome', 'Response', 'Complain', 'Country']
for column_name in selected_columns:
    val_count = df[column_name].value_counts()
    print(f"Value Counts of {column_name}")
    print('Number of values:', val_count.size)
    print(val_count, '\n')
    #plt.figure(figsize=(10, 5))
    val_count.plot(kind='bar')
    plt.title(column_name)
    plt.xticks(rotation=0)
    plt.show()

# %%
df.columns[df.isna().any()]

# %%
df.columns[df.isnull().any()]

# %%
df[df['Income'].isna()].size

# %%
df[df['Income'].isna()]

# %%
df['Marital_Status'].value_counts()

# %%
df.loc[:,'Marital_Status']

# %% [markdown]
# # Removing rows where marital status is Absurd and replacing YOLO/Alone with Single

# %%
df = df[df['Marital_Status'] != 'Absurd']
df['Marital_Status'] = df['Marital_Status'].replace('YOLO', 'Single')
df['Marital_Status'] = df['Marital_Status'].replace('Alone', 'Single')
df['Marital_Status'].value_counts()

# %% [markdown]
# # Fixing data types where applicable

# %%
df.dtypes

# %%
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])

# %%
df.loc[:,'Income']

# %%
df = df.reset_index(drop=True)

# %%
for i in range(len(df)):
    if (pd.notna(df.loc[i,'Income'])):
        df.loc[i,'Income'] = str(df.loc[i,'Income']).replace('$','')
        df.loc[i,'Income'] = str(df.loc[i,'Income']).replace(',','')
        df.loc[i,'Income'] = str(df.loc[i,'Income']).replace(' ','')

# %%
df['Income'] = pd.to_numeric(df['Income'], errors='coerce')

# %%
df.dtypes

# %% [markdown]
# # Imputing missing income values based on the mean income per education and marital status

# %%
df_avg_income = df[df['Income'].notna()]

# %%
df_avg_income =  df_avg_income.groupby(['Education','Marital_Status']).agg({'Income': 'mean'}).reset_index()
df_avg_income['Income'] = round(df_avg_income['Income'])

# %%
df_avg_income['Income_ID'] = df_avg_income['Education'].astype(str) + ' - ' + df_avg_income['Marital_Status'].astype(str)

# %%
df_avg_income

# %%
df_avg_income[df_avg_income['Income_ID'] == 'PhD - Married'].reset_index(drop=True).loc[0,'Income']

# %% [markdown]
# ## Function to get the average income depending on the Income ID (combination of Education and Marital Status)

# %%
def get_income(income_id):
    return float(df_avg_income[df_avg_income['Income_ID'] == income_id].reset_index(drop=True).loc[0,'Income'])

# %%
get_income('PhD - Single')

# %%
type(get_income('PhD - Married'))

# %%
df['Income_ID'] = df['Education'].astype(str) + ' - ' + df['Marital_Status'].astype(str)

# %%
df[df['Income'].isna()].size

# %%
for income_id in df_avg_income['Income_ID']:
    print (f"Updating income of '{income_id}' to {get_income(income_id)}")
    df.loc[(df['Income'].isna()) & (df['Income_ID'] == income_id), 'Income'] = get_income(income_id)

# %%
df[df['Income'].isna()]

# %% [markdown]
# # Create variables to represent the total number of children, age, total spending, total purchases

# %%
df['Total_Children'] = df['Kidhome'] + df['Teenhome']
df['Age'] = datetime.now().year - df['Year_Birth']
df['Total_Spend'] = df['MntWines'] + df['MntFruits'] + df['MntMeatProducts'] + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
df['Total_Purchases'] = df['NumWebPurchases'] + df['NumCatalogPurchases'] + df['NumStorePurchases']
df = df[df['Total_Purchases'] > 0]
df.head(2)

# %%
df = df.drop(['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds'], axis=1, errors='ignore')

# %%
print(columns_list)

# %%
df.duplicated()

# %%
plt.hist(df['Total_Purchases'], bins=100, edgecolor='blue')
plt.title('Number of purchases across all channels')
plt.xlabel('Purchases')
plt.ylabel('Frequency')
plt.show()

# %%
df.head(2)

# %% [markdown]
# # Function to add labels to a bar chart

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
# # Bar charts to analyze the spends per the different variables

# %%
df_spend_educ = df.groupby(['Education']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).sort_values(by='Total_Spend', ascending=False).reset_index()
df_spend_marital = df.groupby(['Marital_Status']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).sort_values(by='Total_Spend', ascending=False).reset_index()
df_spend_income_id = df.groupby(['Income_ID']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).sort_values(by='Total_Spend', ascending=False).reset_index()
df_spend_country = df.groupby(['Country']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).sort_values(by='Total_Spend', ascending=False).reset_index()

# %%
fig, axes = plt.subplots(ncols=2, figsize=(12, 5))

spend_educ_barchart = sns.barplot(x='Education', y='Total_Spend', data=df_spend_educ, ax=axes[0])
annote_bar_chart(spend_educ_barchart, 1000)
axes[0].set_title('Total_Spend')

spend_educ_barchart_num = sns.barplot(x='Education', y='Total_Purchases', data=df_spend_educ, ax=axes[1])
annote_bar_chart(spend_educ_barchart_num, 200)
axes[1].set_title('Total_Purchases')

plt.xlabel('Education Level')
plt.tight_layout()
plt.show()

# %%
fig, axes = plt.subplots(ncols=2, figsize=(12, 5))

spend_marital_barchart = sns.barplot(x='Marital_Status', y='Total_Spend', data=df_spend_marital, ax=axes[0])
annote_bar_chart(spend_marital_barchart, 1000)
axes[0].set_title('Total_Spend')

spend_marital_barchart_num = sns.barplot(x='Marital_Status', y='Total_Purchases', data=df_spend_marital, ax=axes[1])
annote_bar_chart(spend_marital_barchart_num, 200)
axes[1].set_title('Total_Purchases')

plt.xlabel('Marital Status Level')
plt.tight_layout()
plt.show()

# %%
fig, axes = plt.subplots(ncols=2, figsize=(12, 8))

spend_income_id_barchart = sns.barplot(x='Income_ID', y='Total_Spend', data=df_spend_income_id, ax=axes[0])
annote_bar_chart(spend_income_id_barchart, 1000)
axes[0].set_title('Total_Spend')
axes[0].tick_params(axis='x', rotation=90)

spend_income_id_barchart_num = sns.barplot(x='Income_ID', y='Total_Purchases', data=df_spend_income_id, ax=axes[1])
annote_bar_chart(spend_income_id_barchart_num, 100)
axes[1].set_title('Total_Purchases')
axes[1].tick_params(axis='x', rotation=90)

#plt.xticks(rotation=45)
plt.xlabel('Income ID')
plt.tight_layout()
plt.show()

# %%
fig, axes = plt.subplots(ncols=2, figsize=(12, 5))

spend_country_barchart = sns.barplot(x='Country', y='Total_Spend', data=df_spend_country, ax=axes[0])
annote_bar_chart(spend_country_barchart, 1000)
axes[0].set_title('Total_Spend')

spend_country_barchart_num = sns.barplot(x='Country', y='Total_Purchases', data=df_spend_country, ax=axes[1])
annote_bar_chart(spend_country_barchart_num, 200)
axes[1].set_title('Total_Purchases')

plt.xlabel('Country')
plt.tight_layout()
plt.show()

# %% [markdown]
# # Sales in ME (Montenegro) are insignificant - removing those rows

# %%
df = df[df['Country'] != 'ME']

# %%
df[df['Country'] == 'ME']

# %%
df.size

# %% [markdown]
# # Removing outliers in Age

# %%
df['Age']

# %%
sns.boxplot(data=df['Age'])
plt.title('Ages box plot')
plt.show()

# %%
age_q1 = df['Age'].quantile(0.25)
age_q3 = df['Age'].quantile(0.75)
age_iqr = age_q3 - age_q1
age_lower_bound = age_q1 - 1.5 * age_iqr
age_upper_bound = age_q3 + 1.5 * age_iqr

# %%
print("age_q1:", age_q1)
print("age_q3:", age_q3)
print("age_iqr:", age_iqr)
print("age_lower_bound:", age_lower_bound)
print("age_upper_bound:", age_upper_bound)

# %%
df[df['Age'] > 93]

# %%
df[df['Age'] <= 21]

# %%
df = df[df['Age'] <= 93]

# %%
sns.boxplot(data=df['Age'])
plt.title('Ages box plot')
plt.show()

# %%
df['Age'].describe()

# %% [markdown]
# # Creating bins for Age (age groups)

# %%
age_bin_edges = [25, 35, 45, 55, 65, np.inf]
age_bin_labels = ['25-34', '35-44', '45-54', '55-64','65+']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bin_edges, labels=age_bin_labels, right=False)

# %%
df.tail(2)

# %%
df = df.drop('Age', axis=1, errors='ignore')

# %%
df_spend_age = df.groupby(['Age_Group']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).sort_values(by='Total_Spend', ascending=False).reset_index()

# %%
df_spend_age

# %%
fig, axes = plt.subplots(ncols=2, figsize=(12, 8))

spend_income_age_barchart = sns.barplot(x='Age_Group', y='Total_Spend', data=df_spend_age, ax=axes[0], order=df_spend_age['Age_Group'], color='grey')
annote_bar_chart(spend_income_age_barchart, 1000)
axes[0].set_title('Total_Spend')
#axes[0].tick_params(axis='x', rotation=90)

spend_income_age_barchart_num = sns.barplot(x='Age_Group', y='Total_Purchases', data=df_spend_age, ax=axes[1], order=df_spend_age['Age_Group'], color='aqua')
annote_bar_chart(spend_income_age_barchart_num, 100)
axes[1].set_title('Total_Purchases')
#axes[1].tick_params(axis='x', rotation=90)

#plt.xticks(rotation=45)
plt.xlabel('Age Group')
plt.tight_layout()
plt.show()

# %% [markdown]
# # Sales trend analysis - no seasonality

# %%
df['Month'] = df['Dt_Customer'].dt.to_period('M')
df['Year_Week'] = df['Dt_Customer'].dt.year.astype(str) + '-' + df['Dt_Customer'].dt.isocalendar().week.astype(str)
df['Quarter'] = df['Dt_Customer'].dt.to_period('Q')

# %%
df.head(2)

# %%
df_spend_week = df.groupby(['Year_Week']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).reset_index()
df_spend_month = df.groupby(['Month']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).reset_index()
df_spend_quarter = df.groupby(['Quarter']).agg({'Total_Spend': 'sum', 'Total_Purchases': 'sum'}).reset_index()

# %%
plt.figure(figsize=(20, 4))
sns.lineplot(x='Year_Week', y='Total_Spend', data=df_spend_week)
plt.xticks(rotation=90)
plt.title('Sales trend per week')
plt.show()

# %%
fig, axes = plt.subplots(ncols=2, figsize=(12, 5))

spend_quarter_barchart = sns.barplot(x='Quarter', y='Total_Spend', data=df_spend_quarter, ax=axes[0], color='blue')
annote_bar_chart(spend_quarter_barchart, 2000)
axes[0].set_title('Total_Spend')

spend_quarter_barchart_num = sns.barplot(x='Quarter', y='Total_Purchases', data=df_spend_quarter, ax=axes[1], color='green')
annote_bar_chart(spend_quarter_barchart_num, 50)
axes[1].set_title('Total_Purchases')

plt.xlabel('Quarter')
plt.tight_layout()
plt.show()

# %% [markdown]
# # One-hot encoding and correlation analysis

# %%
print(df.columns.tolist())

# %%
df_engineered = df.drop(['ID', 'Year_Birth', 'Education', 'Marital_Status', 'Kidhome', 'Teenhome', 'Dt_Customer', 'MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'Month','Year_Week','Quarter', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Response', 'Complain'], axis=1, errors='ignore')
df_engineered.head(2)

# %%
df_engineered = pd.get_dummies(df_engineered, columns=['Country', 'Income_ID', 'Age_Group'], prefix='', prefix_sep='')

# %%
df_engineered.head(5)

# %%
df_engineered.tail(5)

# %%
sales_data_eng_correlations = df_engineered.corr(numeric_only=True)
plt.figure(figsize=(20, 12))
sns.heatmap(sales_data_eng_correlations, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0.5)
plt.title('Sales data correlations')
plt.show()

# %% [markdown]
# # Only a few variables have a possible correlation with spends. Let's drop all others and try again.

# %%
print(df.columns.tolist())

# %%
df_engineered = df.drop(['ID', 'Year_Birth', 'Kidhome', 'Teenhome', 'Dt_Customer', 'Recency', 'NumDealsPurchases', 'NumWebPurchases', 'NumCatalogPurchases', 'NumStorePurchases', 'AcceptedCmp3', 'AcceptedCmp4', 'AcceptedCmp5', 'AcceptedCmp1', 'AcceptedCmp2', 'Response', 'Complain', 'Income_ID', 'Month', 'Year_Week', 'Quarter','Country'], axis=1, errors='ignore')

# %%
df_engineered = pd.get_dummies(df_engineered, columns=['Education', 'Marital_Status', 'Age_Group'], prefix='', prefix_sep='')

# %%
df_engineered.head(5)

# %%
sales_data_eng_correlations2 = df_engineered.corr(numeric_only=True)
plt.figure(figsize=(20, 12))
sns.heatmap(sales_data_eng_correlations2, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0.5)
plt.title('Sales data correlations 2nd attepmt')
plt.show()

# %% [markdown]
# # Income has the strongest correlation with spend
# # The number of children is negatively correlated with soend: the more children, the less spend
# # Surprisingly, the more visits in store, teh less likely the visitor is to make a purchase

# %% [markdown]
# <span style="font-size: 300%; font-weight: bold">Ok, i'll stop here. I did the first exercise also. The company needs to pay more for more analysis. I am exhausted... :-)</span>

# %%



