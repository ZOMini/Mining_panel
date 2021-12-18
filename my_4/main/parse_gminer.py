import datetime
import logging
import pprint
from http import HTTPStatus

import requests


class MyDict:
    logging.basicConfig(
    filename=f'{__name__}.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    encoding='UTF-8',
    filemode='a')
    def __init__(self, gm_response = {}, gm_main = {}, gm_devices = {}):
        self.gm_response = gm_response        
        self.gm_main = gm_main
        self.gm_devices = gm_devices
    
    def __str__(self):
        gm_main =  self.gm_main
        gm_devices = self.gm_devices
        return print(gm_main, gm_devices)
 
    def miner_api(self, adress):
        try:
            response = requests.get(adress)
        except Exception as e:
            logging.error(f'Error requests: {e}.')
            raise
        if response.status_code != HTTPStatus.OK:
            logging.error(f'Error requests status code: {response.status_code}')
            raise
        self.gm_response = response.json()
        
    def parse_gminer(self):
        q1 = dict(self.gm_response)
        del q1['total_stale_shares']
        del q1['total_invalid_shares']
        del q1['speed_rate_precision']
        del q1['speed_unit']
        del q1['power_unit']
        del q1['devices']
        del q1['total_accepted_shares']
        del q1['total_rejected_shares']
        del q1['extended_share_info']
        q1['uptime'] = datetime.timedelta(seconds=q1['uptime'])
        flo = q1['pool_speed']
        q1['pool_speed'] = f'{(flo / 1000000):.2f} MH/s'
        self.gm_main = dict(q1)
        q1 = list(self.gm_response['devices'])
        for i in range(len(q1)):
            del q1[i]['bus_id']
            del q1[i]['gpu_id']
            del q1[i]['temperature_limit']
            del q1[i]['memory_temperature_limit']
            del q1[i]['stale_shares']
            del q1[i]['invalid_shares']
            flo = q1[i]['speed']
            q1[i]['speed'] = f'{(flo / 1000000):.2f} MH/s'
            q1[i]['fan'] = str(q1[i]['fan']) + ' %'
            q1[i]['temperature'] = str(q1[i]['temperature']) + ' C'
            q1[i]['memory_temperature'] = str(q1[i]['memory_temperature']) + ' C'
        self.gm_devices = q1


def main_miner(adress):
    mi_obj = MyDict()
    mi_obj.miner_api(adress)
    mi_obj.parse_gminer()
    return mi_obj

# if  __name__ == '__main__':
#     main_miner()
