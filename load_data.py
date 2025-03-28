import os
import kagglehub

#define the path where the dataset is downloaded
dataset_path = "C:\\Users\\laura\\.cache\\kagglehub\\datasets\\ananthr1\\weather-prediction"

#check if dataset is already downloaded
def download_dataset():
    if not os.path.exists(dataset_path):
        path = kagglehub.dataset_download("ananthr1/weather-prediction")
        print(f"Dataset downloaded to: {path}")
    else:
        print(f"Dataset already exists at: {dataset_path}")

#check if the dataset file exists at the specified path
def validate_dataset():
    if os.path.exists(dataset_path):
        print("Dataset folder exists.")
    else:
        print(f"Error: The dataset folder at {dataset_path} does not exist.")
