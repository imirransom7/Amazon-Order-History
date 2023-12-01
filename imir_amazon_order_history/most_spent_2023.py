from matplotlib import pyplot as plt
from most_spent_overall import df
from most_spent_overall import tab

def get_month_2023(month):
    if month >= "2023-01-01" and month < "2023-02-01":
        return 'January'
    elif month >= "2023-02-01" and month < "2023-03-01":
        return 'February'
    elif month >= "2023-03-01" and month < "2023-04-01":
        return 'March'
    elif month >= "2023-04-01" and month < "2023-05-01":
        return 'April'
    elif month >= "2023-05-01" and month < "2023-06-01":
        return 'May'
    elif month >= "2023-06-01" and month < "2023-07-01":
        return 'June'
    elif month >= "2023-07-01" and month < "2023-08-01":
        return 'July'
    elif month >= "2023-08-01" and month < "2023-09-01":
        return 'August'
    elif month >= "2023-09-01" and month < "2023-10-01":
        return 'September'
    elif month >= "2023-10-01" and month < "2023-11-01":
        return 'October'
    elif month >= "2023-11-01" and month < "2023-12-01":
        return 'November'
    elif month >= "2023-12-01" and month < "2024-01-01":
        return 'December'


df_2023 = df[df["Order Date"] >= "2023-01-01"]

df_2023['Month'] = df_2023['Order Date'].apply(get_month_2023)

dates_and_months = df_2023.groupby(['Month'])['Order Date'].size().reset_index()
print(tab(dates_and_months, 'psql'))

# Using the measurement size to get the amount of orders for the month of each person
dates_and_months = df_2023.groupby(['Month', 'Name'])['Order Date'].size().reset_index()
print(tab(dates_and_months, 'psql'))

pivoted_df = dates_and_months.pivot(
    columns='Name',
    index='Month',
    values='Order Date'
)

pivoted_df = pivoted_df.fillna(0)
print('most purchases made for 2023'.title())
print(tab(pivoted_df, 'psql'))

overall_sum_2023 = df_2023.groupby(['Name'])['Total Owed'].sum().reset_index()
print("most money spent on amazon for 2023".title())
print(tab(overall_sum_2023, 'psql'))

x = sorted(df_2023['Name'].unique())
y = overall_sum_2023['Total Owed']
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)
ax.set_title('money spent on amazon (2023)'.title(), fontsize=21)
ax.set_xlabel("name of the spenders".title(), fontsize=14)
ax.set_ylabel('total spent'.title() + ' (USD)', fontsize=14)


plt.plot(x, y)
plt.show()
