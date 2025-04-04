import matplotlib.pyplot as plt

#function to ask the user if they want to see a specific chart
def ask_user_to_show_chart(chart_number):
    response = input(f"Would you like to see Chart {chart_number}? (yes/no): ").lower()
    return response == 'yes'

#function to plot the seasonal averages
def show_seasonal_avg_chart(seasonal_avg):
    seasonal_avg.plot(kind='bar')
    plt.title("Average Maximum Temperature by Season")
    plt.xlabel("Season")
    plt.ylabel("Average Temperature (°C)")
    plt.show()
