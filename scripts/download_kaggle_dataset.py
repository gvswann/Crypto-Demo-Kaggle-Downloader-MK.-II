import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate
api = KaggleApi()
api.authenticate()

# Set download location
download_dir = os.path.join(os.getcwd(), "data")

# Download the dataset (replace with your dataset slug)
dataset = 'paveljurke/crypto-prices-historical-data'
api.dataset_download_files(dataset, path=download_dir, unzip=True)

print("✅ Dataset downloaded and unzipped.")
