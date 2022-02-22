from utils_and_db.yahoo_finance_scraper import RandomStockAnalysis
from utils_and_db.update_sql import Database
import os


if __name__ == "__main__":
    # number of stocks you want to analyse:
    NUM_STOCK = 1
    rsa = RandomStockAnalysis(NUM_STOCK).return_data

    sql = Database()
    sql.insert_data_to_db(rsa)

    DAYS = 10
    data = sql.get_last_n_days_per_ticker(500)
    path = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(path, "stock_data.csv")
    data.to_csv(csv_path)


    print("end")
