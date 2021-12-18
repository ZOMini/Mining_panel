import pprint

from django.shortcuts import render

from main.parse_2miner import pool_main
from main.parse_binance import main_binance
from main.parse_gminer import main_miner
from main.templatetags.my_decorator import timeit

GM_ADRESSES = [
    'http://192.168.1.52:10293/stat',
    'http://192.168.1.52:10294/stat',
]
EP_BIN_API = {
    'BTCUSDT': 'https://api2.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT',
    'CFXUSDT': 'https://api2.binance.com/api/v3/ticker/24hr?symbol=CFXUSDT',
    'CTXCUSDT': 'https://api2.binance.com/api/v3/ticker/24hr?symbol=CTXCUSDT',
    'NANOUSDT': 'https://api2.binance.com/api/v3/ticker/24hr?symbol=NANOUSDT',
    'USDTRUB': 'https://api2.binance.com/api/v3/ticker/24hr?symbol=USDTRUB',
    'RVNUSDT': 'https://api2.binance.com/api/v3/ticker/24hr?symbol=RVNUSDT',
    'ETHUSDT': 'https://api2.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT',
}
EP_POOL_ALL = {
    'EP_2MINER_RVN' : 'https://rvn.2miners.com/api/accounts/RJph4xK73HBAG2C7uRfD8FBSvWSgKRw4rt',
    # 'EP_FLYPOOL_RVN' : 'https://api-ravencoin.flypool.org/miner/:RJph4xK73HBAG2C7uRfD8FBSvWSgKRw4rt/dashboard',    
}
q1 = ('https://api2.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT')

def _sub_index():
    context = {}
    my_cout_list = []
    for adress in GM_ADRESSES:
        mi_obj = main_miner(adress)
        my_cont =  {f'mi_obj': mi_obj}
        my_cout_list.append(my_cont)
    context = {'mi_obj': my_cout_list}
    bin_obj = []
    for bin_adress in EP_BIN_API.values():
        var_1 = main_binance(bin_adress)
        bin_obj.append(var_1)
    context['bin_obj'] = bin_obj
    for adress in EP_POOL_ALL.values():
        pool_obj = pool_main(adress)
    context['pool_obj'] = pool_obj
    return context

@timeit
def index(request):
    template = 'main/index.html'
    context = _sub_index()
    return render(request, template, context)
 