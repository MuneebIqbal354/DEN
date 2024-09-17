<h1 align="center">Task No. 2</h1>

# Web Scraper: Largest U.S. Companies

This script extracts a table of the largest companies in the United States by revenue from a Wikipedia page and exports it as a CSV file.

## Prerequisites
Before running the code, make sure you have the following installed:
* Python 3.x
* Required libraries:
  1. `requests`
  2. `BeautifulSoup` (from `bs4`)
  3. `pandas`

You can install these libraries using pip:
```
pip install requests beautifulsoup4 pandas
```

## Code Explanation
### 1. Importing Libraries
The code uses three main libraries:

* __requests:__ To make an HTTP request and fetch the HTML content from Wikipedia.
* __BeautifulSoup:__ To parse the HTML content and find specific elements on the page.
* __pandas:__ To store the extracted data and save it in CSV format.

```
from bs4 import BeautifulSoup
import requests
import pandas as pd
```

### 2. URL and Request
We define the URL for the Wikipedia page containing the list of companies and make a request to fetch the page content.
```
urls = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(urls)
soup = BeautifulSoup(page.text, 'html.parser')
```
### 3. Extracting the Table
Using BeautifulSoup, the script finds the first table (`table[0]`) on the page and extracts all table headers (`th` elements).
```
table = soup.find_all('table')[0]
world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]
```

### 4. Creating a DataFrame
A pandas DataFrame is created with columns corresponding to the table headers.
```
data_frame = pd.DataFrame(columns=world_table_titles)
```

### 5. Parsing Table Rows
The script iterates over the table rows (tr elements), extracting the text data from each cell (td elements) and appending it to the DataFrame.
```
column_data = table.find_all('tr')

for rows in column_data[1:]:
    row_data = rows.find_all('td')
    individiual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(data_frame)
    data_frame.loc[lenght] = individiual_row_data
```
### 6. Exporting Data to CSV
Finally, the data is exported to a CSV file with the path specified.
```
data_frame.to_csv(r'C:\Users\Muneeb Iqbal\OneDrive\DEN Internship\Task 2\webscrapper_data.csv', index=False)
```
## Output
The output CSV file will contain the extracted data in tabular format.


  ![Screenshot 2024-09-17 210249](https://github.com/user-attachments/assets/d74d8236-9c39-4dde-a801-70844212b23f)
