# python-sql-tableau

Project that uses all three of Python, SQL and Tableau to retrieve, analyse and visualize stock data from the S&P 500.

## Python

Using Yahoo Finance API, main.py will import yahoo_finance_scraper.py and the class RandomStockAnalysis to retrieve S&P stock data for a given number of stocks.

## SQL

Using a SQLite .db file and it's respective python module, insert all new raw data from Yahoo Finance API into stock_data.db.

Once inserted, query the database and return and consolidated csv file that will be used to make the data for the Tableau workbook

## Tableau

Using stock_dat.csv, extract the data into the workbook.

Using various visuals and calculated fields, create a dashboard that can be filtered by Date and Company Name.

Visuals of the dashboard can be found below:

![Alt text](/screenshots/1.png?raw=true "1")
![Alt text](/screenshots/2.png?raw=true "2")
![Alt text](/screenshots/3.png?raw=true "3")
