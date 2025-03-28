import os
from data_loader import load_data  #import function to load the dataset
from temperature_analysis import find_highest_temperature, calculate_seasonal_averages, compare_seasons  #import analysis functions
from visualization import show_seasonal_avg_chart, ask_user_to_show_chart  #import function for showing seasonal average chart and asking user for input

if __name__ == "__main__":  #check if the script is being run directly
    #define the path to the dataset
    file_path = "C:\\Users\\laura\\.cache\\kagglehub\\datasets\\ananthr1\\weather-prediction\\versions\\1\\seattle-weather.csv"
    
    #check if the dataset file exists at the specified path
    if os.path.exists(file_path):
        #load the dataset using the load_data function
        df = load_data(file_path)
        
        #proceed if the dataset was loaded successfully
        if df is not None:
            #find and display the highest recorded temperature
            find_highest_temperature(df)
            
            #calculate and store the seasonal averages
            seasonal_avg = calculate_seasonal_averages(df)
            
            #ask the user if they want to see the chart for seasonal averages
            if ask_user_to_show_chart(1):
                #show the seasonal average chart if the user agrees
                show_seasonal_avg_chart(seasonal_avg)
            
            #ask the user if they want to see the comparison chart for seasons across years
            if ask_user_to_show_chart(2):
                #show the comparison of seasons across years if the user agrees
                compare_seasons(df)  
            else:
                #inform the user that charts won't be displayed if they declined
                print("Charts will not be displayed.")
    else:
        #if the file doesn't exist, print an error message
        print(f"Error: The file at {file_path} does not exist.")
