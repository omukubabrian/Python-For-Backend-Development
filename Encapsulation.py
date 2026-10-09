class Wallet:
    def __init__(self,balance:float=0.0)-> None:
      self._balance =balance

    @property
    def balance(self)->float:
      return self._balance

    def spend(self,amount:float)->None:
       if amount >self._balance:

          raise ValueError("Not enough money")
       self._balance-=amount
w=Wallet(50)
w.spend(20)
print(w.balance)
       #w.balance=1000