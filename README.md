# California Trip Expense Analyzer

A Python-based expense analysis tool that helps track and visualize shared expenses between two people during a trip to California. The program generates detailed visualizations and calculates expense splits between participants.

## Features

- Expense breakdown by category (pie chart)
- Daily expense timeline (line plot)
- Location-based expense analysis (bar chart)
- Automatic calculation of expense splits
- Detailed payment reconciliation between participants

## Prerequisites

- Python 3.x
- Required Python packages:  ```bash
  pandas
  matplotlib
  seaborn  ```

## File Structure

- `expenses.py` - Main script for expense analysis
- `expenses.csv` - Main expense data file (requires: Date, Amount, Category, Location columns)
- `khalid.csv` - Khalid's expense records
- `maain.csv` - Maain's expense records
- `expense_analysis.png` - Generated visualization output

## CSV File Format

### expenses.csv 
csv
Date,Amount,Category,Location
YYYY-MM-DD,XX.XX,Category Name,Location Name

### khalid.csv/maain.csv
csv
Amount
XX.XX


## Usage

1. Ensure all CSV files are in the same directory as the script
2. Run the script:
   ```bash
   python expenses.py
   ```
3. The script will:
   - Calculate total expenses
   - Show individual contributions
   - Determine who owes whom
   - Generate visualizations saved as 'expense_analysis.png'

## Output

The program provides:
- Total expenses for the trip
- Individual expense breakdowns
- Amount owed between participants
- Visual analysis including:
  - Category-wise expense distribution
  - Daily expense timeline
  - Location-based expense breakdown

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## Authors

- Khalid
- Maain