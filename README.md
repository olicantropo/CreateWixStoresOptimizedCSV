# CreateWixStoresOptimizedCSV
This Python script converts data from an Excel (.xlsx) file to a CSV file with a custom format. The script processes specific columns of the Excel file, generates unique identifiers, and applies certain transformations (e.g., cleaning and converting price data).

# Features
Random Handle ID Generation: Each row gets a unique handleId composed of 10 random alphanumeric characters.
Price Processing: Prices are cleaned (removes "R$" and replaces commas with dots) and multiplied by a factor of 2.5.
Custom CSV Format: Columns are transformed and formatted in a specific structure:
handleId: Randomly generated unique ID.
fieldType: Set to "Product" for all rows.
name: Set to "Brinquedo" for all rows.
productImageUrl: Created based on the third column in the Excel file, formatted as .png.
sku: Data copied from the fourth column.
collection: Set to "Brinquedos" for all rows.
price: Processed price based on the seventh column.
visible: Set to "true" for all rows.
inventory: Data copied from the fifth column.

# Requirements
Python 3.x
Pandas library (for reading and manipulating Excel/CSV files)
Openpyxl library (for reading .xlsx files)

You can install the required dependencies using:
_pip install pandas openpyxl_

# Usage
1. Prepare your Excel file: Ensure the Excel file has at least 7 columns. The relevant columns should be:

Column 3: Image names or IDs (used for productImageUrl)
Column 4: SKUs (used for sku)
Column 5: Inventory numbers (used for inventory)
Column 7: Prices (used for price)

2. Run the script: The script will read the Excel file, process the data, and generate a CSV file.

   from excel_to_csv import convert_xlsx_to_csv

convert_xlsx_to_csv('input_file.xlsx', 'output_file.csv')

3. Output: The script will generate a CSV file (output_file.csv) with the following columns:

handleId
fieldType
name
productImageUrl
sku
collection
price
visible
inventory

