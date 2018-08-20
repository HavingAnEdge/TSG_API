import requests

class TSG_API():
    """
    API for https://www.thesharegame.com
    You can get more information about each method by calling help(TSG_API.methodName) on it
    Visit https://www.thesharegame.com/api/overview/ to get your own API-Token
    You need to install the python Module "requests" in order to use this module
    Created by James-Smith (ID:10) and HavingAnEdge (ID:76)
    """

    def __init__(self, token):
        self.headers = {"Authorization":"Token %s"%(token)}
        self.baseurl = "https://www.thesharegame.com/api/"

    def get_tsgIndex(self):
        """Returns: All Stock-Index Points"""
        return requests.get(self.baseurl + "tsgindex/", headers=self.headers).json()

    def get_share(self, share_id):
        """Key-Figures about the share with the given id"""
        return requests.get(self.baseurl + "share/%s/"%(share_id), headers=self.headers).json()

    def get_shares(self):
        """Key-Figures of all shares"""
        return requests.get(self.baseurl + "shares/", headers=self.headers).json()

    def get_buyOfShare(self, share_id):
        """All buy orders of the share with the given id"""
        return requests.get(self.baseurl + "buy/of_share/%s/"%(share_id), headers=self.headers).json()

    def get_sellOfShare(self, share_id):
        """All sell orders of the share with the given id"""
        return requests.get(self.baseurl + "sell/of_share/%s/"%(share_id), headers=self.headers).json()

    def get_yourBuy(self):
        """All of your buy orders"""
        return requests.get(self.baseurl + "your/buy/", headers=self.headers).json()

    def get_yourSell(self):
        """All of your sell orders"""
        return requests.get(self.baseurl + "your/sell/", headers=self.headers).json()

    def get_yourDepot(self):
        """All of your depot positions"""
        return requests.get(self.baseurl + "your/depot", headers=self.headers).json()

    def get_shareDepot(self, share_id):
        """Depot of the share with the given id"""
        return requests.get(self.baseurl + "share/%s/depot/" % (share_id), headers=self.headers).json()

    def get_fonds(self):
        """All fonds with its memebers"""
        return requests.get(self.baseurl + "fonds/", headers=self.headers).json()

    def get_futures(self):
        """All Futures"""
        return requests.get(self.baseurl + "futures/tsgx/", headers=self.headers).json()

    def get_trades(self, year, month, day):
        """All Trades of the given day"""
        return requests.get(self.baseurl + "trades/%s/%s/%s/" % (year, month, day), headers=self.headers).json()

    def get_bonds(self):
        """All Bonds"""
        return requests.get(self.baseurl + "bonds/", headers=self.headers).json()

    def get_credits(self):
        """All Credits"""
        return requests.get(self.baseurl + "credits/", headers=self.headers).json()

    def get_monthStats(self, share_id):
        """Month Stats of the share by the given id"""
        return requests.get(self.baseurl + "month/%s/" % (share_id), headers=self.headers).json()

    def get_pastVolume(self, share_id):
        """Past Share, Buy & Sell volume of the share by the given id"""
        return requests.get(self.baseurl + "past/volumes/%s/" % (share_id), headers=self.headers).json()

    def get_pastFigures(self, share_id):
        """Past key figures of the share by the given id"""
        return requests.get(self.baseurl + "past/figures/%s/" % (share_id), headers=self.headers).json()

    def get_marketStats(self):
        """Returns all past Data about the Market"""
        return requests.get(self.baseurl + "market/stats/", headers=self.headers).json()

    def get_pastSharePrice(self, share_id):
        """Returns Bid,Share-Price & Ask of every 5-Min Tick. Currently limited to the last 1000 entries"""
        return requests.get(self.baseurl + "past/share_price/%s/" % (share_id), headers=self.headers).json()

def example():
    print "##### Getting TSGIndex-data #####"
    api = TSG_API("YourToken") #Since tsgIndex-data is free to test, you don't need to pass any token
    tsgIndex = api.get_tsgIndex()
    for datapoint in tsgIndex:
        s = ""
        for key in tsgIndex[0].iterkeys():
            s = s + "%s:%s " %(key, datapoint[key])
        print s

if __name__ == '__main__':

    print "API for thesharegame.com"
    print "Call help(TSG_API) to get more information about the methods"
    print 'Call python -c "import TSG_API; TSG_API.example()" to get an example (getting every record in the tsgIndex)'
    #help(TSG_API)
    #help(TSG_API.get_yourBuy)
    #example()
