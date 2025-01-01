import requests
import pandas as pd

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR,TIMESTAMP,FLOAT


def get_data(symbol):

    base_url = "https://api.binance.com"
    endpoint = "/api/v3/klines"

    params = {
        "symbol" : symbol,
        "interval" : "1d",
        "startTime" : 1690848000000,
        "endTime" : 1732924800000
    }

    url = base_url + endpoint

    response = requests.get(url,params=params)

    keys = ["id","symbol","opentime","openprice","highprice","lowprice","closeprice","volume","closetime","assetvolume","trades","baseassetvolume","quoteassetvolume"]

    data_list = []

    for k in range(len(response.json())):

        row_dict = {}
        for i in range(len(keys)):

            if keys[i] == "id":
                row_dict[keys[i]] =  symbol + "_" + str(response.json()[k][0])

            elif keys[i] == "symbol":
                row_dict[keys[i]] = symbol

            elif keys[i] in ["opentime","closetime"]:
                row_dict[keys[i]] = datetime.fromtimestamp((response.json()[k][i-2])/1000)

            else:
                row_dict[keys[i]] = round(float(response.json()[k][i-2]),4)

        data_list.append(row_dict)

    dataframe = pd.DataFrame(data_list)

    return dataframe


def manage_db(dataframe):
    
    db_url = "postgresql+psycopg2://ruben:preludio33@localhost/cryptodb"
    engine = create_engine(db_url)

    dtype = {
        "Id": VARCHAR(50),
        "symbol": VARCHAR(25),
        "opentime": TIMESTAMP,
        "openprice": FLOAT,
        "highprice": FLOAT,
        "lowprice": FLOAT,
        "closeprice": FLOAT,
        "volume": FLOAT,
        "closetime": TIMESTAMP,
        "assetvolume": FLOAT,
        "trades": FLOAT,
        "baseassetvolume": FLOAT,
        "quoteassetvolume": FLOAT,
    }

    dataframe.to_sql(
        name = "cryptoklines",
        con = engine,
        if_exists = "append",
        index = False,
        dtype = dtype
    )





if __name__ == "__main__":
    
    data = get_data(symbol="BTCUSDT")
    manage_db(dataframe=data)

