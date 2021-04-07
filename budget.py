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

#Show Spending Chart
def create_spend_chart(categories):
  category_length = 0
  category_list = ""
  chart= ""
  percentages = ""
  spending = []
  title = "Percentage spent by category\n"
  total_spent = 0

  #Get spent for each category and Total Spent
  for category in categories:
    spent = 0
    for transaction in category.ledger:
      if transaction["amount"] < 0:
        spent -= float(transaction["amount"])
        total_spent -= spent
    spending.append({
      "category": category.category,
      "spent": spent,
      "percent": 0
    })
    if len(category.category) > category_length:
      category_length = len(category.category)

  #Find percentages
  for i in range(len(spending)):
    spending[i]['percent'] =  abs(int((spending[i]['spent'] / total_spent) * 100))

  #Fill out percentages
  for i in range (100,-1,-10):
    line = str(i).rjust(3) + "|"
    for j in range(len(spending)):
      if spending[j]['percent'] >= i:
        line += " o "
      else:
        line += "".rjust(3)
    line += " \n"
    percentages += line
  equal = "".rjust(4) + "-" * (len(spending) *3 + 1) + "\n"

  #Fill out categories - TODO
  for i in range (0, category_length, 1):
    line = "".rjust(4) 
    for j in range (len(spending)):
      if len(spending[j]['category'][i:i+1]) > 0:
        line += " " + spending[j]['category'][i:i+1]+ " "
      else:
        line += " "*3
    if i + 1 < category_length:
      line += " \n"
    else:
      line += " "
    category_list += line

  #Combine chart components
  chart = title + percentages + equal + category_list
  
  return chart