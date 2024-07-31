import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import numpy as np
from datetime import datetime

'''
Function responsible for extracting necessary information from the site and saving into a DF
'''


def extract_from_web(url, table_attribs):
    page = requests.get(url).text
    data = bs(page, 'html.parser')  # parses the HTML page

    df = pd.DataFrame(columns=table_attribs)  # creates an empty DataFrame with the columns
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')

    for row in rows:  # it will iterate over every row to extract the data and append it to the DF
        col = row.find_all('td')  # it will find every cell in the row
        if len(col) != 0:  # if the row is not empty
                if col[0].find('a') is not None and '—'  not in col[1]:
                        data_dict = {"Country": col[0].a.contents[0],
                                     "GDP_USD_millions": col[1].contents[0]}
                        df1 = pd.DataFrame(data_dict, index=[0])  # creates a data frame from the dictionary
                        df = pd.concat([df, df1], ignore_index=True)  # appends the new data frame to the main DF
    return df


'''
Function responsible for converting the GDP information from currency to float, and from USD (Millions) to USD (Billions) and rounding to 2 decimal places.
'''


def transform(df):
    gdp_list = df["GDP_USD_millions"].tolist()  # transforms the column to a list
    gdp_list = [float("".join(x.split(','))) for x in gdp_list]  # converts the currency into a float
    gdp_list = [np.round(x / 1000, 2) for x in gdp_list]  # round the currency with 2 decimal places
    df["GDP_USD_millions"] = gdp_list  # replaces the value on the DF
    df = df.rename(columns={"GDP_USD_millions": "GDP_USD_billions"})  # renaming the column

    return df


'''
Function to save the DF as 'csv' file 
'''


def load_to_csv(df, csv_path):
    df.to_csv(csv_path)


'''
Load the file into a json
'''


def load_to_json(df, json_path):
    df.to_json(json_path)


'''
Function responsible for the logging
'''


def log(message):
    timestamp_format = '%Y-%n-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_gdp.txt", "a") as f:
        f.write(timestamp + " : " + message + '\n')

