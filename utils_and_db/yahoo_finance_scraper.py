import utils_and_db.list_of_tickers as tick
import numpy as np
import yfinance as yf
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta


class RandomStockAnalysis:
    """Given a number, generate data for n number of stocks
    from the S&P 500
    """
    def __init__(self, company_nums):
        """Initialise function

        Args:
            company_nums (int): number of companies to retrive data for
        """
        # Number of companies you want to analyse
        self.company_nums = company_nums
        # Start and end dates
        self.today = datetime.today()
        self.start_date = self.today + relativedelta(years=-2)

        self.tickers = self._get_random_tickers()

    def _get_random_tickers(self):
        """Generates a list of indices to find rand ticker

        Returns:
            list: random tickers from S&P 500
        """
        # Get selection of tickers to analyse
        random_numbers = [
            np.random.randint(0, len(tick.list_of_tickers))
            for i in range(self.company_nums)
        ]
        return [tick.list_of_tickers[x] for x in random_numbers]

    @property
    def return_data(self):
        """Query Yahoo Finance API, retreive data and clean it

        Returns:
            dp.Dataframe: consolidated dataframe of all downloaded data
        """
        df_list = []
        for ticker in self.tickers:
            try:
                df = yf.download(
                    ticker,
                    start=self.start_date,
                    end=self.today,
                    progress=False,
                )
            except Exception as e:
                print(e)

            # Clean data
            if not df.empty:
                df = df.reset_index()
                df["Ticker"] = ticker
                info = yf.Ticker(ticker).info
                try:
                    df["CompanyName"] = info["longName"]
                except Exception as e:
                    print(e)
                    df["CompanyName"] = "NameNotAvailable"

                df_list.append(df)

        return pd.concat(df_list).reset_index()


