class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    result = ''
    length = (30 - len(self.name)) // 2
    result += '' + ("*" * length) + self.name + ("*" * length)
    balance = self.get_balance()
    for item in self.ledger:
      value = item["amount"]
      desc = item['description']
      result += f"\n{desc[:23]}".ljust(
          25, ' ') + (f"{value:.2f}").rjust(len(str(value)) - 5)
    result += f"\nTotal: {balance}"
    return result

  def deposit(self, amount, description=""):
    return self.ledger.append({"amount": amount, "description": description})

  def get_balance(self):
    result = sum(item["amount"] for item in self.ledger)
    return float(result)

  def check_funds(self, amount):
    return not amount > self.get_balance()  # false if amount > balance

  def withdraw(self, amount, description=""):
    withdraw = False
    if amount < 0.00:
      print("You can't withdraw a negative amount")
    else:
      if self.check_funds(amount):
        self.ledger.append({"amount": -amount, "description": description})
        print("Withdrawal successful")
        withdraw = True
    return withdraw

  def transfer(self, amount, dest):
    transferred = False
    if amount < 0.00:
      print("You can't transfer a negative amount")
    else:
      if self.check_funds(amount):
        self.withdraw(amount, f"Transfer to {dest.name}")
        dest.deposit(amount, f"Transfer from {self.name}")
        transferred = True
      else:
        print("Not enough fund in the source account")

    return transferred


def create_spend_chart(categories):  
  result = f"Percentage spent by category\n"
  balances = [900-cat.get_balance() for cat in categories]
  max_balance = sum(balances)
  length = [len((cat.name)) for cat in categories]
  max_length = max(length)

  for percentage in range(100, -1, -10): 
    result += str(percentage).rjust(3)+ '|' 
    for cat in categories:
      result += " o " if  ((900-cat.get_balance())*100)/max_balance > percentage else "   "

    result += " \n" 
  result += "    -" + ("---" * len(categories)) + "\n"
  for i in range(max_length):
    result += "    "
    for cat in categories:
      result += " " + (str(cat.name)[i] if i < len(str(cat.name)) else " ") + " "
    result += " \n" if i!= max_length-1 else " "
  print("####",result)
  return result

