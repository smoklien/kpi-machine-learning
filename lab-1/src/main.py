import pandas as pd
import statistics as sts
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Task 2

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

def calculate_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates and returns descriptive statistics for a DataFrame.
    
    Args:
        df (pandas.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: DataFrame that contains calculated statistics.
    """

    df = df.iloc[:, 1:]
    df = df.apply(pd.to_numeric, errors='coerce')

    statistics = pd.DataFrame({
        'mean': df.mean(),
        'median': df.median(),
        'mode': df.apply(lambda x: x.mode()[0] if len(x.mode()) == 1 else None),
        'std_dev': df.std(),
        'variance': df.var()
    })

    return statistics

# Task 3

def plot_statistics(statistics: pd.DataFrame, column: str) -> None:
    """Plots a bar chart for a specific column in a DataFrame of statistics.
    
    Args:
        statistics (pandas.DataFrame): The input DataFrame.
        column (str): The column for which to plot the bar chart.

    Returns:
        None
    """

    # Check if column exists in DataFrame
    if column not in statistics.columns:
        print(f"Column '{column}' not found in DataFrame.")
        return
    
    # Check if there is data in the column
    numeric_mode = pd.to_numeric(result[column], errors='coerce')

    if numeric_mode.dropna().empty:
        print(f"No numeric data to plot in the '{column}' column.")
        return

    # Plot bar chart
    plt.figure(figsize=(10, 6))
    statistics[column].plot(kind='bar', edgecolor='black')
    plt.title(f'{column} of Disposable Income per Capita (Excluding Temporarily Occupied Territories)')
    plt.xlabel('Years')
    plt.ylabel('Value (UAH)')
    plt.show()


df = read_xlsx("statistics.xlsx")
result = calculate_statistics(df)


print('Дані про наявний дохід у розрахунку на одну особу')
print ('-' * 50)
print(df)

print('Статистичні дані')
print ('-' * 50)
print(result)


# # To visualize all numeric columns in your DataFrame
# sns.pairplot(statistics)

# plt.show()


plot_statistics(result, 'mode')
plot_statistics(result, 'mean')
# plot_statistics(statistics, 'mean')
# plot_statistics(statistics, 'median')
# plot_statistics(statistics, 'std_dev')
# plot_statistics(statistics, 'variance')

# plot_statistics(df, 2013)