import kagglehub
import matplotlib.pyplot as plt
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("whenamancodes/blood-transfusion-dataset")

print("Path to dataset files:", path)

# Explore the data
df = pd.read_csv(path + "/transfusion.csv")
print(df.head())

# Visualize the data