import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore, Style

#function to find the highest temperature
def find_highest_temperature(df):
    #convert the 'date' column to datetime format
    df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Ensure invalid date entries are handled
    
    #check if 'temp_max' column exists
    if 'temp_max' not in df.columns:
        print("Error: 'temp_max' column is missing.")
        return
    
    #extract the 'month' and 'year' columns
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    
    #find the row with the highest temperature
    highest_temp = df.loc[df['temp_max'].idxmax()]
    highest_temp_month = highest_temp['month']
    highest_temp_value = highest_temp['temp_max']
    highest_temp_year = highest_temp['year']
    
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
    
    # Define colors for each season
    season_colors = {
        "Fall": Fore.YELLOW,
        "Spring": Fore.GREEN,
        "Summer": Fore.RED,
        "Winter": Fore.CYAN
    }
    
    # Print the seasonal averages with colors
    print("\nAverage temperature for each season:")
    for season, temp in seasonal_avg.items():
        print(f"{season_colors.get(season, Fore.WHITE)}{season}: {temp:.2f}°C{Style.RESET_ALL}")
    
    return seasonal_avg

#new function to compare average temperatures for each season across years
def compare_seasons(df):
    # group by 'year' and 'season' to calculate the average 'temp_max' temperature for each combination
    season_avg_by_year = df.groupby(['year', 'season'])['temp_max'].mean().unstack()
    
    #plot the comparison of average temperature by year and season
    season_avg_by_year.plot(kind='bar', figsize=(10, 6))
    plt.title("Comparison of Average Temperature by Year and Season")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.xticks(rotation=45)
    plt.show()
