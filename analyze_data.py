import pandas as pd
import os
import matplotlib.pyplot as plt

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

#function to find the highest temperature
def find_highest_temperature(df):
    #convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'])
    
    #extract the 'month' and 'year' columns (this creates the 'month' column correctly)
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    #check if the 'month' column is created
    print("Columns in the dataframe:\n")
    print(df.columns)
    
    #finds the row with the highest temperature
    highest_temp = df.loc[df['temp_max'].idxmax()]
    highest_temp_month = highest_temp['month']
    highest_temp_value = highest_temp['temp_max']
    highest_temp_year = highest_temp['year']
    
    print('\n')#space for better reading
    print(f"The highest temperature recorded in the last 10 years was {highest_temp_value}°C in month {highest_temp_month} of {highest_temp_year}.\n")

#function to calculate the average temperature for each season
def calculate_seasonal_averages(df):
    #define a function to assign seasons based on the month
    def get_season(month):
        if month in [12, 1, 2]: return 'Winter'
        elif month in [3, 4, 5]: return 'Spring'
        elif month in [6, 7, 8]: return 'Summer'
        else: return 'Fall'
    
    #create a 'season' column based on the month
    df['season'] = df['month'].apply(get_season)
    
    #calculate the average temperature for each season
    seasonal_avg = df.groupby('season')['temp_max'].mean()
    print("Average temperature for each season:")
    print(seasonal_avg)
    
    return seasonal_avg

#new function to compare average temperatures for each season across years
def compare_seasons(df):
    #group by 'year' and 'season' to calculate the average 'temp_max' temperature for each combination
    season_avg_by_year = df.groupby(['year', 'season'])['temp_max'].mean().unstack()
    
    #plot the comparison of average temperature by year and season
    season_avg_by_year.plot(kind='bar', figsize=(10, 6))
    plt.title("Comparison of Average Temperature by Year and Season")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.xticks(rotation=45)
    plt.show()

#function to ask the user if they want to see a specific chart
def ask_user_to_show_chart(chart_number):
    response = input(f"Would you like to see Chart {chart_number}? (yes/no): ").lower()
    return response == 'yes'

if __name__ == "__main__":
    #path to dataset
    file_path = "C:\\Users\\laura\\.cache\\kagglehub\\datasets\\ananthr1\\weather-prediction\\versions\\1\\seattle-weather.csv"
    
    if os.path.exists(file_path):
        df = load_data(file_path)
        if df is not None:
            find_highest_temperature(df)
            seasonal_avg = calculate_seasonal_averages(df)
            
            #ask the user if they want to see Chart 1 (Seasonal Averages)
            if ask_user_to_show_chart(1):
                seasonal_avg.plot(kind='bar')
                plt.title("Average Maximum Temperature by Season")
                plt.xlabel("Season")
                plt.ylabel("Average Temperature (°C)")
                plt.show()
            
            #ask the user if they want to see Chart 2 (Comparison of Seasons across Years)
            if ask_user_to_show_chart(2):
                compare_seasons(df)  #show the comparison charts if the user agrees
            else:
                print("Charts will not be displayed.")
    else:
        print(f"Error: The file at {file_path} does not exist.")
