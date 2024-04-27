# %% [markdown]
# ## Import libraries

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %% [markdown]
# ## Show the first 5 rows of the data

# %%


def show_data(dataframe, n=5):
    """Show the first n rows of the dataframe

    This function is used to show the first n rows of the dataframe.
    Default value of n is 5.
    """
    print(dataframe.head(n))


# %% [markdown]
# ## Explore the dataset

# %%
def explore_dataset(dataframe):
    """Explore the dataset

    This function is used to explore the dataset. It shows basic statistics
    and a pairplot for visual exploration.

    A pairplot is a plot where each row and column of the dataset is plotted against each other.
    This means that there are n^2 plots for a dataset with n features (columns).
    """
    # Basic statistics
    print("Basic Statistics:")
    print(dataframe.describe())

# %% [markdown]
# ## Show the info of the dataframe

# %%


def show_data_info(dataframe):
    """Show the info of the dataframe

    This function is used to show the info of the dataframe. It shows the number of rows, columns, column names, column types, number of non-null values and memory usage.
    It also shows the number of unique values, number of missing values, number of zero values, number of positive values and number of negative values for each column.
    """
    print(dataframe.info())

# %% [markdown]
# ## Show the details of each column

# %%


def show_column_details(dataframe):
    """Show the details of each column

    This function is used to show the details of each column. It shows the column name, column type, number of unique values, unique values, number of missing values, number of zero values, number of positive values and number of negative values for each column.

    If the column type is object, it shows the number of empty strings instead of number of positive and negative values.

    If the number of unique values is less than 10, it shows the unique values.
    """
    columns = dataframe.columns
    print("Column details:")
    print(f"Number of columns: {len(columns)}")
    print()
    for column in columns:
        # Show column name
        print(f"Column name: {column}")

        # Show column type, types are int64, float64, object, bool, datetime64, timedelta[ns]
        print(f"Column type: {dataframe[column].dtype}")

        # Show number of unique values
        print(f"Number of unique values: {dataframe[column].nunique()}")

        # Show unique values if number of unique values is less than 10
        if len(dataframe[column].unique()) < 10:
            print(f"Unique values: {dataframe[column].unique()}")

        # Show number of missing values
        print(f"Number of missing values: {dataframe[column].isnull().sum()}")

        #  if column type is object, show number of empty strings
        if dataframe[column].dtype == "object":
            print(
                f"Number of empty strings: {len(dataframe[dataframe[column] == ''])}")
        # otherwise, show number of zero values, number of positive values and number of negative values
        else:
            # Show number of zero values
            print(
                f"Number of zero values: {len(dataframe[dataframe[column] == 0])}")

            # Show number of positive values
            print(
                f"Number of positive values: {len(dataframe[dataframe[column] > 0])}")

            # Show number of negative values
            print(
                f"Number of negative values: {len(dataframe[dataframe[column] < 0])}")
        print()

# %% [markdown]
# ## Drop missing values

# %%


def drop_missing_values(dataframe):
    """Drop missing values

    This function is used to drop missing values from the dataframe. It drops all rows with missing values.

    Dropping missing values means removing rows with missing values.

    It does not modify the original dataframe. It returns a new dataframe with missing values dropped.
    """
    return dataframe.dropna()

# %% [markdown]
# ## Drop columns

# %%


def drop_columns(dataframe, columns):
    """Drop columns

    This function is used to drop columns from the dataframe. It drops the specified columns.

    Dropping columns means removing columns from the dataframe.
    """
    return dataframe.drop(columns, axis=1)  # axis=1 means columns, axis=0 means rows

# %% [markdown]
# ## Fill missing values

# %%


def fill_missing_values(dataframe, column, strategy="mean"):
    """Fill missing values

    This function is used to fill missing values in the dataframe. It fills missing values with the mean, median, mode or 0. The default strategy is mean. Other strategies are median, mode and 0.

    Filling missing values with mean, median or mode is only possible for numeric columns. Filling missing values with 0 is possible for all columns.

    Filling missing values means replacing missing values with other values. It is also known as imputation.

    It does not modify the original dataframe. It returns a new dataframe with missing values filled.
    """

    if strategy == "mean":
        dataframe[column] = dataframe[column].fillna(dataframe[column].mean())
    elif strategy == "median":
        dataframe[column] = dataframe[column].fillna(
            dataframe[column].median())
    elif strategy == "mode":
        dataframe[column] = dataframe[column].fillna(dataframe[column].mode())
    elif strategy == "filna":
        dataframe[column] = dataframe[column].fillna(0)
    else:
        raise ValueError("Invalid strategy")

# %% [markdown]
# ## Merge two dataframes

# %%


def merge_dataframes(df1, df2, on_column):
    """Merge two dataframes

    This function is used to merge two dataframes. It merges two dataframes on a column.

    Merging two dataframes means combining two dataframes into one dataframe.

    Here is an example of how to use this function:

    Original dataframe 1:
        ID  Score
    0   1     70
    1   2     80
    2   3     90

    Original dataframe 2:
        ID Grade
    0   2     B
    1   3     A
    2   4     C

    Merged dataframe on ID:
        ID  Score Grade
    0   2     80     B
    1   3     90     A

    In this case the merged dataframe has 2 rows and 3 columns. Only the common rows are kept. The rows with ID 1 and 4 are dropped. And all columns from both dataframes are kept. The rows are sorted by ID.
    """
    return pd.merge(df1, df2, on=on_column)

# %% [markdown]
# ## Join two dataframes

# %%


def join_dataframes(df1, df2, on_column):
    """Join two dataframes

    This function is used to join two dataframes. It joins two dataframes on a column.

    Joining two dataframes means combining two dataframes into one dataframe.


    Here is an example of how to use this function:

    Original dataframe 1:
        ID  Score
    0   1     70
    1   2     80
    2   3     90

    Original dataframe 2:
        ID Grade
    0   2     B
    1   3     A
    2   4     C

    Case 1:
    Joined dataframe 1 on dataframe 2 using ID:
    ID  Score Grade
    1      70   NaN
    2      80     B
    3      90     A

    Case 2:
    Joined dataframe 2 on dataframe 1 using ID:
    ID  Score Grade
    2      80     B
    3      90     A
    4     NaN     C

    In the first case, dataframe 1 is joined on dataframe 2, so all rows from dataframe 1 are kept.

    In the second case, dataframe 2 is joined on dataframe 1, so all rows from dataframe 2 are kept.

    In both cases, the rows are sorted by ID.
    """
    return df1.join(df2.set_index(on_column), on=on_column)

# %% [markdown]
# ## Concatenate two dataframes

# %%


def concatenate_dataframes(df1, df2):
    """Concatenate two dataframes

    This function is used to concatenate two dataframes. It concatenates two dataframes on the columns.

    Concatenating two dataframes means combining two dataframes into one dataframe.

    Here is an example of how to use this function:

    Original dataframe 1:
        ID  Score
    0   1     70
    1   2     80
    2   3     90

    Original dataframe 2:
        ID Grade
    0   2     B
    1   3     A
    2   4     C

    Concatenated dataframe:
        ID  Score  ID Grade
    0   1     70   2     B
    1   2     80   3     A
    2   3     90   4     C

    In this case the concatenated dataframe has 3 rows and 4 columns. All rows from both dataframes are kept. And all columns from both dataframes are kept.
    """
    return pd.concat([df1, df2], axis=1)

# %% [markdown]
# ## Show scatter plot

# %%


def show_scatter_plot(dataframe, x, y):
    """Show scatter plot

    This function is used to show a scatter plot. It shows a scatter plot of the specified columns.

    A scatter plot is a plot where each point represents a row in the dataframe. The x-axis represents the values of the first column and the y-axis represents the values of the second column.
    """
    plt.scatter(dataframe[x], dataframe[y])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

# %% [markdown]
# ## Show bar plot

# %%


def show_bar_plot(dataframe, x, y):
    """Show bar plot

    This function is used to show a bar plot. It shows a bar plot of the specified columns.

    A bar plot is a plot where each bar represents a row in the dataframe. The x-axis represents the values of the first column and the y-axis represents the values of the second column.
    """
    plt.bar(
        dataframe[x],
        dataframe[y],
        color="green",
        width=0.5,
    )
    plt.xlabel(x)
    plt.ylabel(y)
    plt.show()

# %% [markdown]
# ## Show histogram

# %%


def show_histogram(dataframe, column):
    """Show histogram

    This function is used to show a histogram. It shows a histogram of the specified column.

    A histogram is a plot where each bar represents a range of values. The x-axis represents the range of values and the y-axis represents the frequency of values in that range.
    """

    plt.hist(
        dataframe[column],
        bins=20,
        rwidth=0.9,
        color='blue',
        alpha=0.5,
        edgecolor='black',
        linewidth=1.2,
    )
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# %% [markdown]
# ## Show box plot

# %%


def show_box_plot(dataframe, x, y):
    """Show box plot

    This function is used to show a box plot. It shows a box plot of the specified columns.

    A box plot is a plot where each box represents a range of values. The x-axis represents the range of values and the y-axis represents the frequency of values in that range.
    """
    sns.boxplot(
        x=x,
        y=y,
        data=dataframe,
        palette="Set3",
        linewidth=1,
        width=0.5,
        showmeans=True,
        meanprops={
            "marker": "x",
            "markerfacecolor": "white",
            "markeredgecolor": "black",
            "markersize": "5",
        },
        showfliers=False,
    )
    plt.show()

# %% [markdown]
# ## Show heatmap

# %%


def show_heatmap(dataframe):
    """Show heatmap

    This function is used to show a heatmap. It shows a heatmap of the correlation between columns.

    A heatmap is a plot where each cell represents the correlation between two columns. The x-axis represents the first column and the y-axis represents the second column.
    """
    sns.heatmap(dataframe.corr(), annot=True)
    plt.show()

# %% [markdown]
# ## Read dataset


# %%
df1 = pd.read_csv('Australia.csv')
df2 = pd.read_csv('National.csv')

# %% [markdown]
# ## Show dataset

# %%
show_data(df1)

# %%
show_data(df2)

# %%
show_data_info(df1)
print()
print()
show_data_info(df2)

# %% [markdown]
# ### The first dataframe has a column named ICU. The column name has a space at the beginning. We will remove the space.

# %%
# remove space from column names
# remove space from start and end of column names
df1.columns = df1.columns.str.strip()
# remove space from start and end of column names
df2.columns = df2.columns.str.strip()


# %%
show_data_info(df1)
print()
print()
show_data_info(df2)

# %%
show_data_info(df1)
print()
print()
show_data_info(df2)

# %%
show_data(df1)
print()
print()
show_data(df2)

# %% [markdown]
# ### The first dataframe has a column named Hospital, which contains numeric values but because of the comma in the numbers it is considered as a string. We need to remove the comma and convert the column to numeric.

# %%
# remove comma from numbers
df1['Hospital'] = df1['Hospital'].str.replace(',', '')

# convert to numeric
df1['Hospital'] = pd.to_numeric(df1['Hospital'])
print(df1)

# %%
explore_dataset(df1)
print()
print()
explore_dataset(df2)

# %%
show_column_details(df1)

# %%
show_column_details(df2)

# %% [markdown]
# ### In the first dataframe, the column named "Hospitalisations exc. QLD / NT incidental admissions" has no values. We will drop this column.

# %%
df1 = drop_columns(
    df1,  # dataframe to drop columns from
    ['Hospitalisations exc. QLD / NT incidental admissions'],  # columns to drop
)
print(df1)

# %% [markdown]
# ## Show histogram of the first dataframe

# %%
show_histogram(df1, 'Hospital')

# %%
show_histogram(df1, 'ICU')

# %%
show_histogram(df2, 'AUS')

# %% [markdown]
# ## Show bar plots

# %%
show_bar_plot(df1, 'Date', 'Hospital')

# %%
show_bar_plot(df1, 'Date', 'ICU')

# %%
show_bar_plot(df2, 'Date', 'AUS')

# %% [markdown]
# ## Find the max value of ICU and Hospital

# %%
icu_max = df1['ICU'].max()
icu_max_date = df1[df1['ICU'] == icu_max]['Date'].values[0]

icu_min = df1['ICU'].min()
icu_min_date = df1[df1['ICU'] == icu_min]['Date'].values[0]

hospital_max = df1['Hospital'].max()
hospital_max_date = df1[df1['Hospital'] == hospital_max]['Date'].values[0]

hospital_min = df1['Hospital'].min()
hospital_min_date = df1[df1['Hospital'] == hospital_min]['Date'].values[0]

print(f"Highest ICU count: {icu_max} on date {icu_max_date}")
print(f"Lowest ICU count: {icu_min} on date {icu_min_date}")

print(f"Highest hospital count: {hospital_max} on date {hospital_max_date}")
print(f"Lowest hospital count: {hospital_min} on date {hospital_min_date}")


# %% [markdown]
# ## Find the max value of AUS

# %%
death_max = df2['AUS'].max()
death_max_date = df2[df2['AUS'] == death_max]['Date'].values[0]

death_min = df2['AUS'].min()
death_min_date = df2[df2['AUS'] == death_min]['Date'].values[0]

print(f"Highest AUS count: {death_max} on date {death_max_date}")
print(f"Lowest AUS count: {death_min} on date {death_min_date}")

# %% [markdown]
# ### These values are outliers. Outliers are extreme values that deviate from other observations on data , they may indicate a variability in a measurement, experimental errors or a novelty. Outliers can cause serious problems in statistical analyses.

# %%
show_box_plot(df1, 'Date', 'ICU')

# %%
show_box_plot(df1, 'Date', 'Hospital')

# %%
show_box_plot(df2, 'Date', 'AUS')

# %%
numerical_columns = [
    column for column in df1.columns if df1[column].dtype != "object"]
for column in numerical_columns:

    # Plot the graphs
    fig3 = plt.figure(figsize=(20, 15))
    # Title for the whole figure
    fig3.suptitle("Profile of " + column, fontsize=25)
    plt.subplots_adjust(wspace=0.4, hspace=0.35)

    ax1 = fig3.add_subplot(2, 2, 1)
    ax1.set_title("Box Plot", fontsize=20)
    plt.setp(ax1.get_xticklabels(), fontsize=10)
    plt.setp(ax1.get_yticklabels(), fontsize=15)
    ax1.boxplot(df1[column])

    ax1 = fig3.add_subplot(2, 2, 2)
    ax1.set_title("Data Distribution", fontsize=20)
    plt.setp(ax1.get_xticklabels(), fontsize=10)
    plt.setp(ax1.get_yticklabels(), fontsize=15)
    ax1.hist(
        df1[column],
        bins=20,
        rwidth=0.9,
        color='blue',
        alpha=0.5,
        edgecolor='black',
        linewidth=1.2,
    )

    plt.subplots_adjust(wspace=0.4, hspace=0.35)
    plt.show()

    skewness = df1[column].skew()
    print("Skewness of " + column + " is " + str(skewness))

    if skewness > 0:
        print("The data is positively skewed")
        print("Positive skewness means that the data is concentrated on the left side of the graph")
    elif skewness < 0:
        print("The data is negatively skewed")
        print("Negative skewness means that the data is concentrated on the right side of the graph")
    else:
        print("The data is not skewed")

        print("The data is normally distributed")

    print()

    kurtosis = df1[column].kurtosis()
    print("Kurtosis of " + column + " is " + str(kurtosis))

    if kurtosis > 3:
        print("The data is heavy-tailed")
        print("Heavy-tailed means that the data has outliers")
    elif kurtosis < 3:
        print("The data is light-tailed")
        print("Light-tailed means that the data has no outliers")
    else:
        print("The data is normally distributed")

# %%
numerical_columns = [
    column for column in df2.columns if df2[column].dtype != "object"]
print(numerical_columns)

for column in numerical_columns:
    # Plot the graphs
    fig3 = plt.figure(figsize=(20, 15))
    # Title for the whole figure
    fig3.suptitle("Profile of " + column, fontsize=25)
    plt.subplots_adjust(wspace=0.4, hspace=0.35)

    ax1 = fig3.add_subplot(2, 2, 1)
    ax1.set_title("Box Plot", fontsize=20)
    plt.setp(ax1.get_xticklabels(), fontsize=10)
    plt.setp(ax1.get_yticklabels(), fontsize=15)
    ax1.boxplot(
        df2[column],
    )

    ax1 = fig3.add_subplot(2, 2, 2)
    ax1.set_title("Data Distribution", fontsize=20)
    plt.setp(ax1.get_xticklabels(), fontsize=10)
    plt.setp(ax1.get_yticklabels(), fontsize=15)
    ax1.hist(
        df2[column],
        bins=20,
        rwidth=0.9,
        color='blue',
        alpha=0.5,
        edgecolor='black',
        linewidth=1.2,
    )

    plt.subplots_adjust(wspace=0.4, hspace=0.35)
    plt.show()

    skewness = df2[column].skew()
    print("Skewness of " + column + " is " + str(skewness))

    if skewness > 0:
        print("The data is positively skewed")
        print("Positive skewness means that the data is concentrated on the left side of the graph")
    elif skewness < 0:
        print("The data is negatively skewed")
        print("Negative skewness means that the data is concentrated on the right side of the graph")
    else:
        print("The data is not skewed")

        print("The data is normally distributed")

    print()

    kurtosis = df2[column].kurtosis()
    print("Kurtosis of " + column + " is " + str(kurtosis))

    if kurtosis > 3:
        print("The data is heavy-tailed")
        print("Heavy-tailed means that the data has outliers")
    elif kurtosis < 3:
        print("The data is light-tailed")
        print("Light-tailed means that the data has no outliers")
    else:
        print("The data is normally distributed")

# %% [markdown]
# ### These two csv files are not complete on their own. We need to merge them to get the complete data. We will merge them on the column named "Date".
#
# ## Show the first 5 rows of the merged dataframe

# %%
merged_df = merge_dataframes(df1, df2, 'Date')
print(merged_df)

# %%
show_data_info(merged_df)

# %%
columns = merged_df.columns
print(columns)

# %% [markdown]
# ### AUS column should be named to Death

# %%
# change column name from AUS to Avg_Death
merged_df = merged_df.rename(columns={'AUS': 'Avg_Death'})
print(merged_df)

# %%
show_column_details(merged_df)

# %%
# drop the missing values
merged_df = drop_missing_values(merged_df)
print(merged_df)

# %%
show_bar_plot(merged_df, 'Date', 'Hospital')

# %%
show_bar_plot(merged_df, 'Date', 'Hospital')

# %%
show_bar_plot(merged_df, 'Date', 'Avg_Death')
