class Category:
  def __init__(self, category):
    self.amount = 0
    self.category = category
    self.ledger = []

  #Build balance sheet
  def __str__(self):
    balance_sheet = ""
    title = f"{self.category:*^30}\n"
    total = "Total:" + '{:,.2f}'.format(self.get_balance()).rjust(7)
    for transaction in self.ledger:
      amount = ""
      description = ""
      for key,value in transaction.items():
        if key == 'amount':
          amount = '{:,.2f}'.format(value).rjust(7)
        elif key == 'description':
          description = value[:23].ljust(23)
      
      balance_sheet += description + amount + "\n"
    return str(title) + balance_sheet + total

  #Deposit Funds
  def deposit(self, amount, description=""):
    self.amount += amount
    self.ledger.append({"amount": amount, "description": description})
    
  #Withdraw Funds
  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.amount -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  #Return Balance
  def get_balance(self):
    return self.amount

  #Transfer Funds  
  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.amount -= amount
      self.ledger.append({"amount": -amount, "description": "Transfer to " + category.category})
      category.ledger.append({"amount": amount, "description": "Transfer from " + self.category})
      return True
    else:
      return False

  #Check Balance
  def check_funds(self, amount):
    if self.amount >= amount:
      return True
    return False

def create_spend_chart(categories):
  return ""