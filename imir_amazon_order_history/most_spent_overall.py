import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

df = pd.read_csv('orderHistory.csv')
df = df.fillna(0)


# Creating a function to put any DataFrame in to use tabulate
def tab(frame, formatting):
    return tabulate(frame, headers='keys', tablefmt=formatting)


# Creating a function that will be later used to implement a name based on the address in the DataFrame
def get_name(name):
    if name == 'Stephanie Pullins 3007 N STILLMAN ST PHILADELPHIA PA 19132-1306 United States'\
            or name == 'Stephanie Pullins 2626 N BANCROFT ST PHILADELPHIA PA 19132-3933 United States':
        return "Stephanie"
    elif name == 'Ahmad Benefield 3007 N STILLMAN ST PHILADELPHIA PA 19132-1306 United States':
        return "Ahmad"
    elif name == 'Teyonna Pullins 3007 N STILLMAN ST PHILADELPHIA PA 19132-1306 United States':
        return "Teyonna"
    elif name == 'Sadie Graham 203 ATLANTIC AVE WILMINGTON DE 19804-1432 United States':
        return "Sadie"
    elif name == 'Jeffrey Mullen 203 ATLANTIC AVE WILMINGTON DE 19804-1432 United States':
        return "Jeffrey"
    elif name == 'Imir Ransom 1141 Creekside Dr Wilmington DE 19804 United States' \
            or name == 'Imir 1140 CREEKSIDE DR APT 1 WILMINGTON DE 19804-3931 United States' \
            or name == 'Imir Ransom 2005 CERVANTES CT NEWARK DE 19702-4401 United States' \
            or name == 'Imir 2005 CERVANTES CT NEWARK DE 19702-4401 United States' \
            or name == 'Imir 33 WENARK DR APT 12 NEWARK DE 19713-1442 United States' \
            or name == 'Imir Ransom 83 PIKE CREEK RD APT 1B NEWARK DE 19711-6819 United States' \
            or name == 'Imir Ransom 2 Indepence Hall Newark Delaware 19711 United States':
        return "Imir"


# Applying this function to the age column using the apply() method and assigning the result to a new coulumn called name
df['Name'] = df['Shipping Address'].apply(get_name)

overall_sum = df.groupby(['Name'])['Total Owed'].sum().reset_index()
tab(overall_sum, 'psql')

x = sorted(df['Name'].unique())
y = overall_sum['Total Owed']
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Blues, s=10)
ax.set_title('who spent the most money'.title(), fontsize=21)
ax.set_xlabel("name of the spenders".title(), fontsize=14)
ax.set_ylabel('total spent'.title(), fontsize=14)


plt.plot(x, y)


def plt_show():
    return plt.show()

