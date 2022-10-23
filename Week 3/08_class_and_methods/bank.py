class bank :
  def __init__(self,balance):
    self.balace = balance
    self.min_withdraw = 100
    self.max_withdraw = 10000

  def get_balance(self):
    return self.balace

  def withdraw(self,amout):
    if amout < self.min.withdraw:
      return 'no money for you'