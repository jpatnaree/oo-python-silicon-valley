from funding_round import FundingRound

class VentureCapitalist:
    
    all = []

    def __init__(self, name, total_worth):
        self.name = name
        self.total_worth = total_worth
        VentureCapitalist.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception('')
        
    @property
    def total_worth(self):
        return self._total_worth
    
    @total_worth.setter
    def total_worth(self, new_total_worth):
        if isinstance(new_total_worth, int):
            self._total_worth = new_total_worth
        else:
            raise Exception('')

    @classmethod
    def tres_commas_club(self):
        return [v for v in VentureCapitalist.all if v.total_worth >= 1000000000]
    
    def offer_contract(self, startup, type, investment):
        return FundingRound(self, startup, type, investment)
    
    def funding_rounds(self):
        return [f for f in FundingRound.all if f.venture_capitalist == self]
    
    def portfilio(self):
        return list(set([ f.startup for f in FundingRound if f.venture_capitalist == self]))
    
    def biggest_investment(self):
        return max([f.investment for f in FundingRound.all if f.venture_capitalist == self])
    
    def invested(self, domain):
        return sum([ f.investment for f in FundingRound.all if f.venture_capitalist == self and f.startup.domain == domain])