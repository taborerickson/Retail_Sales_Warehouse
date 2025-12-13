import pandas as pd 
import logging 
from pathlib import Path 

# --------------------------
# Logging Configs 
# --------------------------
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s" 
) 

# --------------------------
# Paths 
# -------------------------- 
raw_data_path = Path("data/raw/online_retail.csv") 

# --------------------------
# Expected Schema 
# --------------------------
expected_columns = {
    'InvoiceNo', 
    'StockCode', 
    'Description', 
    'Quantity', 
    'InvoiceDate', 
    'UnitPrice', 
    'CustomerID', 
    'Country' 
}

# --------------------------
# Function to extract the data 
# --------------------------
def extract_raw_data() -> pd.DataFrame: 
    """  
    Extracts the raw retail data fom .csv file and performs basic 
    data validation checks 
    """
    logging.info("Starting data extraction process") 
    if not raw_data_path.exists(): 
        raise FileNotFoundError(
            f"Raw data file not found at {raw_data_path}" 
        )
    # Added encoding="ISO-8859-1" (UK Dataset) 
    data = pd.read_csv(raw_data_path, encoding="ISO-8859-1")  
    logging.info(f"Loaded dataset with {data.shape[0]} rows and {data.shape[1]} columns")
    validate_schema(data) 
    validate_basic_quality(data) 
    logging.info("Data extraction completed successfully") 
    return data 

# --------------------------
# Validation functions 
# --------------------------
def validate_schema(data: pd.DataFrame): 
    actual_columns = set(data.columns) 
    missing_columns = expected_columns - actual_columns 
    if missing_columns: 
        raise ValueError(
            f'Missing expectedcolumns: {missing_columns}' 
        )
    logging.info("Schema vvalidation passed") 

def validate_basic_quality(data: pd.DataFrame): 
    if data.empty: 
        raise ValueError("Dataset is empty") 
    if (data['Quantity'] == 0).all(): 
        raise ValueError("All quantities are zero") 
    if (data['UnitPrice'] <= 0).all(): 
        raise ValueError("All unit prices are non-positive") 
    logging.info("Basic data quality checks passed") 

# --------------------------
# Entry point for script 
# --------------------------
if __name__ == "__main__": 
    extract_raw_data() 
