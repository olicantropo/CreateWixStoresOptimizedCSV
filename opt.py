import pandas as pd
import random
import string


def generate_handle_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))


def process_price(price):
    if isinstance(price, str):
        cleaned_price = price.replace("R$", "").replace(",", ".")
    else:
        cleaned_price = price
    return round(float(cleaned_price) * 2.5, 2)


def convert_xlsx_to_csv(input_file, output_file):
    # Load Excel file
    df = pd.read_excel(input_file)

    # Process data
    csv_data = {
        'handleId': [generate_handle_id() for _ in range(len(df))],
        'fieldType': ['Product'] * len(df),
        'name': ['Brinquedo'] * len(df),
        'productImageUrl': df.iloc[:, 2].apply(lambda x: f"{int(x)}.png" if isinstance(x, (int, float)) and not pd.isnull(x) else f"{x}.png"),
        'sku': df.iloc[:, 3],
        'collection': ['Brinquedos'] * len(df),
        'price': df.iloc[:, 6].apply(process_price),
        'visible': ['true'] * len(df),
        'inventory': df.iloc[:, 4]
    }

    # Convert to DataFrame
    csv_df = pd.DataFrame(csv_data)

    # Save to CSV
    csv_df.to_csv(output_file, index=False, sep=',')


# Usage example
convert_xlsx_to_csv('cat.xlsx', 'output.csv')
