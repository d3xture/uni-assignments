import pandas as pd

# Creating a sample dataset for the books and customers
books_data = {
    "Book ISBN": ["978-3-16-148410-0", "978-0-262-03384-8", "978-1-4028-9462-6", "978-0-141-03435-3", "978-1-56619-909-4"],
    "Book Title": ["The Great Adventure", "Python Programming", "Data Science Handbook", "Mystery of the Lake", "A Journey Through Time"],
    "Author": ["John Doe", "Jane Smith", "Alice Johnson", "Samuel Lee", "Lily White"],
    "Genre": ["Adventure", "Programming", "Science", "Mystery", "Historical Fiction"],
    "Publication Year": [2015, 2018, 2017, 2020, 2019],
    "Price": [19.99, 29.99, 35.50, 15.00, 22.75],
    "Stock Quantity": [120, 50, 200, 75, 60],
    "Reorder Level": [30, 10, 50, 20, 20]
}

# Creating sample order data to simulate purchase history
orders_data = {
    "Order ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Customer Name": ["Alice Brown", "Bob Green", "Charlie Black", "Alice Brown", "David White", "Eva Green", "Charlie Black", "Bob Green", "Alice Brown", "Eva Green"],
    "Order Date": ["2024-10-01", "2024-10-02", "2024-10-02", "2024-10-03", "2024-10-03", "2024-10-04", "2024-10-04", "2024-10-05", "2024-10-05", "2024-10-06"],
    "Total Amount": [45.98, 29.99, 35.50, 60.00, 22.75, 22.75, 45.98, 29.99, 45.98, 22.75],
    "Books Ordered": [["978-3-16-148410-0", "978-0-141-03435-3"], ["978-0-262-03384-8"], ["978-1-4028-9462-6"], ["978-3-16-148410-0", "978-0-141-03435-3"], ["978-1-56619-909-4"], ["978-3-16-148410-0", "978-1-56619-909-4"], ["978-3-16-148410-0", "978-1-4028-9462-6"], ["978-0-262-03384-8"], ["978-3-16-148410-0", "978-1-56619-909-4"], ["978-3-16-148410-0"]]
}

# Converting to DataFrame
books_df = pd.DataFrame(books_data)
orders_df = pd.DataFrame(orders_data)

# Calculating Average Order Size
total_orders = len(orders_df)
total_books_ordered = sum([len(order) for order in orders_df["Books Ordered"]])
avg_order_size = total_books_ordered / total_orders

# Calculating Top Customers by Total Purchase History
top_customers = orders_df.groupby("Customer Name")["Total Amount"].sum().sort_values(ascending=False)

# Calculating Inventory Remaining (Corrected logic)
def calculate_inventory_remaining(isbn):
    ordered_quantity = sum([isbn in order for order in orders_df["Books Ordered"]])
    stock_quantity = books_df.loc[books_df["Book ISBN"] == isbn, "Stock Quantity"].values[0]
    return stock_quantity - ordered_quantity

books_df["Inventory Remaining"] = books_df["Book ISBN"].apply(calculate_inventory_remaining)

# Displaying the final data
print(" ")
print(f"Books Database:\n{books_df}\n")
print(f"Average Order Size: {avg_order_size:.2f}")
print(f"\nTop Customers Based on Total Purchase History:\n{top_customers}")
print(f"\nInventory Left for Each Book:\n{books_df[['Book Title', 'Inventory Remaining']]}")
