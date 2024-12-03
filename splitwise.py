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
    
    # 1. Khalid's Category-wise Expenses (Pie Chart)
    plt.subplot(3, 1, 1)
    category_totals = dk.groupby('Category')['Amount'].sum()
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%')
    plt.title('Khalid\'s Expenses by Category')
    
    # 2. Maain's Category-wise Expenses (Pie Chart)
    plt.subplot(3, 1, 2)
    category_totals = dm.groupby('Category')['Amount'].sum()
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%')
    plt.title('Maain\'s Expenses by Category')
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    
    # Save the visualization
    plt.savefig('splitwise.png')
    
if __name__ == "__main__":
    create_expense_visualizations() 