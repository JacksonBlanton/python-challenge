# Dependencies
import csv
import os

# Set the file path
file_path = os.path.join("PyBank", "Resources", "budget_data.csv")
data = open(file_path)
Reader = csv.reader(data)

header = next(Reader)

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
profit_loss_changes = []
greatest_increase_date = None
greatest_increase_amount = 0
greatest_decrease_date = None
greatest_decrease_amount = 0

# Read the CSV file
with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Extract the data from the row
        date = row[0]
        profit_loss = int(row[1])

        # Update the total months and net total
        total_months += 1
        net_total += profit_loss

        # Update the profit/loss changes list
        if previous_profit_loss is not None:
            profit_loss_change = profit_loss - previous_profit_loss
            profit_loss_changes.append(profit_loss_change)

            # Update the greatest increase and decrease
            if profit_loss_change > greatest_increase_amount:
                greatest_increase_amount = profit_loss_change
                greatest_increase_date = date
            elif profit_loss_change < greatest_decrease_amount:
                greatest_decrease_amount = profit_loss_change
                greatest_decrease_date = date

        previous_profit_loss = profit_loss

# Compute the average profit/loss change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Print the financial analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")