from funding_round import FundingRound

class Startup:

   all = []
   
   def __init__(self,name, founder, domain, pivot):
      self.name = name
      self.founder = founder
      self.domain = domain
      self.pivot = pivot
      Startup.all.append(self)

   @property
   def name(self):
      return self._name
   
   @name.setter
   def name(self, new_name):
      if isinstance(new_name, str):
         self._name = new_name
      else:
         raise Exception("Name must be a string")
      
   @property
   def founder(self):
      return self._founder
   
   @founder.setter
   def founder(self, new_founder):
      if not hasattr(self, "_founder"):
         if isinstance(new_founder, str):
            self._founder = new_founder
         else:
            raise Exception("Founder's name must be a string ")
      else:
         raise Exception("Founder cannot be changed")
      
   @property
   def domain(self):
      return self._domain
   
   @domain.setter
   def domain(self, new_domain):
      print('Domain connot be changed')
      
   @property
   def pivot(self):
      return self._pivot
   
   @pivot.setter
   def pivot(self, new_pivot, new_name, new_domain):
      if isinstance((new_domain and new_name), str):
         self._pivot = new_pivot
         self._domain = new_domain
         self._name = new_name
      else:
         raise Exception('Name and Domain must be strings')

   def find_by_founder(self, founder):
      return [s.founder for s in Startup.all if s.founder == founder]
   
   @classmethod
   def domains(self):
      return [s.domain for s in Startup.all]
   
   def sign_contract(self, venture_capitalist, type, investment):
      return FundingRound(self, venture_capitalist, type, investment)
   
   def num_funding_rounds(self):
      return len([f for f in FundingRound.all if f.startup == self])
   
   def total_funds(self):
      return sum([f.investment for f in FundingRound.all if f.startup == self])
   
   def investors(self):
      return list(set([f.venture_capitalist for f in FundingRound.all if f.startup == self]))
   
   def big_investors(self):
      return list(set([f.venture_capitalist for f in FundingRound.all if f.startup == self and f.venture_capitalist.total_worth >= 1000000000]))