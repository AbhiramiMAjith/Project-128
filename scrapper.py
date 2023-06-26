from bs4 import BeautifulSoup
import pandas as pd, time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome("C:/Users/Abhirami M Ajith/Downloads/Project 127/chromedriver.exe")
browser.get(URL)

time.sleep(10)

scraped_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,'html.parser')

    table_tag = soup.find("table", attrs={"class","wikitable"})
    tbody_tag = table_tag.find("tbody")
    tr_tag = tbody_tag.find_all("tr")

    for td_tag in tr_tag:
        column_data = td_tag.find_all('td')
        #print(column_data)
        temp_list = []

        for col_data in column_data:
            #print(col_data.text)
            data = col_data.text.strip()
            #print(data)
            temp_list.append(data)
            #print(temp_list)
        scraped_data.append(temp_list)

    stars_data = []

    for i in range(0, len(scraped_data)):
        Star_names = scraped_data[i][1]
        Distance = scraped_data[i][3]
        Mass = scraped_data[i][5]
        Radius = scraped_data[i][6]
        Lum = scraped_data[i][7]

        required_data = [Star_names, Distance, Mass, Radius, Lum]
        stars_data.append(required_data)
        
        headers = ['Star_name','Distance', 'Mass','Radius','Luminosity']

        star_df_1 = pd.DataFrame(stars_data, columns=headers)
        star_df_1.to_csv('scraped_data.csv', index = True, index_label='id')

scrape()