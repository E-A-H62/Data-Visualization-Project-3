import kagglehub
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Download latest version
path = kagglehub.dataset_download("whenamancodes/blood-transfusion-dataset")
#print("Path to dataset files:", path)

# Explore the data
df = pd.read_csv(path + "/transfusion.csv")
#print(df.head())

# Visualize the data
categorical_cols = ['Recency (months)', 'Frequency (times)', 'Monetary (c.c. blood)', 'Time (months)']
donated = df.loc[df['whether he/she donated blood in March 2007'] == 1, categorical_cols]
not_dontated = df.loc[df['whether he/she donated blood in March 2007'] == 0, categorical_cols]
# print(donated.head())
# print(not_dontated.head())
w, x = 0.4, np.arange(len(categorical_cols))

# BASIC VISUALIZATIONS (CAN BE EDITED/MODIFIED)
# Sum of Categorical Columns by Donation Status
plt.bar(x - w/2, donated.sum(), width=w, label='Donated')
plt.bar(x + w/2, not_dontated.sum(), width=w, label='Not Donated')
plt.xticks(x, categorical_cols, rotation=45)
plt.xlabel('Categorical Columns')
plt.ylabel('Sum')
plt.title('Sum of Categorical Columns by Donation Status')
plt.legend()
plt.show()
# Mean of Categorical Columns by Donation Status
plt.bar(x - w/2, donated.mean(), width=w, label='Donated')
plt.bar(x + w/2, not_dontated.mean(), width=w, label='Not Donated')
plt.xticks(x, categorical_cols, rotation=45)
plt.xlabel('Categorical Columns')
plt.ylabel('Mean')
plt.title('Mean of Categorical Columns by Donation Status')
plt.legend()
plt.show()

# Distribution of Categorical Columns by Donation Status
# for col in categorical_cols:
#     sns.histplot(donated[col], label='Donated')
#     sns.histplot(not_dontated[col], label='Not Donated')
#     plt.xlabel(col)
#     plt.ylabel('Count')
#     plt.title(f'Distribution of {col} by Donation Status')
#     plt.legend()
#     plt.show()

# Stacked bar chart (TBD)


# Scatterplot matrix
sns.pairplot(df, hue='whether he/she donated blood in March 2007')
plt.show()