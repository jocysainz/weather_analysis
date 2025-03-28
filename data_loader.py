import pandas as pd

#function to load and analyze the data
def load_data(file_path):
    print(f"Loading data from: {file_path}\n")
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!\n")
    except Exception as e:
        print(f"Error loading dataset: {e}\n")
        return None
    print("First 5 records:\n")
    print(df.head())
    print('\n')
    return df
