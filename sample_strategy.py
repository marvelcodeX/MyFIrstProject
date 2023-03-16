from datetime import datetime as dt
import datetime
from zerodha import Zerodha


def start():
    current_time = dt.now().time()    
    
    if ((datetime.time(9, 30) < current_time) and 
        (current_time< datetime.time(15, 25))):
        
        get_quotes("341249")
        print("Hellow")
        
        
def get_quotes(symbols):
    Zerodha.get_instruments()
    last_price = Zerodha.get_ltp(symbols)
    print(last_price)
    
    
            


start()