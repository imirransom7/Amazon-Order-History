from tabulate import tabulate
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
orders = pd.read_csv("orderHistory.csv")

# Set maximum columns to display
pd.set_option("display.max_columns", 27)

# to see all rows
# pd.set_option("display.max_rows", None)

# Fill missing values with 0
orders = orders.fillna(0)


# Remove non-numeric characters and convert to float
orders["Shipment Item Subtotal"] = pd.to_numeric(orders["Shipment Item Subtotal"].str.replace('[^\d.]', '', regex=True), errors='coerce')
item_subtotal = orders["Shipment Item Subtotal"]

columns_to_print = ["Shipping Address", "Product Name", "Shipment Item Subtotal", "Order Date"]
#print(order_history[columns_to_print])

# This variable has all items ordered from the beginning of 2023 till the time I reqauted the Csv files of my Amazon order history
items_for_2023 = orders[orders["Order Date"] > "2023-01-01"]

# This variable is going to show me all orders made to Stephanie Pullins
moms_orders = orders[orders["Shipping Address"] == "Stephanie Pullins 3007 N STILLMAN ST PHILADELPHIA PA 19132-1306 United States"]
# print(moms_orders)

# print(tabulate(order_history.head(5), headers = "keys", tablefmt = "simple"))
# Sum the cleaned "Shipment Item Subtotal" column
subtotal_sum = item_subtotal.sum()
# print(subtotal_sum)
addresses = orders["Shipping Address"].unique()
print(addresses)

order_names = orders.groupby(["Product Name", "Shipping Address"])["Unit Price"].count().reset_index()
print(order_names)

order_names_pivot = order_names.pivot(
    columns="Shipping Address",
    index="Product Name",
    values="Unit Price"
).reset_index()

print(order_names_pivot)




# x = [1, 2, 3, 4, 5]
#
# y = [2, 4, 6, 8, 10]
#
# plt.plot(x, y)
#
# plt.show()











