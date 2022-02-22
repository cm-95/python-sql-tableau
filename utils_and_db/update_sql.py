import sqlite3 as sql
import os
import pandas as pd


class Database:
    """Class to interact with SQLite Database
    """
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(self.path, "stock_data.db")
        self.con = sql.connect(self.db)
        self.curs = self.con.cursor()
        self.BASE_QUERY = """INSERT INTO stock_analysis (Date, Open, High, Close, AdjClose, Volume, Ticker, CompanyName) 
                             VALUES ('{}', {}, {}, {}, {}, {}, '{}', '{}')"""

    def insert_data_to_db(self, df):
        """Insert new data points into the database

        Args:
            df (dp.Dataframe): all data being inserted into database
        """
        for index in df.index:
            try:
                q = self.BASE_QUERY.format(
                    df.at[index, "Date"],
                    df.at[index, "Open"],
                    df.at[index, "High"],
                    df.at[index, "Close"],
                    df.at[index, "Adj Close"],
                    df.at[index, "Volume"],
                    df.at[index, "Ticker"],
                    df.at[index, "CompanyName"],
                )
                self.curs.execute(q)

            except sql.Error as error:
                print("Failed to update sqlite table", error)    

        if self.con:
            self.con.commit()
            self.curs.close()
            print("The SQLite connection is closed")
    
    def get_last_n_days_per_ticker(self, days):
        """Query the last n amount of days for all distinct tickers from database

        Args:
            days (int): number of days we want to query

        Returns:
            pd.DataFrame: consolidated dataframe
        """

        Q = '''SELECT * 
            FROM stock_analysis t1
            WHERE t1.ID IN
                (SELECT t2.Id 
                FROM stock_analysis t2
                WHERE t2.Ticker = t1.Ticker
                ORDER by t2.Date DESC
                LIMIT {}
                );'''

        q = Q.format(days)
        self.con = sql.connect(self.db)
        return pd.read_sql_query(q, self.con)
