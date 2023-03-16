import requests
import pandas as pd
import random
from io import StringIO
#from trade_data import Trade, Order


class Zerodha: 
    quote = "https://api.kite.trade/quote?i="
    instruments_url = "https://api.kite.trade/instruments"
    api_key = "88yyxwtzevcdxuhg"
    access_token = "ES7FDFHGkpw5Yqh5haTb06CWgCELVEFx"
    headers = {"X-Kite-Version" : "3", "Authorization" : f"token {api_key}:{access_token}"}
    expiry_date = '2023-03-29'
    index_symbol = 'BANKNIFTY23MARFUT'
    sl_hit_thresold = 2
    qty = 25 
    
    def get_option_instruemnts():        
        inst = requests.get(Zerodha.instruments_url + '/NFO', headers=Zerodha.headers).text
        df_fno = pd.read_csv(StringIO(inst))
        df_options = df_fno[df_fno.segment == 'NFO-OPT']
        return df_options
    
    def get_instruments():        
        inst = requests.get(Zerodha.instruments_url + '/NSE', headers=Zerodha.headers).text
        df_stocks = pd.read_csv(StringIO(inst))
        print(df_stocks)
        #df_options = df_fno[df_fno.segment == 'NFO-OPT']
        return df_stocks
    

    def get_ltp(symbol):
        url = f"https://api.kite.trade/quote/ltp?i={symbol}"
        response = requests.request("GET", url, headers=Zerodha.headers, data={}).json()
        ltp =  response["data"][symbol]["last_price"]
        return ltp
    
    def get_quotes(symbols):
        res = requests.get(Zerodha.quote + symbols, headers=Zerodha.headers).json()
        df = pd.DataFrame(res['data'])
        df = df.T
        df1 = df['ohlc'].apply(pd.Series)
        df.drop(['depth', 'ohlc', 'last_quantity', 'lower_circuit_limit', 'upper_circuit_limit'], 1, inplace=True)
        df = pd.concat([df, df1], axis=1)
        return df