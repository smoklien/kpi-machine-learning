import pandas as pd
import statistics as sts
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1

def read_xlsx(name: str) -> pd.DataFrame:
    """Reads an excel file from the parent directory.

    Args:
        name: The name of the excel file in the parent directory.

    Returns:
        A pandas DataFrame containing the data from the excel file.
    """

    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, '..', name)
    
    return pd.read_excel(file_path)

# Task 2

def calculate_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates and returns descriptive statistics for a DataFrame.
    
    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: DataFrame that contains calculated statistics.
    """

    # Exclude the row for 'України'
    df = df[df['Регіони та області'] != 'України']

    # Select only numeric columns and convert them to numeric type
    numeric_df = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

    statistics = pd.DataFrame({
        'mean': numeric_df.mean(),
        'median': numeric_df.median(),
        'mode': numeric_df.apply(lambda x: x.mode()[0] if len(x.mode()) == 1 else None),
        'std_dev': numeric_df.std(),
        'variance': numeric_df.var()
    })

    return statistics

# Task 3

def plot_df(df: pd.DataFrame, column: str) -> None:
    """Plots a bar chart for a specific column in a DataFrame.
    
    Args:
        df (pandas.DataFrame): The input DataFrame.
        column (str): The column for which to plot the bar chart.

    Returns:
        None
    """

    # Check if column exists in DataFrame
    if column not in df.columns:
        print(f"Column '{column}' not found in DataFrame.")
        return
    
    df = df.apply(pd.to_numeric, errors='coerce')

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    df[column].plot(kind='bar', edgecolor='black', color='orange')
    plt.title(f'Disposable Income per Capita (Excluding Temporarily Occupied Territories) in {column}')
    plt.xlabel('Regions')
    plt.ylabel('Value (UAH)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# def plot_stats(df: pd.DataFrame, column: str) -> None:
#     """Plots a bar chart for a specific column in a DataFrame of statistics.
    
#     Args:
#         df (pandas.DataFrame): The input DataFrame.
#         column (str): The column for which to plot the bar chart.

#     Returns:
#         None
#     """

#     # Check if column exists in DataFrame
#     if column not in df.columns:
#         print(f"Column '{column}' not found in DataFrame.")
#         return
    
#     # Check if there is data in the column
#     numeric_mode = pd.to_numeric(df[column], errors='coerce')

#     if numeric_mode.dropna().empty:
#         print(f"No numeric data to plot in the '{column}' column.")
#         return

#     # Plot bar chart
#     plt.figure(figsize=(10, 6))
#     df[column].plot(kind='bar', edgecolor='black', color='orange')
#     plt.title(f'{column} of Disposable Income per Capita (Excluding Temporarily Occupied Territories)')
#     plt.xlabel('Years')
#     plt.ylabel('Value (UAH)')
#     plt.show()


raw_df = read_xlsx("statistics.xlsx")
statistics_df = calculate_statistics(raw_df)

# Task 1

# print('Дані про наявний дохід у розрахунку на одну особу')
# print ('-' * 50)
# print(raw_df)

# Task 2

# print('Статистичні дані')
# print ('-' * 50)
# print(statistics_df)

# Task 3

# raw_df.set_index('Регіони та області', inplace=True)
#
# plot_df(raw_df, 2013)
# plot_df(raw_df, 2015)

# Task 4

# 1.
series = pd.Series(raw_df[2013])
print(series)

# 2.

raw_df.head()
# 3. 

# 4. 

# 5. 

# 6.

# 7.

# 8. 

# 9. 

# 10. 

# 11.