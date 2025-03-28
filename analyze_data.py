import pandas as pd
import os

#function to load and analyze the data
def load_data(file_path):
    print(f"Loading data from: {file_path}")  #debugging print
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")  #confirm if loading is successful
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None
    
    #print the first 5 rows to confirm it's loaded correctly
    print("First 5 records:")
    print(df.head())  #prints the first 5 rows to confirm data
    return df

#function to find the month with the highest temperature
def find_highest_temperature(df):
    #convert 'date' column to datetime type for easier manipulation
    df['date'] = pd.to_datetime(df['date'])
    
    #extract year and month
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    #find the row with the highest temp_max value
    highest_temp = df.loc[df['temp_max'].idxmax()]
    highest_temp_month = highest_temp['month']
    highest_temp_value = highest_temp['temp_max']
    print(f"The highest temperature recorded was {highest_temp_value}°C in month {highest_temp_month}.")

#function to calculate the average temperature for each season
def calculate_seasonal_averages(df):
    #define a function to assign seasons based on the month
    def get_season(month):
        if month in [12, 1, 2]:
            return 'Winter'
        elif month in [3, 4, 5]:
            return 'Spring'
        elif month in [6, 7, 8]:
            return 'Summer'
        else:
            return 'Fall'
    
    #create a 'season' column based on the month
    df['season'] = df['month'].apply(get_season)
    
    #calculate the average temperature for each season
    seasonal_avg = df.groupby('season')['temp_max'].mean()
    print("Average temperature for each season:")
    print(seasonal_avg)

if __name__ == "__main__":
    #path to dataset
    file_path = "C:\\Users\\laura\\.cache\\kagglehub\\datasets\\ananthr1\\weather-prediction\\versions\\1\\seattle-weather.csv"
    
    #load the data
    df = load_data(file_path)
    
    #call the functions to perform the analysis
    if df is not None:
        find_highest_temperature(df)
        calculate_seasonal_averages(df)
