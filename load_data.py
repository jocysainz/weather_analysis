import kagglehub

# Download the latest version of the dataset
path = kagglehub.dataset_download("ananthr1/weather-prediction")

# Print the path to the downloaded dataset files
print("Path to dataset files:", path)
