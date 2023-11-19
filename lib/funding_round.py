class FundingRound:

    all = []

    def __init__(self, startup, venture_capitalist, type, investment):
        self.startup = startup
        self.venture_capitalist = venture_capitalist
        self.type = type
        self.investment = investment

    @property
    def startup(self):
        return self._startup
    
    @startup.setter
    def startup(self, new_startup):
        if not hasattr(self, "_startup"):
            self._startup = new_startup
        else:
            raise Exception('startup cannot be change')
        
    @property
    def venture_capitalist(self):
        return self._venture_capitalist
    
    @venture_capitalist.setter
    def venture_capitalist(self, new_venture_capitalist):
        if not hasattr(self, '_venture_capitalist'):
            self._venture_capitalist = new_venture_capitalist
        else:
            raise Exception('venture_capitalist cannot be change')
        
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        if isinstance(new_type, str):
            self._type = new_type
        else:
            raise Exception('')
        
    @property
    def investment(self):
        return self._investment
    
    @investment.setter
    def investment(self, new_investment):
        if isinstance(new_investment, float) and new_investment > 0:
            self._investment = new_investment
        else:
            raise Exception('')