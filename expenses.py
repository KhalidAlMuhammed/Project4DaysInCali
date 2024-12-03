import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the CSV file
df = pd.read_csv('expenses.csv', skiprows=1)  # Skip the title row

# Convert Date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Clean Amount column (remove any currency symbols if present)
df['Amount'] = df['Amount'].astype(float)

# Khalid's Expenses
dk = pd.read_csv("khalid.csv")
dm = pd.read_csv("maain.csv")

khalid_total_pay = dk['Amount'].sum()
maain_total_pay = dm['Amount'].sum()

print(f"Total Expenses: ${df['Amount'].sum():.2f}")
print("Total: " + str(khalid_total_pay + maain_total_pay))

print("Khalid's Expenses: " + str(khalid_total_pay) + " Maain's Expenses: " + str(maain_total_pay))

print("Difference: " + str(abs(maain_total_pay - khalid_total_pay)))

print("Split: " + "Maain should pay: " + str(khalid_total_pay/2) + " Khalid should pay: " + str(maain_total_pay/2))

# Person who owes who
if maain_total_pay > khalid_total_pay:
    print("Khalid owes Maain " + str(maain_total_pay/2 - khalid_total_pay/2))
else:
    print("Maain owes Khalid " + str(khalid_total_pay/2 - maain_total_pay/2))

def create_expense_visualizations():
    # Create a figure with subplots
    plt.figure(figsize=(15, 20))
    
    # 1. Category-wise Total Expenses (Pie Chart)
    plt.subplot(3, 1, 1)
    category_totals = df.groupby('Category')['Amount'].sum()
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%')
    plt.title('Expenses by Category')
    
    # 2. Daily Expenses Timeline (Line Plot)
    plt.subplot(3, 1, 2)
    daily_expenses = df.groupby('Date')['Amount'].sum()
    plt.plot(daily_expenses.index, daily_expenses.values, marker='o')
    plt.title('Daily Expenses Timeline')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Amount ($)')
    
    # 3. Location-wise Expenses (Bar Chart)
    plt.subplot(3, 1, 3)
    location_totals = df.groupby('Location')['Amount'].sum().sort_values(ascending=True)
    location_totals.plot(kind='barh')
    plt.title('Expenses by Location')
    plt.xlabel('Amount ($)')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Save the visualization
    plt.savefig('expense_analysis.png')
    
    # Print some basic statistics
    print("\nExpense Summary:")
    print(f"Total Expenses: ${df['Amount'].sum():.2f}")
    print(f"Average Daily Expense: ${df.groupby('Date')['Amount'].sum().mean():.2f}")
    print("\nTop 3 Categories by Expense:")
    print(category_totals.sort_values(ascending=False).head(3))

if __name__ == "__main__":
    create_expense_visualizations() 