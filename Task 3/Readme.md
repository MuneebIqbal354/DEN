<h1 align="center">Task No. 3</h1>

# Data Analysis and Visualization Project

This project performs data analysis and visualization on a dataset containing placement data of students. The analysis is implemented using `pandas` and `matplotlib` libraries in Python.

## Dataset

The dataset used in this project is `Placement_Data_Full_Class.csv`, which contains information about the students' academic performance, work experience, placement status, and salary offered.

Dataset link: https://www.kaggle.com/datasets/benroshan/factors-affecting-campus-placement/data

## Prerequisites

Before running the code, make sure you have the following installed:

* Python 3.x
* Required libraries:
  1. `pandas`
  2. `matplotlib`
  
You can install these libraries using pip:

```
pip install pandas
```
```
pip install matplotlib
```

## Code Explanation

The following analyses and visualizations are performed in the Jupyter notebook:

1. **Necessary Libraries:**

   Importing the necessary libraries, `pandas` as and `matplotlib.pyplot`.

    ```python
    import pandas as pd
    import matplotlib.pyplot as plt
    ```
3. **Loading Dataset:**

   The dataset is loaded into a variiable `data_frame` and the `sl_no` column is set as the index.

     ```python
     data_frame = pd.read_csv("Placement_Data_Full_Class.csv")
     data_frame = data_frame.set_index('sl_no')
     data_frame
     ```
     ![image](https://github.com/user-attachments/assets/2e09d671-e381-4a83-a841-5a35fa2405ec)

2. **Gender Distribution:**

   First i have plotted a pie chart to show the distribution of genders in the dataset.

    ```python
    data_frame['gender'].value_counts().plot(kind='pie', title='Gender Distribution', ylabel='', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen'], figsize=(12,8))
    ```
    ![image](https://github.com/user-attachments/assets/549a797a-287a-4bce-a9ac-a1ed89b0f973)


4. **Salary Distribution by Gender:**

   This code sets the gender column as the index and plots a horizontal bar chart showing the salary distribution for each gender, with appropriate axis labels and figure size.

    ```python
    data_frame = data_frame.set_index('gender')
    data_frame['salary'].plot(kind='barh', xlabel='salaries', ylabel='genders', figsize=(12,8))
    ```
    ![image](https://github.com/user-attachments/assets/351a59b9-b5cf-4c22-9642-24108346097f)

6. **Placement Status:**

   This code applies a grayscale style and plots a bar chart showing the count of students who are placed vs not placed.

    ```python
    plt.style.use('grayscale')
    data_frame['status'].value_counts().plot(kind='bar', title='Placed vs Not Placed', xlabel='Status', ylabel='Number of Students', figsize=(8,6))
    ```
    ![image](https://github.com/user-attachments/assets/6f54f089-f3b1-4b0b-90e1-d0df7c91ce6b)

8. **Salary vs. Degree Percentage:**

   Here I have created a scatter plot to show the relationship between students' degree percentages and their salaries

    ```python
    data_frame.plot.scatter(x='degree_p', y='salary', title='Salary vs Degree Percentage', xlabel='Degree Percentage', ylabel='Salary', figsize=(8,6))
    ```
    ![image](https://github.com/user-attachments/assets/9d983ae9-3291-49eb-a6eb-57cdf907dfc2)

10. **Number of Students by Major:**

    Lastly I have plotted another bar chart highlighting the number of students in each higher secondary education specialization (major).
    ```python
    data_frame['hsc_s'].value_counts().plot(kind='bar', title='No of Students vs Major', xlabel='Major', ylabel='Number of Students', color='lightgreen', figsize=(8,6))
    ```
    ![image](https://github.com/user-attachments/assets/5fa470a1-675a-4535-a2d4-64b2535782f0)

## Conclusion

This project provides insights into the placement data of students, including gender distribution, salary distribution by gender, placement status, and the relationship between salary and degree percentage. The visualizations help in understanding the trends and patterns in the data.
