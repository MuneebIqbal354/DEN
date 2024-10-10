<h1 align="center">Task No. 5: Data Analysis </h1>

In this project I have performed data analysis on a discrete dataset of student marks and visualizes the findings using Python. It provides insights into student performance through statistical calculations and various plots, such as bar plots, pie charts, and dot plots, using the libraries pandas, matplotlib, and seaborn.

The analysis and visualizations are implemented in Python, using the following tools:

  - `Pandas` for data manipulation
  - `Matplotlib` and Seaborn for creating visualizations

## Features

  - **Mean, Median, Mode Calculation:** Provides the central tendency measures of the student marks.
  - **Bar Plot:** Displays the distribution of marks for each student.
  - **Pie Chart:** Shows the proportion of marks for a specific student.
  - **Dot Plot:** Illustrates individual marks for each student across all subjects.

## Requirements

  - Python 3.x
  - The following Python libraries:
    
      - pandas
      - matplotlib
      - seaborn

You can install the necessary libraries using the following command:

```
pip install pandas matplotlib seaborn
```

## Code

### 1. Import Libraries

Imports the necessary libraries 
  
  - `pandas` for data manipulation and analysis.
  - `matplotlib.pyplot` for creating static, animated, and interactive visualizations.
  - `seaborn` for statistical data visualization.
  - `mode` from the `statistics` library to calculate the mode of the data.

```python
# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import mode
```

### 2. Load Dataset:

Loads the dataset from an Excel file using `pandas`. The variable `df` becomes a DataFrame containing the data.

```python
# Load the dataset (update 'path_to_file' with the actual file path)
file_path = 'C:\\Users\\Muneeb Iqbal\\Desktop\\Book1.xlsx'
df = pd.read_excel(file_path)
```

### 3. Data Analysis: 

Calculates the mean, median, and mode for each column in the DataFrame and print the output.

  - `mean()` computes the average for each column.
  - `median()` finds the middle value.
  - `apply(lambda x: mode(x))` calculates the mode using a lambda function to apply the `mode` function to each column.

```python
# Data Analysis: Calculate mean, median, and mode for each column
# Calculated the mean
mean_values = df.mean()
print(f"Mean values:\n{mean_values}\n")

# Calculated the median 
median_values = df.median()
print(f"Median values:\n{median_values}\n")

# Calculated the mode
mode_values = df.apply(lambda x: mode(x))
print(f"Mode values:\n{mode_values}")
```

### 4. Visualizations: 

Created a bar plot to visualize the distribution of marks for each student.

  - `plt.figure(figsize=(10,6))` sets the size of the plot.
  - `df['Marks'].plot(kind='bar')` generates a bar plot of the marks column from the DataFrame.

```python
# Bar Plot: Display the distribution of marks for each student
plt.figure(figsize=(10,6))
df['Marks'].plot(kind='bar')
plt.title('Bar Plot of Student Marks')
plt.xlabel('Student Index')
plt.ylabel('Marks')
plt.show()
```

Generates a pie chart for the first student’s marks.

  - `autopct='%1.1f%%'` displays the percentage on the pie chart.
  - `startangle=90` rotates the start of the pie chart for better visualization.

```python
# Pie Chart: Show the proportion of marks for one student
plt.figure(figsize=(6,6))
df.iloc[0].plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Pie Chart of Marks for Student 1')
plt.show()
```

Uses a strip plot to display individual student marks for each subject.

  - The `for` loop iterates through each column to plot individual marks with a little jitter for better visibility.

```python
# Dot Plot: Display individual student marks for each subject
df_filtered = df.drop(columns=df.columns[0])

# Plot the updated chart
plt.figure(figsize=(10,6))
for column in df_filtered.columns:
    sns.stripplot(x=df_filtered.index, y=column, data=df_filtered, jitter=True, color = 'orange')
plt.title('Dot Plot of Marks per Student')
plt.xlabel('Student Index')
plt.ylabel('Marks')
plt.show()
```

### 5. Documented the insight: 

Lastly I have documented the analysis findings and insights, the saves the findings in a text file called `data_analysis_findings.txt`.

```python
findings = f"""
Data Analysis Findings:
1. Mean values per subject:
{mean_values}

2. Median values per subject:
{median_values}

3. Mode values per subject:
{mode_values}

Visualization Insights:
1. The bar plot shows the distribution of marks for each student across all subjects.
2. The pie chart highlights the proportion of marks for Student 1 in different subjects.
3. The dot plot illustrates individual marks, helping to observe the spread and distribution of scores across students.
"""

# Save the findings into a text file
with open('data_analysis_findings.txt', 'w') as file:
    file.write(findings)

print("Analysis complete. Findings saved to 'data_analysis_findings.txt'.")
```
