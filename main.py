from etl_project_gdp import extract_from_web, transform, load_to_csv, log, load_to_json

'''
1 - URL
2 - table_attribs: column attributes
3 - db_name: 'World_Economies.db'
4 - table_name: 'Countries_by_GDP'
5 - csv_path: 'Countries_by_GDP.csv'
'''


url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29'
table_attribs = ["Country", "GDP_USD_millions"]
table_name = 'Countries_by_GDP'
csv_path = './Countries_by_GDP.csv'
json_path = './Countries_by_GDP.json'

if __name__ == '__main__':
    log('Initializing ETL')
    df = extract_from_web(url, table_attribs)

    log('Extraction concluded')
    df = transform(df)

    log('Loading Data')
    df = load_to_csv(df, csv_path)

    log('Data saved as CSV''\n' 'Data saved as JSON')
    df = load_to_json(df, json_path)