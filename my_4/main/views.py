import pprint

from django.shortcuts import render

from main.parse_gminer import main_miner
from main.templatetags.my_decorator import timeit

GM_ADRESSES = [
    'http://192.168.1.52:10293/stat',
    'http://192.168.1.52:10294/stat',
    
]
def _sub_index():
    context = {}
    my_cout_list = []
    for adress in GM_ADRESSES:
        mi_obj = main_miner(adress)
        my_cont =  {f'mi_obj': mi_obj}
        my_cout_list.append(my_cont)
    context = {'mi_obj': my_cout_list}
    return context

@timeit
def index(request):
    template = 'main/index.html'
    context = _sub_index()
    return render(request, template, context)
 