# EdX: ETL Pipeline Project

## Introduction

In this project, we will create an ETL pipeline to access data from a website and process it as it is required.

## Project

An international firm that is looking to expand its business in different countries across the world has recruited you. You have been hired as a junior Data Engineer and are tasked with creating an automated script that can extract the list of all countries in order of their GDPs in billion USDs (rounded to 2 decimal places), as logged by the International Monetary Fund (IMF). 

Since IMF releases this evaluation twice a year, this code will be used by the organization to extract the information as it is updated.

________________________________________________________________________________________________________________________
URL:
``
https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29
``
________________________________________________________________________________________________________________________

The required information needs to be made accessible as a JSON file 'Countries_by_GDP.json' as well as a table 'Countries_by_GDP' in a database file 'World_Economies.db' with attributes 'Country' and 'GDP_USD_billion.'

## Objectives

1. Write an Extract method, in order to recover the information needed.
2. Transform the available GDP information into `Billion USD` from `Million USD`.
3. Load the transformed information into the necessary `CSV` file.
4. Load the transformed data and record all the steps.


## Initial Setup
Add the following libraries to the code:

1. `requests`- Library used to send HTTP requests to the website and retrieve the HTML content.

2. `bs4`- A library used to extract data from HTML and XML files.

3. `pandas`- A library used to manipulate and analyze data.

5. `numpy`- A library used to perform mathematical operations on arrays.

6. `datetime`- A library used to work with dates and times.


```pip
python3.11 -m pip install pandas
python3.11 -m pip install numpy
python3.11 -m pip install bs4
```

