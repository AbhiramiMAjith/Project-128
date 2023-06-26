from bs4 import BeautifulSoup
import pandas as pd, time
from selenium import webdriver
from selenium.webdriver.common.by import By

NEW_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs#Field_brown_dwarfs"

browser = webdriver.Chrome("C:/Users/Abhirami M Ajith/Downloads/Project 127/chromedriver.exe")
browser.get(NEW_URL)

time.sleep(10)

scraped_data = []

def new_scrape():
    soup = BeautifulSoup(browser.page_source,'html.parser')

    table_tag = soup.find("table", attrs={"class","wikitable"})
    tbody_tag = table_tag.find("tbody")
    tr_tag = tbody_tag.find_all("tr")

    for td_tag in tr_tag:
        column_data = td_tag.find_all('td')
        temp_list = []

        for col_data in column_data:
            data = col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)

    stars_data = []

    for i in range(0, len(scraped_data)):
        Star_names = scraped_data[i][0]
        Distance = scraped_data[i][5]
        Mass = scraped_data[i][7]
        Radius = scraped_data[i][8]

        required_data = [Star_names, Distance, Mass, Radius]
        stars_data.append(required_data)
        
        headers = ['Star_name','Distance', 'Mass','Radius']

        star_df_2 = pd.DataFrame(stars_data, columns=headers)
        star_df_2.to_csv('new_scraped_data.csv', index = True, index_label='id')

new_scrape()