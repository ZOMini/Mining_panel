from main.parse_gminer import MyDict

ACCESS = ['symbol', 'lastPrice', 'priceChange', 'priceChangePercent', 'weightedAvgPrice', 'highPrice', 'lowPrice']


class BinDict(MyDict):
    def __init__(self, gm_response = {}, bin_var = {}):
        super().__init__(gm_response,)
        self.bin_var = bin_var
        
    def parse_gminer(self):
        bin_var = {}
        dict_var = {}
        gm_response = dict(self.gm_response)
        bin_var = {gm_response['symbol']: {}}
        for k, v in gm_response.items():
            if k in ACCESS:
                dict_var[k] = v
                bin_var[gm_response['symbol']].update(dict_var)
        self.bin_var = bin_var 
        
def main_binance(adress):
    var = BinDict()
    var.miner_api(adress)
    var.parse_gminer()
    return(var.bin_var)


# if __name__ == '__main__':
#     main_binance('https://api2.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT')
