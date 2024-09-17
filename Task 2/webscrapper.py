from bs4 import BeautifulSoup
import requests
import pandas as pd

urls = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(urls)
soup = BeautifulSoup(page.text, 'html.parser')

# print (soup)

table = soup.find_all('table')[0]
# print (table)

# print(soup.find('table', class_= 'wikitable sortable'))

world_titles = table.find_all('th')

world_table_titles = [title.text.strip() for title in world_titles]
# print (world_table_titles)

data_frame = pd.DataFrame(columns = world_table_titles)

column_data = table.find_all('tr')

for rows in column_data[1:]:
    row_data = rows.find_all('td')
    individiual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(data_frame)
    data_frame.loc[lenght] = individiual_row_data

data_frame.to_csv(r'C:\Users\Muneeb Iqbal\OneDrive\DEN Internship\Task 2\webscrapper_data.csv', index = False)