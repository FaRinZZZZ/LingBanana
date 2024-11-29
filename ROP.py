import numpy as np
import matplotlib.pyplot as plt

# Inputs
days = 200  # Total number of days to simulate
initial_supply = 1300  # Initial supply in the warehouse
daily_consumption = 550  # Units consumed per day
ROP = 1755.6  # Reorder Point
Leadtime = 3  # Days to receive new stock
order_quantity = 16500  # Units ordered when ROP is reached

# Simulate supply levels
supply = [initial_supply]
orders = []
pending_order = False  # Flag to track if an order is pending

for day in range(1, days + 1):
    # Determine if it's a working day (Mon-Fri)
    is_working_day = (day % 7 != 6) and (day % 7 != 0)  # Exclude Saturday (6) and Sunday (0)
    
    # Consume daily supply only on working days
    current_supply = supply[-1]
    if is_working_day:
        current_supply -= daily_consumption
    
    # Prevent supply from going below zero
    if current_supply < 0:
        current_supply = 0  # Reflect a stockout situation

    # Check for reorder point
    if current_supply <= ROP and not pending_order:
        orders.append(day)
        pending_order = True  # Mark that an order is pending
    
    # Check for received orders
    if day - Leadtime in orders:
        current_supply += order_quantity
        pending_order = False  # Reset pending order flag after receiving stock
    
    supply.append(current_supply)

# Prepare the graph
plt.figure(figsize=(12, 6))
plt.plot(range(days + 1), supply, label="Warehouse Supply", color='blue')
plt.axhline(y=ROP, color='red', linestyle='--', label="ROP (Reorder Point)")

# Mark reorder days
for order_day in orders:
    plt.axvline(x=order_day, color='green', linestyle=':', label=f"Order Placed" if order_day == orders[0] else "")

# Annotate the graph
plt.title("ROP Graph: Warehouse Supply Over Time Packaging (5-Day Workweek)")
plt.xlabel("Day")
plt.ylabel("Supply in Warehouse")
plt.legend()
plt.grid()

# Show the graph
plt.show()
