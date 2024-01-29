

data = [
    ["No", "Name", "Capitalization", "QtyBought", "Bought Price", "Current Price", "Total Invested", "Total Current Value", "Profit/Loss"],
    [1, "Bitcoin", "High", 15, 38000, 62000, 570000, 930000, 360000],
    [2, "Ethereum", "High", 90, 4200, 3500, 378000, 315000, -63000],
    [3, "Solana", "Mid", 60, 260, 110, 15600, 6600, -9000],
    [4, "Decentraland", "Mid", 30000, 1.5, 5, 45000, 150000, 105000],
    [5, "The Sandbox", "Mid", 25000, 2, 4, 50000, 100000, 50000],
    [6, "Dogecoin", "Low", 55000, 0.4, 0.15, 22000, 8250, -13750]
]

# Determine column widths based on the maximum length in each column
column_widths = [max(len(str(item)) for item in col) for col in zip(*data)]

# Print data with each header and its values in separate columns
for row in data:
    row_format = " ".join(["{:<{}}"] * len(row))
    print(row_format.format(row, column_widths))
