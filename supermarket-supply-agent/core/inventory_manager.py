import pandas as pd
from datetime import datetime, timedelta

# Constants
LOW_STOCK_THRESHOLD = 20
EXPIRY_WARNING_DAYS = 7

def load_inventory_data(file_path):
    """Load inventory CSV with ItemSize and parse dates."""
    df = pd.read_csv(file_path, parse_dates=['ExpiryDateBatch'])
    return df

def identify_low_stock(df):
    """Flag items with low stock grouped by ItemID and ItemSize."""
    grouped = df.groupby(['ItemID', 'ItemName', 'ItemSize'])['StockQty'].sum().reset_index()
    low_stock = grouped[grouped['StockQty'] < LOW_STOCK_THRESHOLD]
    return low_stock

def detect_expiring_batches(df):
    """Find batches nearing expiry within EXPIRY_WARNING_DAYS."""
    today = datetime.today()
    upcoming = today + timedelta(days=EXPIRY_WARNING_DAYS)
    expiring = df[df['ExpiryDateBatch'] <= upcoming]
    return expiring[['ItemID', 'ItemName', 'ItemSize', 'BatchID', 'ExpiryDateBatch', 'StockQty']]

def summarize_inventory(file_path):
    df = load_inventory_data(file_path)
    low_stock_items = identify_low_stock(df)
    expiring_batches = detect_expiring_batches(df)
    return low_stock_items, expiring_batches

if __name__ == "__main__":
    inventory_file = "../data/inventory_sample.csv"
    low_stock, expiring = summarize_inventory(inventory_file)

    print("\n--- Low Stock Items ---")
    print(low_stock)

    print("\n--- Expiring Batches ---")
    print(expiring)
5