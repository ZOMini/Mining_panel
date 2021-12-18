import pprint

from main.parse_gminer import MyDict

items_del = ('24hnumreward', '24hreward', 'apiVersion', 'config', 'sumrewards', 'pageSize', 'payments', 'paymentsTotal', 'rewards', 'roundShares', 'sharesInvalid', 'stats', 'updatedAt', 'workers', 'workersOffline', 'workersTotal')

class PoolDict(MyDict):
    def __init__(self, gm_response = {}, pool_var = {}):
        super().__init__(gm_response)
    
    def miner_api(self, adress):
        super().miner_api(adress)
        
    def parse_pool(self):
        pool_var = self.gm_response
        for item in items_del:
            del pool_var[item]
        flo = float(pool_var['currentHashrate'] / 1000000)
        pool_var['currentHashrate'] = f'{flo:.2f} MH/s'
        flo = float(pool_var['hashrate'] / 1000000)
        pool_var['hashrate'] = f'{flo:.2f} MH/s'
        self.pool_var = pool_var

def pool_main(adress):
    var = PoolDict()
    var.miner_api(adress)
    var.parse_pool()
    return var.pool_var


# if __name__ == '__main__':
#     pool_main()
