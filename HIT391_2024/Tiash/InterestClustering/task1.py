# %%

from kneed import KneeLocator
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

# %%

# %% read csv
data = pd.read_csv("kaggle_Interests_group.csv")
data.describe()

# %% find how many null value available
print(data.isna().sum())

# drop null values
# every row has missing value so we cant use dropna


def drop_missing_values_threshold(data, threshold):
    # Initialize an empty list to store indices of columns to drop
    list_of_index = []

    # Get the list of column names from the DataFrame
    columns = list(data.isna().sum().index)

    # Calculate the number of missing values for each column
    missing_values = data.isna().sum().values

    # Iterate over the range of the length of missing values
    for i in range(len(missing_values)):
        # If the number of missing values in the column exceeds the threshold
        if missing_values[i] > threshold:
            # Append the index of the column to the list_of_index
            list_of_index.append(i)

    # Initialize an empty list to store the names of columns to drop
    list_of_columns_to_drop = []

    # Iterate over the list of indices of columns to drop
    for i in list_of_index:
        # Append the column name corresponding to the index to list_of_columns_to_drop
        list_of_columns_to_drop.append(columns[i])

    # Drop the columns listed in list_of_columns_to_drop from the DataFrame
    # axis=1 specifies that columns are being dropped, inplace=True modifies the DataFrame in place
    data.drop(list_of_columns_to_drop, axis=1, inplace=True)

    # Return the modified DataFrame
    return data


df = data.copy()
# df1 = drop_missing_values_threshold(df , 1000)
df1 = data.copy()
df1

# %% still there are some missing value left, fill the missing value with median value
columns = list(df1.columns)
columns.remove("group")
for col in columns:
    median = df1[col].median()
    df1[col].fillna(1-median,  inplace=True)

df1.isna().sum()  # now we have 0 nuill values

df1


# %% in the dataset groups column was catagorical, encode this using labelEncoder
encoder = LabelEncoder()
df1['group'] = encoder.fit_transform(df1['group'])
df1


# %% print unique group values
print(df1['group'].unique())

# %% lets find out the corelation using correlation matrix

# Calculate the correlation matrix
corr_matrix = df1.corr()
corr_matrix


# plt.figure(figsize=(10, 8))
# sns.heatmap(corr_matrix, annot=True, fmt=".2f",
#             cmap='coolwarm', linewidths=0.5, cbar=True)
# plt.title('Correlation Heatmap')
# plt.show()

# %%

mask = np.triu(np.ones_like(corr_matrix, dtype=bool), k=1)
correlation_matrix = corr_matrix.mask(mask)

# Find the pairs with correlation of 1 or -1
fully_correlated_features = corr_matrix[(
    corr_matrix == 1) | (corr_matrix == -1)].stack()

# Print the fully correlated feature pairs
print("Fully correlated feature pairs:", fully_correlated_features)


# %%

# df2 = df1[["group", "grand_tot_interests", "interest47"]]
df2 = df1.copy()

mms = MinMaxScaler()
df2["grand_tot_interests"] = mms.fit_transform(df2[["grand_tot_interests"]])
df2.skew()

# %%
Y = df2["group"]
X = df2.drop(["group"], axis=1)


# %%
inertias = []

for i in range(2, 10):
    kmeans = KMeans(n_clusters=i).fit(X)
    inertias.append(kmeans.inertia_)
print("inertia = ", inertias)
plt.plot(range(2, 10), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()

# %%
kneedle = KneeLocator(range(2, 10), inertias,
                      curve="convex", direction="decreasing")
kneedle.elbow


# %%
kmeans = KMeans(n_clusters=4).fit(X)


# %%
print(set(list(kmeans.labels_)))
plt.figure(figsize=(5, 5))
plt.scatter(X["interest47"], X["grand_tot_interests"], c=kmeans.labels_)
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1], c="red")
for l, x, y in zip(Y, X["interest47"], X["grand_tot_interests"]):
    plt.annotate(l, xy=(x, y))
print("inertia = ", kmeans.inertia_)
