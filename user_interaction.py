#function to ask the user if they want to see a specific chart
def ask_user_to_show_chart(chart_number):
    response = input(f"Would you like to see Chart {chart_number}? (yes/no): ").lower()
    return response == 'yes'
